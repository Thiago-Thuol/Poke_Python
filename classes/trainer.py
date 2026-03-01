from classes import pokemon as pk
trainers = []


##classe de treinadores

class trainer:
    def __init__ (self,name:str):
        self.name = name
        self.__party = []
        trainers.append(name)


## criar um treinador
    def add_trainer (nome):
        try:
            if nome not in trainers: 
                command_add_player = (f"\n{nome} = trainer('{nome}')\n")
                exec(command_add_player)
            else:
                print ("\nJogador ja existe\n")
        except:
            print ("\nINPUT INVALIDO\n")



## funcoes para add ou tirar pokemon

    def add_party(self,pokemon):
        if len(self.__party) >5:
            print  ("Party cheia")
        elif pokemon in self.__party:
            print ("Pokemon repetido")
        else:
            self.__party.append(pokemon)
    
    def del_party(self,pokemon):

        if len(self.__party) == 0:
            print ("Party Vazia")
        elif pokemon not in self.__party:
            print ("Pokemon nao esta na party")
        else: 
            self.__party.pop(pokemon)



## Debug para aanalisar os stats do obj

    def __str__(self):
        self.org_party_list = [i.id() for i in self.__party]
        self.org_party_list_final = str()
        for i in range(len(self.org_party_list)):
            self.org_party_list_final = (f"{self.org_party_list_final}\n{self.org_party_list[i-1]}\n{"-"*100}")
        return (f"Treinador: {self.name}\n\nPOKEMONS\n\n{self.org_party_list_final}")

### TREINADOR TESTE ####

Thuol_trainer = trainer("Thuol")

##Thuol_trainer.add_party(pk.Thuol)
Thuol_trainer.add_party(pk.Alfaro)
##Thuol_trainer.add_party(pk.Puta)
##Thuol_trainer.add_party(pk.Trotsky)
##Thuol_trainer.add_party(pk.Mendigo)
##Thuol_trainer.add_party(pk.Lula)
Thuol_trainer.add_party(pk.Gui)