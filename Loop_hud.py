import pokemon as pk
import trainer as tr
import race as rc
import move as mv
import format_input as form


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
            tr.Trainer.add_trainer(answer)
        elif key == "2":
            Nome_pk = form.format_names(input("Digite o nome do pokemon: "))
            LVL_pk = int((input("Digite o level do pokemon: ")))
            race_pk = form.format_names(input("Digite a raca do pokemon: "))
            pk.pokemon.build_pk(Nome_pk,LVL_pk,race_pk)
        elif key == "3":
            print(f"1) ADD_pokemon\n2) DEL_pokemon\n")
            answer = form.format(input("resposta: "))
            if answer == "1" or answer == "add":
                Nome_treinador = form.format_names(input("Nome do treinador: "))
                Nome_pk = form.format_names(input("Digite o nome do pokemon: "))
                tr.Trainer.add_party(Nome_treinador,Nome_pk)
            else:
                Nome_treinador = form.format_names(input("Nome do treinador: "))
                Nome_pk = form.format_names(input("Digite o nome do pokemon: "))
                tr.Trainer.del_party(Nome_treinador,Nome_pk)
