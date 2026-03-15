import pokemon as pk
import trainer as tr
import race as rc
import move as mv
import format_input as form
import os
import paint as pnt
import show_poke as sw
import random as rm

def clean():
    os.system('cls' if os.name == 'nt' else 'clear')

### draw battle 

def draw_top_part():
    ##display hud batalha

    print (f"{"="*100}\n{' '*35}MODO DE BATALHA !!!!!\n{' '*40}{you} vs {enemy}\n{' '*40}Round :{Round}\n{"="*100}")

def draw_enemy():
##     player enemy
    count_play1 = life_bar(enemypk_name)
    not_count1 = 10-count_play1
    pokebolas_enemy = len(pokemon_enemy)
    draw_enem_text =[
         (f"Player: {enemy}"),
        (f"{enemypk_name}"+" ("+f"{pk.pokemons[enemypk_name].race._race}  {pnt.amarelo("Lv.")} {enemy_pk_lvl}"")"),
        (  pnt.amarelo("HP")  + "["+ pnt.verde("#"*count_play1) + "-"*not_count1+"]"),
        (f"     {total_life_enemy[enemypk_name]}"+"/"+f"{pk.pokemons[enemypk_name].max_hp}"),
        (f"{pnt.branco("▀ "*pokebolas_enemy)}{"- "*(6-pokebolas_enemy)}")
    ]
    sw.draw_poke_enemy(pk.pokemons[enemypk_name].race._race,draw_enem_text,(f"{enemy_pk_lvl}"),len(pk.pokemons[enemypk_name].race._race))

def draw_you():
## player you
    pokebolas_you = len(pokemons_you)
    count_play2 = life_bar(yourpk_name)
    not_count2 = 10-count_play2


    draw_you_text = [
        (f"{yourpk_name}"+" ("+f"{pk.pokemons[yourpk_name].race._race}  {pnt.amarelo("Lv.")} {your_pk_lvl}"")"),
        (pnt.amarelo("HP")  + "["+ pnt.verde("#"*count_play2)+"-"*not_count2+"]"),
        (f"     {total_life_you[yourpk_name]}"+"/"+f"{pk.pokemons[yourpk_name].max_hp}"),
        (f"{pnt.branco("▀ "*pokebolas_you)}{"- "*(6-pokebolas_you)}")
    ]
    sw.draw_poke_you(pk.pokemons[yourpk_name].race._race,draw_you_text)

## draw lowe part none

def draw_basic_lower():
    print (f"{"="*100}\n{' '*35}\nWhat will {" "*15} 1)Ataque{' '*20}2)Bag\n{yourpk_name} do?{" "*(22-len(yourpk_name))}3)Pokemons{' '*18}4)fugir\n\n{"="*100}")
    action = input("ACTION: ")

    return action

def draw_attack_lower():

    clean()
   
    draw_top_part()

    draw_enemy()

    draw_you()

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

def life_bar(name):

    count = 10
    try:
        sub = total_life_you[name]*10//pk.pokemons[name].max_hp
    except:
        sub = total_life_enemy[name]*10//pk.pokemons[name].max_hp
    not_count = count - sub
    count = count - not_count

    return int (count)

##start######

def battle(you_inp,enemy_inp):
    clean()
    global Round
    global enemy
    global enemypk_name
    global enemy_pk_lvl
    global total_life_enemy
    global enemy_ATTK
    global enemy_DFS
    global enemy_SPPD
    global enemy_SP_ATTK
    global enemy_SP_DEF
    global you
    global yourpk_name
    global your_pk_lvl
    global total_life_you
    global your_ATTK
    global your_DFS
    global your_SPPD
    global your_SP_ATTK
    global your_SP_DEF
    global attacks_display
    global PP_id
    global attacks_display_PP
    global attacks_display_PP_max

### your setup ####

    you = you_inp

    yourpk_name = tr.trainers[you].party[0].name

    your_pk_lvl = pk.pokemons[yourpk_name].lvl ###ENEMY LEVEL

    your_DFS = pk.pokemons[yourpk_name].DFS
    your_DFS = pk.pokemons[yourpk_name].DFS
    your_ATTK = pk.pokemons[yourpk_name].ATTK
    your_SPPD = pk.pokemons[yourpk_name].SPPD
    your_SP_ATTK = pk.pokemons[yourpk_name].SP_ATTK
    your_SP_DEF = pk.pokemons[yourpk_name].SP_DEF

    attacks_display = [] 

     #####formatacao dos ataques#####

    for i in pk.pokemons[yourpk_name].attaks:
        name = ([j for j in i])
        for index in name:
            attacks_display.append(index)
    PP_id = []
    for i in pk.pokemons[yourpk_name].attaks_pp:
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

