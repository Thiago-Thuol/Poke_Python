import pokemon as pk
import trainer as tr
import race as rc
import move as mv
import format_input as form
import os


## funcao q retorna uma chave (5==erro)

def inicio():
    a = form.format(input("Resposta : "))

    if a == "criar um treinador" or a == "1":
        return ("1")
    elif a == "criar um pokemon" or a == "2":
        return ("2")
    elif a == "adicionar um pokemon" or a == "3" or a == "adicionar um pokemon para um treinador":
        return ("3")
    elif a == "criar um treinador" or a == "4":
        return ("4")
    else:
        print ("Resposta Invalida")
        return ("5")
os.system('cls' if os.name == 'nt' else 'clear')
## Hud ###
def hud():
    while True:
        print (f"{"="*100}\n{' '*20}Bem Vindo ao CRIADOR DE POKEMON PYTHON !!!!!\n{' '*15}Esse programa esta em fase de testes e bugs sao esperados\n{"="*100}")
        print (f"Voce deseja fazer oq?\n\n1)Criar um treinador\n2)Criar um Pokemon\n3)Adicionar um pokemon para um treinador\n4)Obter informacao de algum treinador/Pokemon\n")
        key = "5"
        while key == "5":
            key = inicio()

##Criar treinador

        if key == "1":
            answer = form.format_names(input("Nome do treinador: "))
            tr.Trainer.add_trainer(answer)
            continuar = input("continue")
            os.system('cls' if os.name == 'nt' else 'clear')

##Criar Pokemon

        elif key == "2":
            Nome_pk = form.format_names(input("Digite o nome do pokemon: "))
            LVL_pk = int((input("Digite o level do pokemon: ")))
            print (f"Pokemons disponiveis: {[i for i in rc.races.keys()]}")
            race_pk = form.format_names(input("Digite a raca do pokemon: "))
            pk.pokemon.build_pk(Nome_pk,LVL_pk,race_pk)
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
            os.system('cls' if os.name == 'nt' else 'clear')