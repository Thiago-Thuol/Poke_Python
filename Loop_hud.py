import pokemon as pk
import trainer as tr
import race as rc
import move as mv
import format_input as form
import os
import fight_lopp as fg

def clean():
    os.system('cls' if os.name == 'nt' else 'clear')

def inicio():
    a = form.format(input("Resposta : "))

    match a:
        case "criar um treinador" | "1":
        ##Criar treinador
            print (f"Treinadores indisponiveis: {[i for i in tr.trainers.keys()]}\n")
            answer = form.format_names(input("\nNome do treinador: "))
            tr.Trainer.add_trainer(answer)
            continuar = input("continue")
            clean()

            
        case "criar um pokemon" | "2":
            ##Criar Pokemon
            try:
                clean()
                print (f"Nomes ja usados {[i for i in pk.pokemons.keys()]}\n")
                Nome_pk = form.format_names(input("\nDigite o nome do pokemon: "))
                LVL_pk = int((input("\nDigite o level do pokemon: ")))
                if LVL_pk >100 or LVL_pk <1:
                    print ("\nERRO\nO level deve ser um numero entre 1 e 100 !")
                    continuar = input("continue")
                else:
                    print (f"Pokemons disponiveis: {[i for i in rc.races.keys()]}")
                    race_pk = form.format_names(input("Digite a raca do pokemon: "))
                    clean()
                    pk.pokemon.build_pk(Nome_pk,LVL_pk,race_pk)
                    print (f"\nSucesso!\n Pokemons disponiveis: {[i for i in pk.pokemons.keys()]}\n")
                    continuar = input("continue")
            except:
                print(f"\nInput invalido")
                continuar = input("continue")
            clean()


        case "adicionar um pokemon" | "3" |"adicionar um pokemon para um treinador":

##MOVE SET
    
            print(f"1) ADD_pokemon\n2) DEL_pokemon\n")
            answer = form.format(input("resposta: "))

##ADD MOVE

            if answer == "1" or answer == "add":
                try:
                    print (f"Treinadores disponiveis: {[i for i in tr.trainers.keys()]}\n")

                    Nome_treinador = form.format_names(input("Nome do treinador: "))

                    print (f"Pokemons disponiveis: {[i for i in pk.pokemons.keys()]}")

                    Nome_pk = form.format_names(input("Digite o nome do pokemon: "))
                    clean()
                    tr.Trainer.add_party(Nome_treinador,Nome_pk)
                    continuar = input("continue")
                except:
                    print ("Input Incorreto")
                clean()

##DEL MOVE

            else:
                print (f"Treinadores disponiveis: {[i for i in tr.trainers.keys()]}\n")
                Nome_treinador = form.format_names(input("Nome do treinador: "))

                print (f"Pokemons disponiveis: {[i.name for i in tr.trainers[Nome_treinador].party]}")

                Nome_pk = form.format_names(input("Digite o nome do pokemon: "))
                tr.Trainer.del_party(Nome_treinador,Nome_pk)
                continuar = input("continue")
                clean()

## ADD MOVE

        case "add ataque" | "adicionar ataque" | "4":
            clean()
            print (f"Pokemons Disponiveis {[i for i in pk.pokemons.keys()]}\n")
            Nome_pk = form.format_names(input("Digite o nome do pokemon: "))
            pk.pokemon.add_mov(Nome_pk,0)
            continuar = input("continue")
            clean()

###OBTER ID

        case "ID" | "5":
            clean()
            print (f"1) ID Players?({len([i for i in tr.trainers.keys()])})\n2) ID Pokemons?({len([i for i in pk.pokemons.keys()])})")
            choice = form.format(input("Resposta: "))
            match choice:
                case "1" | "players":
                    print (f"Seu treinadores: {[i for i in tr.trainers.keys()]}")
                    choice = form.format_names(input("Resposta: "))
                    clean()
                    tr.trainers[choice].id_trainer()
                case "2" | "pokemons":
                    print (f"Seu pokemons: {[i for i in pk.pokemons.keys()]}")
                    choice = form.format_names(input("Resposta: "))
                    clean()
                    print (pk.pokemons[choice].id())
            continuar = input("continue")
## BATALHAR
        case "batalha" |"6":
            try:    
                treinadore_temp = [i for i in tr.trainers.keys()]
                print (f"\nTreinadores disponiveis: {treinadore_temp}\n")
                player1 = form.format_names(input("Nome do Player 1 (you): "))
                treinadore_temp.remove(player1)
                print (f"\nTreinadores disponiveis: {treinadore_temp}\n")
                player2 = form.format_names(input("Nome do Player 2: "))
                fg.battle(player1,player2)
            except:
                print ("Input Invalido!")
        case _ :
            print ("Resposta Invalida")
            clean()
## Hud ###
def hud():
    clean()
    while True:
        clean()
        print (f"{"="*100}\n{' '*20}Bem Vindo ao CRIADOR DE POKEMON PYTHON !!!!!\n{' '*15}Esse programa esta em fase de testes e bugs sao esperados\n{"="*100}")
        print (f"Voce deseja fazer oq?\n\n1)Criar um treinador\n2)Criar um Pokemon\n3)Adicionar um pokemon para um treinador\n4)Adicionar Ataque para um pokemon\n5)ID Pokemon/Treinador\n6)Batalhar\n")
        inicio()