#### enemy setup ###
    enemy = enemy_inp

    enemypk_name = tr.trainers[enemy].party[0].name

    enemy_pk_lvl = pk.pokemons[enemypk_name].lvl ###ENEMY LEVEL

    enemy_DFS = pk.pokemons[enemypk_name].DFS
    enemy_DFS = pk.pokemons[enemypk_name].DFS
    enemy_ATTK = pk.pokemons[enemypk_name].ATTK
    enemy_SPPD = pk.pokemons[enemypk_name].SPPD
    enemy_SP_ATTK = pk.pokemons[enemypk_name].SP_ATTK
    enemy_SP_DEF = pk.pokemons[enemypk_name].SP_DEF

    attacks_display_enemy = [] 

     #####formatacao dos ataques#####

    for i in pk.pokemons[enemypk_name].attaks:
        name = ([j for j in i])
        for index in name:
            attacks_display_enemy.append(index)
    PP_id_enemy = []
    for i in pk.pokemons[enemypk_name].attaks_pp:
        PPSd_enemy = ([j for j in i.values()])
        for index in PPSd_enemy:
            PP_id_enemy.append(index)

    attacks_display_enemy_PP = []
    attacks_display_enemy_PP_max = []


    for i in attacks_display_enemy:
        attacks_display_enemy_PP.append(mv.moves[i].PP) 
        attacks_display_enemy_PP_max.append(mv.moves[i].PP) 
    while len(attacks_display_enemy_PP) < 4 :
        attacks_display_enemy_PP.append(0)
        attacks_display_enemy_PP_max.append(0)

    Round = 1 ##RODADA


### lista com os nomes do pokemon ##
    global pokemons_you
    global pokemon_enemy

    pokemons_you = []

    pokemon_enemy = []

    for i in tr.trainers[you].party:
        pokemons_you.append(i.name)

    for i in tr.trainers[enemy].party:
        pokemon_enemy.append(i.name)

    total_life_enemy = {}

    for i in pokemon_enemy:
          total_life_enemy[i] = pk.pokemons[i].max_hp

    total_life_enemy = {}

    for i in pokemon_enemy:
          total_life_enemy[i] = pk.pokemons[i].max_hp

    total_life_you = {}

    for i in pokemons_you:
        total_life_you[i] = pk.pokemons[i].max_hp
    

##### inicio do loop

    while True :

## chack if enemy is dead##

        if total_life_enemy[enemypk_name] <= 0:
            for i in pokemon_enemy:
                all_dead_enemy = True
                if total_life_enemy[i] >= 0:
                    enemypk_name = i

                    enemy_pk_lvl = pk.pokemons[enemypk_name].lvl ###ENEMY LEVEL
                    enemy_DFS = pk.pokemons[enemypk_name].DFS
                    enemy_DFS = pk.pokemons[enemypk_name].DFS
                    enemy_ATTK = pk.pokemons[enemypk_name].ATTK
                    enemy_SPPD = pk.pokemons[enemypk_name].SPPD
                    enemy_SP_ATTK = pk.pokemons[enemypk_name].SP_ATTK
                    enemy_SP_DEF = pk.pokemons[enemypk_name].SP_DEF


                    attacks_display_enemy = [] 

                    #####formatacao dos ataques#####

                    for i in pk.pokemons[enemypk_name].attaks:
                        name = ([j for j in i])
                        for index in name:
                            attacks_display_enemy.append(index)
                    PP_id_enemy = []
                    for i in pk.pokemons[enemypk_name].attaks_pp:
                        PPSd_enemy = ([j for j in i.values()])
                        for index in PPSd_enemy:
                            PP_id_enemy.append(index)

                    attacks_display_enemy_PP = []
                    attacks_display_enemy_PP_max = []


                    for i in attacks_display_enemy:
                        attacks_display_enemy_PP.append(mv.moves[i].PP) 
                        attacks_display_enemy_PP_max.append(mv.moves[i].PP) 
                    while len(attacks_display_enemy_PP) < 4 :
                        attacks_display_enemy_PP.append(0)
                        attacks_display_enemy_PP_max.append(0)
                    all_dead_enemy = False
            if all_dead_enemy == False:
                continue
            else:
                return 0
            
## check if you are dead###

        if total_life_you[yourpk_name] <= 0:
            for i in pokemons_you:
                all_dead_enemy = True
                if total_life_you[i] > 0:

                    enemypk_name = i

                    your_pk_lvl = pk.pokemons[yourpk_name].lvl ###ENEMY LEVEL

                    your_DFS = pk.pokemons[yourpk_name].DFS
                    your_DFS = pk.pokemons[yourpk_name].DFS
                    your_ATTK = pk.pokemons[yourpk_name].ATTK
                    your_SPPD = pk.pokemons[yourpk_name].SPPD
                    your_SP_ATTK = pk.pokemons[yourpk_name].SP_ATTK
                    your_SP_DEF = pk.pokemons[yourpk_name].SP_DEF


                    all_dead_enemy = False
            if all_dead_enemy == False:
                continue
            else:
                return 0
            
    ## desenha na tela as info basicas ##

        draw_top_part()
        draw_enemy()

        draw_you()


