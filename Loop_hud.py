from classes import pokemon as pk
from classes import trainer as tr
from classes import race as rc
from classes import move as mv
from classes import format_input as form


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

## Hud ###
def hud():
    while True:
        print (f"Voce deseja fazer oq?\n\n1)Criar um treinador\n2)Criar um Pokemon\n3)Adicionar um pokemon para um treinador\n4)Obter informacao de algum treinador/Pokemon\n")
        key = "5"
        while key == "5":
            key = inicio()
        if key == "1":
            answer = form.format_names(input("Nome do treinador: "))
            tr.trainer.add_trainer(answer)
        elif key == "2":
            Nome_pk = form.format_names(input("Digite o nome do pokemon: "))
            LVL_pk = int(input("Digite o level do pokemon: "))
            race_pk = form.format_names(input("Digite a raca do pokemon: "))
            pk.pokemon.build_pk(Nome_pk,LVL_pk,race_pk)
    
