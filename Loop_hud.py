import pokemon as pk
import trainer as tr
import race as rc
import move as mv
import format_input as form
import os
import fight_lopp as fg


## funcao q retorna uma chave (5==erro)

def inicio():
    a = form.format(input("Resposta : "))

    if a == "criar um treinador" or a == "1":
        return ("1")
    elif a == "criar um pokemon" or a == "2":
        return ("2")
    elif a == "adicionar um pokemon" or a == "3" or a == "adicionar um pokemon para um treinador":
        return ("3")
    elif a == "batalha" or a == "4":
        return ("4")
    else:
        print ("Resposta Invalida")
        return ("5")
os.system('cls' if os.name == 'nt' else 'clear')
## Hud ###
def hud():
    while True:
        print (f"{"="*100}\n{' '*20}Bem Vindo ao CRIADOR DE POKEMON PYTHON !!!!!\n{' '*15}Esse programa esta em fase de testes e bugs sao esperados\n{"="*100}")
        print (f"Voce deseja fazer oq?\n\n1)Criar um treinador\n2)Criar um Pokemon\n3)Adicionar um pokemon para um treinador\n4)Batalhar\n")
        key = "5"
        while key == "5":
            key = inicio()

##Criar treinador

        if key == "1":
            answer = form.format_names(input("\nNome do treinador: "))
            tr.Trainer.add_trainer(answer)
            continuar = input("continue")
            os.system('cls' if os.name == 'nt' else 'clear')

##Criar Pokemon

        elif key == "2":
            try:
                os.system('cls' if os.name == 'nt' else 'clear')
                print (f"Nomes ja usados {[i for i in pk.pokemons.keys()]}\n")
                Nome_pk = form.format_names(input("\nDigite o nome do pokemon: "))
                LVL_pk = int((input("\nDigite o level do pokemon: ")))
                if LVL_pk >100 or LVL_pk <1:
                    print ("\nERRO\nO level deve ser um numero entre 1 e 100 !")
                    continuar = input("continue")
                else:
                    print (f"Pokemons disponiveis: {[i for i in rc.races.keys()]}")
                    race_pk = form.format_names(input("Digite a raca do pokemon: "))
                    os.system('cls' if os.name == 'nt' else 'clear')
                    pk.pokemon.build_pk(Nome_pk,LVL_pk,race_pk)
                    print (f"\nSucesso!\n Pokemons disponiveis: {[i for i in pk.pokemons.keys()]}\n")
                    continuar = input("continue")
            except:
                print(f"\nInput invalido")
                continuar = input("continue")
            os.system('cls' if os.name == 'nt' else 'clear')

##MOVE SET

        elif key == "3":
            print(f"1) ADD_pokemon\n2) DEL_pokemon\n")
            answer = form.format(input("resposta: "))

##ADD MOVE

            if answer == "1" or answer == "add":
                try:
                    print (f"Treinadores disponiveis: {[i for i in tr.trainers.keys()]}\n")

                    Nome_treinador = form.format_names(input("Nome do treinador: "))

                    print (f"Pokemons disponiveis: {[i for i in pk.pokemons.keys()]}")

                    Nome_pk = form.format_names(input("Digite o nome do pokemon: "))

                    tr.Trainer.add_party(Nome_treinador,Nome_pk)
                    continuar = input("continue")
                except:
                    print ("Input Incorreto")
                os.system('cls' if os.name == 'nt' else 'clear')

##DEL MOVE

            else:
                print (f"Treinadores disponiveis: {[i for i in tr.trainers.keys()]}\n")
                Nome_treinador = form.format_names(input("Nome do treinador: "))

                print (f"Pokemons disponiveis: {[i.name for i in tr.trainers[Nome_treinador].party]}")

                Nome_pk = form.format_names(input("Digite o nome do pokemon: "))
                tr.Trainer.del_party(Nome_treinador,Nome_pk)
                continuar = input("continue")
                os.system('cls' if os.name == 'nt' else 'clear')
        
        if key == "4":
                treinadore_temp = [i for i in tr.trainers.keys()]
                print (f"\nTreinadores disponiveis: {treinadore_temp}\n")
                player1 = form.format_names(input("Nome do Player 1 (you): "))
                treinadore_temp.remove(player1)
                print (f"\nTreinadores disponiveis: {treinadore_temp}\n")
                player2 = form.format_names(input("Nome do Player 2: "))
                fg.battle(player2,player1)