import pokemon as pk
import trainer as tr
import race as rc
import move as mv
import format_input as form
import os

### draw battle 

def draw_top_part(name1,name2,Round):
    ##display hud batalha


    print (f"{"="*100}\n{' '*35}MODO DE BATALHA !!!!!\n{' '*40}{name1} vs {name2}\n{' '*40}Round :{Round}\n{"="*100}\n")

def draw_p1(name1,total_life):
##     player 1

    count_play1 = life_bar(name1,total_life)
    not_count1 = 10-count_play1

    print (" "*75+f"Player: {name1}\n")
    print (" "*75+f"{tr.trainers[name1].party[0].name}"+" ("+f"{tr.trainers[name1].party[0].race._race}"")")
    print (" "*75+"HP["+ "#"*count_play1+"-"*not_count1+"]")
    print (" "*75+f"     {total_life[name1]}"+"/"+f"{tr.trainers[name1].party[0].max_hp}\n\n")


def draw_p2(name2,total_life):
## player 2

    count_play2 = life_bar(name2,total_life)
    not_count2 = 10-count_play2

    print (f"{tr.trainers[name2].party[0].name}"+" ("+f"{tr.trainers[name2].party[0].race._race}"")")
    print ("HP["+ "#"*count_play2+"-"*not_count2+"]")
    print (f"     {total_life[name2]}"+"/"+f"{tr.trainers[name2].party[0].max_hp}\n")







## draw lowe part none

def draw_basic_lower(name2):
    print (f"{"="*100}\n{' '*35}Player: {name2}\n\n1)Ataque{' '*20}2)Bag\n3)Pokemons{' '*18}4)fugir\n\n{"="*100}\n")
    action = input("ACTION: ")

    return action


def draw_attack_lower(total_life,name1,name2,Round,attacks_display,attacks_display_PP=0):

    os.system('cls' if os.name == 'nt' else 'clear')
   
    draw_top_part(name1,name2,Round)

    draw_p1(name1,total_life)

    draw_p2(name2,total_life)

    while len(attacks_display) < 4:
        attacks_display.append("Empty")

    print (f"{"="*100}\n{' '*35}Player Attacks: {name2}\n\n1){attacks_display[0]} PP: {attacks_display_PP[0]}{" "*20}2){attacks_display[1]} PP: {attacks_display_PP[1]}\n3){attacks_display[2]} PP: {attacks_display_PP[2]}{" "*20}4){attacks_display[3]} PP: {attacks_display_PP[3]}\n\n{"="*100}\n")

    cin = input("")





def draw_pokemons_lower():
    return 0
def draw_bag_lower():
    return 0
def fugir():
    return 0




##calc life bar 

def life_bar(name,total_life):

    count = 10
    sub = total_life[name]*10//tr.trainers[name].party[0].max_hp
    not_count = count - sub
    count = count - not_count

    return int (count)

##start######

def battle(nome1_inp,nomme2_inp):
    os.system('cls' if os.name == 'nt' else 'clear')


    name1 = nome1_inp
    name2 = nomme2_inp

    total_life = {name1:tr.trainers[name1].party[0].max_hp,
              name2:tr.trainers[name2].party[0].max_hp}

    Round = 1

    attacks_display = [i for i in pk.pokemons[name2].attaks.keys()]

    attacks_display_PP = []

    for i in attacks_display:
        attacks_display_PP.append(mv.moves[i].PP) 



    while True :

        draw_top_part(name1,name2,Round)

        draw_p1(name1,total_life)

        draw_p2(name2,total_life)


##interative part

        step_1 = draw_basic_lower(name2)

        match step_1:
            case "1":
                draw_attack_lower(total_life,name1,name2,Round, attacks_display,attacks_display_PP)
            case "2":
                draw_attack_lower
            case "3":
                draw_attack_lower
            case "4":
                draw_attack_lower
            case _:
                return 0


        total_life[name1] -= 1
        Round += 1
        os.system('cls' if os.name == 'nt' else 'clear')
battle("Alfaro","Thuol")