##interative part

        step_1 = draw_basic_lower()

        match step_1:
            case "1":
                attack_chosen = draw_attack_lower()
                match attack_chosen:

                    #### escolheu um ataque ###

                    case "1" | "2" | "3" | "4":
                        attack_chosen = int(attack_chosen)-1
                        if attacks_display_PP[attack_chosen] > 0:
                            attacks_display_PP[attack_chosen] -= 1
                            if mv.moves[attacks_display[attack_chosen]].category == "Physical":
                                damage_your = (((((2*your_pk_lvl)//5+2)*mv.moves[attacks_display[attack_chosen]].power*your_ATTK)//enemy_DFS)//50+2)
                            elif mv.moves[attacks_display[attack_chosen]].category == "Special":
                                damage_your = (((((2*your_pk_lvl)//5+2)*mv.moves[attacks_display[attack_chosen]].power*your_SP_ATTK)//enemy_SP_DEF)//50+2)
                            else:
                                damage_your = 1
                            ### enemy chose attack for now will be "random"
                            enemy_attack_chosen = rm.randint(0,(len(attacks_display_enemy)-2))

                            if attacks_display_enemy_PP[enemy_attack_chosen] > 0:
                                attacks_display_enemy_PP[enemy_attack_chosen] -= 1
                                if mv.moves[attacks_display_enemy[enemy_attack_chosen]].category == "Physical":
                                    damage_enemy = (((((2*enemy_pk_lvl)//5+2)*mv.moves[attacks_display_enemy[enemy_attack_chosen]].power*enemy_ATTK)//your_DFS)//50+2)
                                    print(enemy_pk_lvl)
                                elif mv.moves[attacks_display_enemy[enemy_attack_chosen]].category == "Special":
                                    damage_enemy = (((((2*enemy_pk_lvl)//5+2)*mv.moves[attacks_display_enemy[enemy_attack_chosen]].power*enemy_SP_ATTK)//your_SP_DEF)//50+2)
                                else:
                                    damage_enemy = 1
                            else:
                                damage_enemy = 1
                        else:
                            print ("Sem PP")
                            ok = input("ok")
                            clean()
                            continue
                        if your_SPPD > enemy_SPPD:
                            clean()
                            total_life_enemy[enemypk_name] -= damage_your
                            if total_life_enemy[enemypk_name] < 0:
                                total_life_enemy[enemypk_name] = 0
                                draw_top_part()
                                draw_enemy()
                                draw_you()
                                print (f"{"="*100}\n\n{yourpk_name} used\n {attacks_display[attack_chosen]} {damage_your}!\n\n{"="*100}")
                                ok = input("")
                                clean()
                                continue
                            else :
                                draw_top_part()
                                draw_enemy()
                                draw_you()
                                print (f"{"="*100}\n\n{yourpk_name} used\n {attacks_display[attack_chosen]} {damage_your}!\n\n{"="*100}")
                                ok = input("")
                                clean()
                                total_life_you[yourpk_name] -= damage_enemy
                                if total_life_you[yourpk_name] < 0:
                                    total_life_you[yourpk_name] = 0
                                    draw_top_part()
                                    draw_enemy()
                                    draw_you()
                                    print (f"{"="*100}\n\n{yourpk_name} used\n {attacks_display[attack_chosen]} {damage_your}!\n\n{"="*100}")
                                    ok = input("")
                                    clean()
                                    continue
                                else :
                                    draw_top_part()
                                    draw_enemy()
                                    draw_you()
                                    print (f"{"="*100}\n\n{enemypk_name} used\n {attacks_display_enemy[enemy_attack_chosen]} {damage_enemy}!\n\n{"="*100}")
                                    ok = input("")
                                    clean()
                        else:
                            clean()
                            total_life_you[yourpk_name] -= damage_enemy
                            if total_life_you[yourpk_name] < 0:
                                total_life_you[yourpk_name] = 0
                                draw_top_part()
                                draw_enemy()
                                draw_you()
                                print (f"{"="*100}\n\n{enemypk_name} used\n {attacks_display_enemy[enemy_attack_chosen]} {damage_enemy}!\n\n{"="*100}")
                                ok = input("")
                                clean()
                                continue
                            else :
                                draw_top_part()
                                draw_enemy()
                                draw_you()
                                print (f"{"="*100}\n\n{enemypk_name} used\n {attacks_display_enemy[enemy_attack_chosen]} {damage_enemy}!\n\n{"="*100}")
                                ok = input("")
                                clean()
                                total_life_enemy[enemypk_name] -= damage_your
                                if total_life_enemy[enemypk_name] < 0:
                                    total_life_enemy[enemypk_name] = 0
                                    draw_top_part()
                                    draw_enemy()
                                    draw_you()
                                    print (f"{"="*100}\n\n{enemypk_name} used\n {attacks_display_enemy[enemy_attack_chosen]} {damage_enemy}!\n\n{"="*100}")
                                    ok = input("")
                                    clean()
                                    continue
                                else :
                                    draw_top_part()
                                    draw_enemy()
                                    draw_you()
                                    print (f"{"="*100}\n\n{yourpk_name} used\n {attacks_display[attack_chosen]} {damage_your}!\n\n{"="*100}")
                                    ok = input("")
                                    clean()


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



battle("Thuol","Alfaro")