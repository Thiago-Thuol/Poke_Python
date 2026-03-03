import race as rc
import element as el
import move as mv
import random as rm

##lista com todos pokemons

pokemons = {}

## classe pokemon

class pokemon:
    def __init__(self,name:str="Noob",lvl:int=0,race:rc.race=rc.races["Bulbasaur"],xp:int=0,show_stats=True):
        self.name = name
        self.lvl = lvl
        self.hp = 0
        self.xp = xp
        self.race = race
        self.attaks = {}
        self.base = race.base
        self.iv = [rm.randrange(1,31) for i in range(6)]
        self.HP = 0
        self.ATTK = 0
        self.DFS = 0
        self.SP_ATTK = 0
        self.SP_DEF = 0
        self.SPPD = 0
        self.base_stat_calc()
        if show_stats == True:
            print (self.id())


## adiciona um  movimento

    def add_mov(self,movi:mv):
        for i in range(len(self.race._element)):
         if movi.element.element_name == self.race._element[i-1].element_name:
            self.attaks[movi] = movi.PP
        else:
            print ("Tipo incompativel")

## criar um pokemon

    def build_pk (nome,lvl,race,stats=0):
        if nome not in pokemons.keys():
            temp_race = rc.race.race_id(race)
            temp_poke = pokemon(name=nome,lvl=lvl,race=temp_race,show_stats=stats)
            pokemons[nome] = temp_poke
        else:
            print ("Pokemon ja existe")

## calculo dos stats  

    def base_stat_calc(self):
        self.HP = (((2*self.base[0]+self.iv[0])*self.lvl)//100)+self.lvl+10
        self.hp = self.HP
        calc = lambda x,y:(((2*x+y)*self.lvl)//100)+5
        self.ATTK = calc(self.base[1],self.iv[1])
        self.DFS = calc(self.base[2],self.iv[2])
        self.SP_ATTK = calc(self.base[3],self.iv[3])
        self.SP_DEF = calc(self.base[4],self.iv[4])
        self.SPPD = calc(self.base[5],self.iv[5])

## GET POKEMON
    def get_pokemon(key):
        saida = pokemons[key]
        return(saida)

    


## formatacao dos textos do ataque 

    def id (self):
        moves_id = ["Move: "+i.name+" PP: "+f"{self.attaks[i]}" for i in self.attaks]

## func para mostrar info do pokemon

        return (f"""
Nome: {self.name} 
Raca: {self.race._race} 
Level: {self.lvl} XP: {self.xp} 
Attaks: {moves_id}
Element: {[i.element_name for i in self.race._element]}
IV: {self.iv}
BASE STATS: {self.base}
HP: {self.HP}
ATTK: {self.ATTK}
DFS: {self.DFS} 
SP_ATTK: {self.SP_ATTK} 
SP_DEF: {self.SP_DEF} 
SPEED: {self.SPPD} 
 """)
    
#### POKEMONS BASE PARA TESTES#####

pokemon.build_pk(nome='Thuol',lvl=10,race="Bulbasaur",stats=False)

pokemon.build_pk(nome='Alfaro',lvl=15,race="Charmander",stats=False)

pokemon.build_pk(nome='Trotsky',lvl=25,race="Abra",stats=False)

pokemon.build_pk(nome='Puta',lvl=1,race="Vaporeon",stats=False)

pokemon.build_pk(nome='Mendigo',lvl=50,race="Gengar",stats=False)

pokemon.build_pk(nome='Lula',lvl=100,race="Tentacool",stats=False)

pokemon.build_pk(nome='Gui',lvl=100,race="Grimer",stats=False)