from classes import race as rc
from classes import element as el
from classes import move as mv
import random as rm

##lista com todos pokemons

pokemons = {}

## classe pokemon

class pokemon:
    def __init__(self,name:str="Noob",lvl:int=0,race:rc.race=rc.Mew,xp:int=0,show_stats=True):
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
        pokemons[name] = race._race
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

    def build_pk (nome,lvl,race):
        try:    
            if nome in pokemons.keys():
                if nome not in pokemons and pokemons[nome] == race:
                    command = (f"{nome} = pokemon('{nome}',{lvl},rc.{race})")
                    exec(command) 
                    print (pokemons)
                else: 
                    print("\nPokemon ja existe\n")
            else:
                command = (f"{nome} = pokemon('{nome}',{lvl},rc.{race})")
                exec(command) 
                print (pokemons)
        except:
            print (f"\nINPUT INVALIDO\n")

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


## formatacao dos textos do ataque 

    def id (self):
        moves_id = ["Move: "+i.name+" PP: "+f"{self.attaks[i]}" for i in self.attaks]

## func para mostrar info do pokemon

        return (f"""
Nome: {self.name} 
Raca: {self.race._race} 
Level: {self.lvl} XP: {self.xp} 
Attaks: {moves_id}
Element: {[ i.element_name for i in self.race._element]}
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

Thuol = pokemon(name='Thuol',lvl=10,race=rc.Bulbasaur,show_stats=False)

Alfaro = pokemon(name='Alfaro',lvl=15,race=rc.Charmander,show_stats=False)

Trotsky = pokemon(name='Trotsky',lvl=25,race=rc.Abra,show_stats=False)

Puta = pokemon(name='Puta',lvl=1,race=rc.Vaporeon,show_stats=False)

Mendigo = pokemon(name='Mendigo',lvl=50,race=rc.Gengar,show_stats=False)

Lula = pokemon(name='Lula',lvl=100,race=rc.Tentacool,show_stats=False)

Gui = pokemon(name='Gui',lvl=100,race=rc.Grimer,show_stats=False)