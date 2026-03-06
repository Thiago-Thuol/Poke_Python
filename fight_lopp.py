import pokemon as pk
import trainer as tr
import race as rc
import move as mv
import format_input as form
import os
os.system('cls' if os.name == 'nt' else 'clear')

name1 = str("Alfaro")
total_life = {name1:tr.trainers["Alfaro"].party[0].max_hp}

##calc life bar 

def life_bar(name):

    count = 10
    sub = total_life[name]*10//tr.trainers["Alfaro"].party[0].max_hp
    not_count = count - sub
    count = count - not_count

    return int (count)

    
    not_count = 10-count




while True :




    count_play1 = life_bar(name1)
    not_count1 = 10-count_play1

    print (" "*100+f"{tr.trainers[name1].party[0].name}"+"("+f"{tr.trainers[name1].party[0].race._race}"")")
    print (" "*100+"HP["+ "#"*count_play1+"-"*not_count1+"]")
    print (" "*100+f"{total_life[name1]}"+"/"+f"{tr.trainers[name1].party[0].max_hp}\n\n")


    total_life[name1] -= 1
    i = input("")
    os.system('cls' if os.name == 'nt' else 'clear')