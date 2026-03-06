import pokemon as pk
import trainer as tr
import race as rc
import move as mv
import format_input as form
import os
os.system('cls' if os.name == 'nt' else 'clear')

name1 = str("Alfaro")
name2 = str("Thuol")
Round = 1

total_life = {name1:tr.trainers[name1].party[0].max_hp,
              name2:tr.trainers[name2].party[0].max_hp}

##calc life bar 

def life_bar(name):

    count = 10
    sub = total_life[name]*10//tr.trainers[name].party[0].max_hp
    not_count = count - sub
    count = count - not_count

    return int (count)


while True :

##display hud batalha


    print (f"{"="*100}\n{' '*35}MODO DE BATALHA !!!!!\n{' '*40}{name1} vs {name2}\n{' '*40}Round :{Round}\n{"="*100}\n")

##     player 1

    count_play1 = life_bar(name1)
    not_count1 = 10-count_play1

    print (" "*75+f"Player: {name1}\n")
    print (" "*75+f"{tr.trainers[name1].party[0].name}"+" ("+f"{tr.trainers[name1].party[0].race._race}"")")
    print (" "*75+"HP["+ "#"*count_play1+"-"*not_count1+"]")
    print (" "*75+f"     {total_life[name1]}"+"/"+f"{tr.trainers[name1].party[0].max_hp}\n\n")

## player 2

    count_play2 = life_bar(name2)
    not_count2 = 10-count_play2

    print (f"{tr.trainers[name2].party[0].name}"+" ("+f"{tr.trainers[name2].party[0].race._race}"")")
    print ("HP["+ "#"*count_play2+"-"*not_count2+"]")
    print (f"     {total_life[name2]}"+"/"+f"{tr.trainers[name2].party[0].max_hp}\n")

    print (f"{"="*100}\n{' '*35}Player: {name2}\n\n1)Ataque{' '*20}2)Bag\n3)Pokemons{' '*18}4)fugir\n\n{"="*100}\n")



    total_life[name1] -= 1
    i = input("")
    Round += 1
    os.system('cls' if os.name == 'nt' else 'clear')