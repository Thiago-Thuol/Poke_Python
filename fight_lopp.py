import pokemon as pk
import trainer as tr
import race as rc
import move as mv
import format_input as form
import os

### draw battle 

def draw_top_part(enemy,you,Round):
    ##display hud batalha

    print (f"{"="*100}\n{' '*35}MODO DE BATALHA !!!!!\n{' '*40}{you} vs {enemy}\n{' '*40}Round :{Round}\n{"="*100}\n")

def draw_p1(enemy,total_life,your_pk_lvl,enemypk):
##     player 1

    count_play1 = life_bar(enemypk,total_life)
    not_count1 = 10-count_play1

    print (" "*75+f"Player: {enemy}\n")
    print (" "*75+f"{enemypk}"+" ("+f"{pk.pokemons[enemypk].race._race}  Lv. {your_pk_lvl}"")")
    print (" "*75+"HP["+ "#"*count_play1+"-"*not_count1+"]")
    print (" "*75+f"     {total_life[enemypk]}"+"/"+f"{pk.pokemons[enemypk].max_hp}\n\n")


def draw_p2(you,total_life,your_pk_lv,yourpk):
## player 2

    count_play2 = life_bar(yourpk,total_life)
    not_count2 = 10-count_play2

    print (f"{yourpk}"+" ("+f"{pk.pokemons[yourpk].race._race}  Lv. {your_pk_lv}"")")
    print ("HP["+ "#"*count_play2+"-"*not_count2+"]")
    print (f"     {total_life[yourpk]}"+"/"+f"{pk.pokemons[yourpk].max_hp}\n")







## draw lowe part none

def draw_basic_lower(you):
    print (f"{"="*100}\n{' '*35}Player: {you}\n\n1)Ataque{' '*20}2)Bag\n3)Pokemons{' '*18}4)fugir\n\n{"="*100}\n")
    action = input("ACTION: ")

    return action


def draw_attack_lower(enemypk,yourpk,your_pk_lvl,enemy_pk_lv,total_life,enemy,you,Round,attacks_display,attacks_display_PP=0):

    os.system('cls' if os.name == 'nt' else 'clear')
   
    draw_top_part(enemy,you,Round)

    draw_p1(enemy,total_life,your_pk_lvl,enemypk)

    draw_p2(you,total_life,enemy_pk_lv,yourpk)

    while len(attacks_display) < 4:
        attacks_display.append("Empty")

    print (f"{"="*100}\n{' '*35}Player Attacks: {you}\n\n1){attacks_display[0]} PP: {attacks_display_PP[0]}{" "*20}2){attacks_display[1]} PP: {attacks_display_PP[1]}\n3){attacks_display[2]} PP: {attacks_display_PP[2]}{" "*20}4){attacks_display[3]} PP: {attacks_display_PP[3]}\n\n{"="*100}\n")

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

def battle(nome1_inp,nomme2_inp):
    os.system('cls' if os.name == 'nt' else 'clear')

    enemy = nome1_inp  ##ENEMY
    you = nomme2_inp ##YOU

    yourpk = tr.trainers[nome1_inp].party[0].name  ###ENEMY POK
    enemypk = tr.trainers[nomme2_inp].party[0].name ###YOUR POK

    your_pk_lvl = pk.pokemons[yourpk].lvl ### YOUR LEVEL
    enemy_pk_lv = pk.pokemons[enemypk].lvl ###ENEMY LEVEL

    enemy_defense = pk.pokemons[enemypk].DFS  ## ENEMY DEFENSE
    enemy_SPdefense = pk.pokemons[enemypk].SP_DEF  ## ENEMY SPDEFENS
    your_ATTK = pk.pokemons[yourpk].ATTK          ##YOUR ATACK
    yout_SPATTK = pk.pokemons[yourpk].SP_ATTK     ##YOUR SPATTACK

    total_life = {yourpk:pk.pokemons[yourpk].max_hp,
              enemypk:pk.pokemons[enemypk].max_hp}

    Round = 1

    attacks_display = [i for i in pk.pokemons[yourpk].attaks.keys()]

    attacks_display_PP = []

    for i in attacks_display:
        attacks_display_PP.append(mv.moves[i].PP) 
    while len(attacks_display_PP) < 4 :
        attacks_display_PP.append(0)



    while True :

        draw_top_part(enemy,you,Round)

        draw_p1(enemy,total_life,your_pk_lvl,enemypk)

        draw_p2(you,total_life,enemy_pk_lv,yourpk)


##interative part

        step_1 = draw_basic_lower(you)

        match step_1:
            case "1":
                attack_chosen = draw_attack_lower(enemypk,yourpk,your_pk_lvl,enemy_pk_lv,total_life,enemy,you,Round, attacks_display,attacks_display_PP)
                match attack_chosen:
                    case "1":
                        if mv.moves[attacks_display[0]].category == "Physical":
                            damage = (((((2*your_pk_lvl)//5+2)*mv.moves[attacks_display[0]].power*your_ATTK)//enemy_defense)//50+2)
                        elif mv.moves[attacks_display[0]].category == "Special":
                            damage = (((((2*your_pk_lvl)//5+2)*mv.moves[attacks_display[0]].power*yout_SPATTK)//enemy_SPdefense)/50+2)
                        else:
                            return 0
                    case "2":
                        if mv.moves[attacks_display[1]].category == "Physical":
                            damage = (((((2*your_pk_lvl)//5+2)*mv.moves[attacks_display[1]].power*your_ATTK)//enemy_defense)/50+2)
                        elif mv.moves[attacks_display[1]].category == "Special":
                            damage = (((((2*your_pk_lvl)//5+2)*mv.moves[attacks_display[1]].power*yout_SPATTK)//enemy_SPdefense)/50+2)
                        else:
                            return 0
                    case "3":
                        if mv.moves[attacks_display[2]].category == "Physical":
                            damage = (((((2*your_pk_lvl)//5+2)*mv.moves[attacks_display[2]].power*your_ATTK)//enemy_defense)/50+2)
                        elif mv.moves[attacks_display[2]].category == "Special":
                            damage = (((((2*your_pk_lvl)//5+2)*mv.moves[attacks_display[2]].power*yout_SPATTK)//enemy_SPdefense)/50+2)
                        else:
                            return 0
                    case "4":
                        if mv.moves[attacks_display[3]].category == "Physical":
                            damage = (((((2*your_pk_lvl)//5+2)*mv.moves[attacks_display[3]].power*your_ATTK)//enemy_defense)/50+2)
                        elif mv.moves[attacks_display[3]].category == "Special":
                            damage = (((((2*your_pk_lvl)//5+2)*mv.moves[attacks_display[3]].power*yout_SPATTK)//enemy_SPdefense)/50+2)
                        else:
                            return 0
                    case _: 
                        return 0
 
            case "2":
                draw_attack_lower
            case "3":
                draw_attack_lower
            case "4":
                draw_attack_lower
            case _:
                return 0


        total_life[enemypk] -= damage
        Round += 1
        os.system('cls' if os.name == 'nt' else 'clear')
        print (damage)