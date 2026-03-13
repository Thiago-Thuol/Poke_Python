import pokemon as pk
import trainer as tr
import race as rc
import move as mv
import format_input as form
import os
import paint as pnt
import show_poke as sw

def clean():
    os.system('cls' if os.name == 'nt' else 'clear')

### draw battle 

def draw_top_part(enemy,you,Round):
    ##display hud batalha

    print (f"{"="*100}\n{' '*35}MODO DE BATALHA !!!!!\n{' '*40}{you} vs {enemy}\n{' '*40}Round :{Round}\n{"="*100}")

def draw_enemy(enemy,total_life,enemypk,enemy_pk_lv):
##     player enemy
    count_play1 = life_bar(enemypk,total_life)
    not_count1 = 10-count_play1

    draw_enem_text =[
         (f"Player: {enemy}"),
        (f"{enemypk}"+" ("+f"{pk.pokemons[enemypk].race._race}  {pnt.amarelo("Lv.")} {enemy_pk_lv}"")"),
        (  pnt.amarelo("HP")  + "["+ pnt.verde("#"*count_play1) + "-"*not_count1+"]"),
        (f"     {total_life[enemypk]}"+"/"+f"{pk.pokemons[enemypk].max_hp}")
    ]
    sw.draw_poke_enemy(pk.pokemons[enemypk].race._race,draw_enem_text,(f"{enemy_pk_lv}"),len(pk.pokemons[enemypk].race._race))

def draw_you(you,total_life,your_pk_lvl,yourpk):
## player you

    count_play2 = life_bar(yourpk,total_life)
    not_count2 = 10-count_play2

    draw_you_text = [
        (f"{yourpk}"+" ("+f"{pk.pokemons[yourpk].race._race}  {pnt.amarelo("Lv.")} {your_pk_lvl}"")"),
        (pnt.amarelo("HP")  + "["+ pnt.verde("#"*count_play2)+"-"*not_count2+"]"),
        (f"     {total_life[yourpk]}"+"/"+f"{pk.pokemons[yourpk].max_hp}")
    ]
    sw.draw_poke_you(pk.pokemons[yourpk].race._race,draw_you_text)






## draw lowe part none

def draw_basic_lower(yourpk):
    print (f"{"="*100}\n{' '*35}\nWhat will {" "*15} 1)Ataque{' '*20}2)Bag\n{yourpk} do?{" "*(22-len(yourpk))}3)Pokemons{' '*18}4)fugir\n\n{"="*100}")
    action = input("ACTION: ")

    return action


def draw_attack_lower(enemypk,yourpk,your_pk_lvl,enemy_pk_lv,total_life,enemy,you,Round,attacks_display,attacks_display_PP=0,attacks_display_PP_max=0):

    clean()
   
    draw_top_part(enemy,you,Round)

    draw_enemy(enemy,total_life,enemypk,enemy_pk_lv)

    draw_you(you,total_life,your_pk_lvl,yourpk)

    while len(attacks_display) < 4:
        attacks_display.append("Empty")

    print (f"{"="*100}\n{' '*35}Player Attacks: {you}\n\n1){attacks_display[0]} PP: {attacks_display_PP[0]}/{attacks_display_PP_max[0]}{" "*20}2){attacks_display[1]} PP: {attacks_display_PP[1]}/{attacks_display_PP_max[1]}\n3){attacks_display[2]} PP: {attacks_display_PP[2]}/{attacks_display_PP_max[2]}{" "*20}4){attacks_display[3]} PP: {attacks_display_PP[3]}/{attacks_display_PP_max[3]}\n\n{"="*100}\n")

    attack_chosen = input("CHOSE: ")

    return attack_chosen





def draw_pokemons_lower():
    return 0
def draw_bag_lower():
    return 0
def fugir():
    return 0




##calc life bar 

def life_bar(name,total_life):

    count = 10
    sub = total_life[name]*10//pk.pokemons[name].max_hp
    not_count = count - sub
    count = count - not_count

    return int (count)

##start######

def battle(you_inp,enemy_inp):
    clean()

    enemy = enemy_inp  ##ENEMY
    you = you_inp ##YOU

    yourpk = tr.trainers[you_inp].party[0].name  ###ENEMY POK
    enemypk = tr.trainers[enemy_inp].party[0].name ###YOUR POK

    your_pk_lvl = pk.pokemons[yourpk].lvl ### YOUR LEVEL
    enemy_pk_lv = pk.pokemons[enemypk].lvl ###ENEMY LEVEL

    enemy_defense = pk.pokemons[enemypk].DFS  ## ENEMY DEFENSE
    enemy_SPdefense = pk.pokemons[enemypk].SP_DEF  ## ENEMY SPDEFENS
    your_ATTK = pk.pokemons[yourpk].ATTK          ##YOUR ATACK
    yout_SPATTK = pk.pokemons[yourpk].SP_ATTK     ##YOUR SPATTACK

    total_life = {yourpk:pk.pokemons[yourpk].max_hp,
              enemypk:pk.pokemons[enemypk].max_hp}

    Round = 1 ##RODADA

    attacks_display = [] 

     #####formatacao dos ataques#####

    for i in pk.pokemons[yourpk].attaks:
        name = ([j for j in i])
        for index in name:
            attacks_display.append(index)
    PP_id = []
    for i in pk.pokemons[yourpk].attaks_pp:
        PPSd = ([j for j in i.values()])
        for index in PPSd:
            PP_id.append(index)

    attacks_display_PP = []
    attacks_display_PP_max = []

    for i in attacks_display:
        attacks_display_PP.append(mv.moves[i].PP) 
        attacks_display_PP_max.append(mv.moves[i].PP) 
    while len(attacks_display_PP) < 4 :
        attacks_display_PP.append(0)
        attacks_display_PP_max.append(0)

##### inicio do loop

    while True :

        draw_top_part(enemy,you,Round)
        draw_enemy(enemy,total_life,enemypk,enemy_pk_lv)

        draw_you(you,total_life,your_pk_lvl,yourpk)


##interative part

        step_1 = draw_basic_lower(yourpk)

        match step_1:
            case "1":
                attack_chosen = draw_attack_lower(enemypk,yourpk,your_pk_lvl,enemy_pk_lv,total_life,enemy,you,Round, attacks_display,attacks_display_PP,attacks_display_PP_max)
                match attack_chosen:

                    #### escolheu um ataque ###

                    case "1" | "2" | "3" | "4":
                        attack_chosen = int(attack_chosen)-1
                        if attacks_display_PP[attack_chosen] > 0:
                            attacks_display_PP[attack_chosen] -= 1
                            if mv.moves[attacks_display[attack_chosen]].category == "Physical":
                                damage = (((((2*your_pk_lvl)//5+2)*mv.moves[attacks_display[attack_chosen]].power*your_ATTK)//enemy_defense)//50+2)
                            elif mv.moves[attacks_display[attack_chosen]].category == "Special":
                                damage = (((((2*your_pk_lvl)//5+2)*mv.moves[attacks_display[attack_chosen]].power*yout_SPATTK)//enemy_SPdefense)/50+2)
                            else:
                                damage = 1
                        else:
                            print ("Sem PP")
                            ok = input("ok")
                            clean()
                            continue
                    case _: 
                        clean()
                        continue
 
            case "2":
                draw_attack_lower
            case "3":
                draw_attack_lower
            case "4":
                draw_attack_lower
            case _:
                clean()
                continue


        total_life[enemypk] -= damage
        Round += 1
        clean()
        print (damage)
battle("Thuol","Alfaro")