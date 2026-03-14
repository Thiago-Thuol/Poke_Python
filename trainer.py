import pokemon as pk
trainers = {}


##classe de treinadores

class Trainer:
    def __init__ (self,name:str="shu"):
        self.name = name
        self.party = []

## criar um treinador

    def id_player(self):
        print (f"Trainer : {self.name}")

    def lista_add(self):
        trainers[self.name] = self

    def add_trainer (nome):

        if nome not in trainers: 
            novo = Trainer(nome)
            novo.lista_add()
            print(f"\nTreinador criado com sucesso!\n\nTreinadores: {[i for i in trainers.keys()]}")
        else:
            print ("\nJogador ja existe\n")




## funcoes para add ou tirar pokemon

    def add_party(name,pokemon):
        if name in trainers.keys():
            temp_trainer = trainers[name]
            temp_pok = pk.pokemon.get_pokemon(pokemon)
            if len(temp_trainer.party) >5:
                print  ("\nParty cheia\n")
            elif temp_pok in temp_trainer.party:
                print ("\nPokemon repetido\n")
            else:
                temp_trainer.party.append(temp_pok)
                temp_trainer.id_trainer()
        else:
            print("\nTreinador nao existe\n")
    
    def del_party(name,pokemon):
        if name in trainers.keys():
            temp_trainer = trainers[name]
            temp_pok = pk.pokemon.get_pokemon(pokemon)
            if len(temp_trainer.party) == 0:
                print ("Party Vazia")
            elif temp_pok not in temp_trainer.party:
                print ("Pokemon nao esta na party")
            else: 
                temp_trainer.party.remove(temp_pok)
        else:
                temp_trainer.party.append(temp_pok)
                temp_trainer.id_trainer()

## Debug para aanalisar os stats do obj

    def id_trainer(self):
        self.org_party_list = [i.id() for i in self.party]
        self.org_party_list_final = str()
        for i in range(len(self.org_party_list)):
            self.org_party_list_final = (f"{self.org_party_list_final}\n{self.org_party_list[i-1]}\n{"-"*100}")
        print (f"Treinador: {self.name}\n\nPOKEMONS\n\n{self.org_party_list_final}")

### TREINADOR TESTE ####

Trainer.add_trainer(nome = "Thuol")
Trainer.add_trainer(nome = "Alfaro")

Trainer.add_party("Alfaro","Trotsky")

Trainer.add_party("Alfaro","Gui")

Trainer.add_party("Thuol","Mendigo")
##Thuol_trainer.add_party(pk.Trotsky)
##Thuol_trainer.add_party(pk.Mendigo)
##Thuol_trainer.add_party(pk.Lula)
##Thuol_trainer.add_party(pk.Gui)