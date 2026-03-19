import pokemon as pk
import trainer as tr
import race as rc
import move as mv
import format_input as form
import os
import paint as pnt
import show_poke as sw
import random as rm
import element as el

## checj if the player or enemy is dead ###

def check_death(player):
    if player.total_life[player.pk_on] == 0:
        all_dead_enemy = True
        for i in player.pokemons:
            if player.total_life[i] > 0:
                player.pk_on = i
                player.setup()
                player.format_attacks()
                all_dead_enemy = False
        if all_dead_enemy == True:
            return True
    else:
        return False

### func mensage down (it doesnt include draw) ###

def mensage(mensage):
    print (f"{'='*100}\n\n{mensage}\n\n\n{'='*100}")
    ok = input("")
    clean()

## clean screen func ##

def clean():
    os.system('cls' if os.name == 'nt' else 'clear')
    ##print("\033[H\033[J", end="")

### draw the 3 functions of battle (faster to write)##

def draw_basic(you,enemy):
    clean()
    draw_top_part(you,enemy)
    draw_enemy(enemy)
    draw_you(you)

### draw battle 

def draw_top_part(you,enemy):
    ##display hud batalha
    print (f"{"="*100}\n{' '*35}MODO DE BATALHA !!!!!\n{' '*40}{you.trainer} vs {enemy.trainer}\n{' '*40}Round :1\n{"="*100}")

def draw_enemy(enemy):
##     player enemy
    count_play1 = life_bar(enemy)
    not_count1 = 10-count_play1
    pokebolas_enemy = len(enemy.pokemons)
    draw_enem_text =[
         (f"Player: {enemy.trainer}"),
        (f"{enemy.pk_on}"+" ("+f"{pk.pokemons[enemy.pk_on].race._race}  {pnt.amarelo("Lv.")} {enemy.pk_lvl}"")"),
        (  pnt.amarelo("HP")  + "["+ pnt.verde("#"*count_play1) + "-"*not_count1+"]"),
        (f"     {enemy.total_life[enemy.pk_on]}"+"/"+f"{pk.pokemons[enemy.pk_on].max_hp}"),
        (f"{pnt.branco("▀ "*pokebolas_enemy)}{"- "*(6-pokebolas_enemy)}")
    ]
    sw.draw_poke_enemy(pk.pokemons[enemy.pk_on].race._race,draw_enem_text,(f"{enemy.pk_lvl}"),len(pk.pokemons[enemy.pk_on].race._race))

def draw_you(you):
## player you
    pokebolas_you = len(you.pokemons)
    count_play2 = life_bar(you)
    not_count2 = 10-count_play2


    draw_you_text = [
        (f"{you.pk_on}"+" ("+f"{pk.pokemons[you.pk_on].race._race}  {pnt.amarelo("Lv.")} {you.pk_lvl}"")"),
        (pnt.amarelo("HP")  + "["+ pnt.verde("#"*count_play2)+"-"*not_count2+"]"),
        (f"     {you.total_life[you.pk_on]}"+"/"+f"{pk.pokemons[you.pk_on].max_hp}"),
        (f"{pnt.branco("▀ "*pokebolas_you)}{"- "*(6-pokebolas_you)}")
    ]
    sw.draw_poke_you(pk.pokemons[you.pk_on].race._race,draw_you_text)

## draw lower part (options)

def draw_basic_lower(you):
    print (f"{"="*100}\n{' '*35}\nWhat will {" "*15} 1)Ataque{' '*20}2)Bag\n{you.pk_on} do?{" "*(22-len(you.pk_on))}3)Pokemons{' '*18}4)fugir\n\n{"="*100}")
    action = input("ACTION: ")

    return action

## draw lower part (moves)

def draw_attack_lower(you,enemy):
    draw_basic(you,enemy)
    while len(you.attacks_display) < 4:
        you.attacks_display.append("Empty")

    print (f"{"="*100}\n{' '*35}Player Attacks: {you.trainer}\n\n1){you.attacks_display[0]} PP: {you.attacks_display_PP[0]}/{you.attacks_display_PP_max[0]}{" "*20}2){you.attacks_display[1]} PP: {you.attacks_display_PP[1]}/{you.attacks_display_PP_max[1]}\n3){you.attacks_display[2]} PP: {you.attacks_display_PP[2]}/{you.attacks_display_PP_max[2]}{" "*20}4){you.attacks_display[3]} PP: {you.attacks_display_PP[3]}/{you.attacks_display_PP_max[3]}\n\n{"="*100}\n")

    attack_chosen = input("CHOSE: ")

    return attack_chosen


def draw_bag_lower():
    return 0
def fugir():
    return 0

## pre attack variables ###

def pre_attack(pk,attack_chosen):
    accuracy = mv.moves[pk.attacks_display[attack_chosen]].accuracy
    priority = mv.moves[pk.attacks_display[attack_chosen]].priority
    if rm.randint(1,100) > accuracy:
        acertou = False
    else:
        acertou = True
    return acertou,priority

## calc the attack of the attack

def calc_attack(pk,attack_chosen,enemy):
    multi_hit = mv.moves[pk.attacks_display[attack_chosen]].multi_hit
    recoil = mv.moves[pk.attacks_display[attack_chosen]].recoil
    if pk.attacks_display_PP[attack_chosen] > 0:
        pk.attacks_display_PP[attack_chosen] -= 1
        attack_you_type = mv.moves[pk.attacks_display[attack_chosen]].element.element_name
        super_effect_you = 1
        for i in enemy.pk_weakness:
            if attack_you_type in i:
                super_effect_you = super_effect_you*2
            else:
                for i in enemy.pk_super_effective:
                    if attack_you_type in i:
                        super_effect_you = super_effect_you/2
        if mv.moves[pk.attacks_display[attack_chosen]].category == "Physical":
            damage = (((((2*pk.pk_lvl)//5+2)*mv.moves[pk.attacks_display[attack_chosen]].power*pk.ATTK)//pk.DFS)//50+2)*super_effect_you
        elif mv.moves[pk.attacks_display[attack_chosen]].category == "Special":
            damage = (((((2*pk.pk_lvl)//5+2)*mv.moves[pk.attacks_display[attack_chosen]].power*pk.SP_ATTK)//pk.SP_DEF)//50+2)*super_effect_you
        else:
            damage = 1
    if recoil == 1:
        damage_recoil = damage//4
    else:
        damage_recoil = 0
    return damage,super_effect_you,multi_hit,damage_recoil

## verify some paramether such as super effective moves##
## draw basic stuff##

def aplication(pk,you,enemy,attack_chosen,damage,super_ef):
    draw_basic(you,enemy)
    mensage (f"{pk.pk_on} used\n {pk.attacks_display[attack_chosen]} {damage}!")
    draw_basic(you,enemy)
    if super_ef > 1 :
        mensage("Its super effective!")
    elif super_ef <1:
        mensage("Its not very effective...")
    clean()

## print a lower mensage in the screen (it draw itself)

def default_mensage(you,enemy,text):
    draw_basic(you,enemy)
    mensage(text)

##calc life bar 

def life_bar(trainer):

    count = 10
    sub = trainer.total_life[trainer.pk_on]*10//pk.pokemons[trainer.pk_on].max_hp
    not_count = count - sub
    count = count - not_count

    return int (count)

##obj of the player --- it has all the variables needed for the player

class Battler:
    def __init__(self,name):
        ### your setup ####

        self.trainer = name

        self.pk_on = tr.trainers[self.trainer].party[0].name
        self.total_life = {}
        self.setup()
        self.format_attacks()
        self.format_pokemons()

    def setup(self):

        self.pk_type = [i.element_name for i in pk.pokemons[self.pk_on].race._element]
        self.pk_weakness = [el.elements[i].weakness for i in  self.pk_type]
        self.pk_super_effective = [el.elements[i].super_effective for i in  self.pk_type]

        self.pk_lvl = pk.pokemons[self.pk_on].lvl ###ENEMY LEVEL

        self.DFS = pk.pokemons[self.pk_on].DFS
        self.ATTK = pk.pokemons[self.pk_on].ATTK
        self.SPPD = pk.pokemons[self.pk_on].SPPD
        self.SP_ATTK = pk.pokemons[self.pk_on].SP_ATTK
        self.SP_DEF = pk.pokemons[self.pk_on].SP_DEF
        self.attacks_display = []
        self.attacks_display_PP = []
        self.attacks_display_PP_max = []
        self.pokemons = []


    def format_attacks(self):
         #####formatacao dos ataques#####
        for i in pk.pokemons[self.pk_on].attaks:
            for move in i:
                self.attacks_display.append(move)
        PP_id = []
        for i in pk.pokemons[self.pk_on].attaks_pp:
            PPSd = ([j for j in i.values()])
            for index in PPSd:
                PP_id.append(index)

        for i in self.attacks_display:
            self.attacks_display_PP.append(mv.moves[i].PP) 
            self.attacks_display_PP_max.append(mv.moves[i].PP) 
        while len(self.attacks_display_PP) < 4 :
            self.attacks_display_PP.append(0)
            self.attacks_display_PP_max.append(0)
    
    def format_pokemons(self):
        ### lista com os nomes do pokemon #

        for i in tr.trainers[self.trainer].party:
            self.pokemons.append(i.name)
        
        for i in self.pokemons:
            self.total_life[i] = pk.pokemons[i].max_hp

####start######

def battle(you_inp,enemy_inp):
    clean()

    you = Battler(you_inp)
    enemy =Battler(enemy_inp)


##### inicio do loop

    while True :

        you_lose = check_death(you)
        enemy_lose = check_death(enemy)

        if you_lose == True:
            mensage("You lost")
            break
        if enemy_lose == True:
            mensage("You won")
            break
            

            
          
    ## desenha na tela as info basicas ##

        draw_top_part(you,enemy)
        draw_enemy(enemy)
        draw_you(you)


##interative part

        step_1 = draw_basic_lower(you)

        match step_1:
            case "1":
                attack_chosen = draw_attack_lower(you,enemy)
                match attack_chosen:

                    #### escolheu um ataque ###

                    case "1" | "2" | "3" | "4":
                        attack_chosen = int(attack_chosen)-1
                            ### enemy chose attack for now will be "random"
                        enemy_attack_chosen = rm.randint(0,(len(enemy.attacks_display)-1))
                        you_acertou,you_priority = pre_attack(you,attack_chosen)
                        enemy_acertou,enemy_priority = pre_attack(enemy,enemy_attack_chosen)


                        if you.SPPD > enemy.SPPD and you_priority > enemy_priority:
                            if you_acertou:
                                damage_your,super_effect_you,multi_hit_you,recoil_you = calc_attack(you,attack_chosen,enemy)
                                enemy.total_life[enemy.pk_on] -= damage_your
                                you.total_life[you.pk_on] -= recoil_you
                                if enemy.total_life[enemy.pk_on] < 0:
                                    enemy.total_life[enemy.pk_on] = 0
                                    aplication(you,you,enemy,attack_chosen,damage_your,super_effect_you)
                                else:
                                    aplication(you,you,enemy,attack_chosen,damage_your,super_effect_you)
                                    if enemy_acertou:
                                        damage_enemy,super_effect_enemy,multi_hit_enemy,recoil_enemy = calc_attack(enemy,enemy_attack_chosen,you)
                                        you.total_life[you.pk_on] -= damage_enemy
                                        enemy.total_life[enemy.pk_on] -= recoil_enemy
                                        if you.total_life[you.pk_on] < 0:
                                            you.total_life[you.pk_on] = 0
                                            aplication(enemy,you,enemy,enemy_attack_chosen,damage_enemy,super_effect_enemy)
                                        else:
                                            aplication(enemy,you,enemy,enemy_attack_chosen,damage_enemy,super_effect_enemy)
                                    else:
                                        default_mensage(you,enemy,"Enemy missed")
                            else:
                                default_mensage(you,enemy,"You missed")
                                aplication(you,you,enemy,attack_chosen,damage_your,super_effect_you)
                                if enemy_acertou:
                                    damage_enemy,super_effect_enemy,multi_hit_enemy,recoil_enemy = calc_attack(enemy,enemy_attack_chosen,you)
                                    you.total_life[you.pk_on] -= damage_enemy
                                    enemy.total_life[enemy.pk_on] -= recoil_enemy
                                    if you.total_life[you.pk_on] < 0:
                                        you.total_life[you.pk_on] = 0
                                        aplication(enemy,you,enemy,enemy_attack_chosen,damage_enemy,super_effect_enemy)
                                    else:
                                        aplication(enemy,you,enemy,enemy_attack_chosen,damage_enemy,super_effect_enemy)
                                else:
                                    default_mensage(you,enemy,"Enemy missed")
                            
                        else:
                            if enemy_acertou:
                                damage_enemy,super_effect_enemy,multi_hit_enemy,recoil_enemy = calc_attack(enemy,enemy_attack_chosen,you)
                                you.total_life[you.pk_on] -= damage_enemy
                                enemy.total_life[enemy.pk_on] -= recoil_enemy
                                if you.total_life[you.pk_on] < 0:
                                    you.total_life[you.pk_on] = 0
                                    aplication(enemy,you,enemy,enemy_attack_chosen,damage_enemy,super_effect_enemy)
                                else:
                                    aplication(enemy,you,enemy,enemy_attack_chosen,damage_enemy,super_effect_enemy)
                                    if you_acertou:
                                        damage_your,super_effect_you,multi_hit_you,recoil_you = calc_attack(you,attack_chosen,enemy)
                                        enemy.total_life[enemy.pk_on] -= damage_your
                                        aplication(you,you,enemy,attack_chosen,damage_your,super_effect_you)
                                        you.total_life[you.pk_on] -= recoil_you
                                        if enemy.total_life[enemy.pk_on] < 0:
                                            enemy.total_life[enemy.pk_on] = 0
                                            aplication(you,you,enemy,attack_chosen,damage_your,super_effect_you)
                                    else:
                                        default_mensage(you,enemy,"You missed")
                            else:
                                default_mensage(you,enemy,"Enemy missed")
                                aplication(you,you,enemy,attack_chosen,damage_your,super_effect_you)
                                if you_acertou:
                                    damage_your,super_effect_you,multi_hit_you,recoil_you = calc_attack(you,attack_chosen,enemy)
                                    enemy.total_life[enemy.pk_on] -= damage_your
                                    you.total_life[you.pk_on] -= recoil_you
                                    if enemy.total_life[enemy.pk_on] < 0:
                                        enemy.total_life[enemy.pk_on] = 0
                                        aplication(you,you,enemy,attack_chosen,damage_your,super_effect_you)
                                else:
                                    default_mensage(you,enemy,"You missed")
                                
                    case _: 
                        clean()
                        continue
 
            case "2":
                draw_attack_lower
            case "3":
                draw_attack_lower
            case "4":
                print ("Covarde!!")
                ok = input("ok")
                return 0
            case _:
                clean()
                continue
    return 0
battle("Teste1","Teste2")
## debug for tests ##