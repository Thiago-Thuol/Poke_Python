import race as rc
import element as el
import move as mv
import random as rm
import format_input as fm

##lista com todos pokemons

pokemons = {}

## classe pokemon

class pokemon:
    def __init__(self,name:str="Noob",lvl:int=0,race:rc.race=rc.races["Bulbasaur"],xp:int=0):
        self.name = name
        self.lvl = lvl
        self.hp = 0
        self.max_hp = 0
        self.xp = xp
        self.race = race
        self.attaks = [{},{},{},{}]
        self.attaks_pp = [{},{},{},{}]
        self.base = race.base
        self.iv = [rm.randrange(1,31) for i in range(6)]
        self.HP = 0
        self.ATTK = 0
        self.DFS = 0
        self.SP_ATTK = 0
        self.SP_DEF = 0
        self.SPPD = 0
        self.base_stat_calc()


## adiciona um  movimento

    def add_mov(nome,sure_mov,id_chosen=0):
        temp_poke = pokemons[nome]
        temp_race = temp_poke.race._race
        movi = sure_mov
        attack_list = []
        for i in temp_poke.attaks:
            name = ([j for j in i])
            for index in name:
                attack_list.append(index)
        print (f"Ataques do seu pokemon: {attack_list}")
##MUDAR ATAQUE

        if nome in pokemons.keys() and sure_mov == False:
            print (f"Moves para esse Pokemon\n{rc.races_learn[temp_race]}")

## ESCHOLHER MOVE

            movi = (input("Escolha o Move (escreva certo pfv):\n"))
            if movi in mv.moves.keys() and movi in rc.races_learn[temp_race] and movi not in attack_list:
                temp_attack = mv.moves[movi]
                temp_pp = temp_attack.PP
                quantidade_pool = len(attack_list)
                if quantidade_pool == 4:
## SUBSTITUIR MOVE

                    print (f"Qual move voce quer substituir?\n{attack_list}")
                    substituir = fm.format_names((input("Escolha 1 2 3 4:\n")))
                    match substituir:
                        case "1" |"2" |"3" |"4":
                            substituir = int(substituir)
                            pop_item = (attack_list[substituir-2])
                            print (pop_item)
                            pokemons[nome].attaks[substituir-2].pop(pop_item)
                            pokemons[nome].attaks[substituir-2][movi] = temp_attack
                            print (temp_poke.id())

                else:
                    pokemons[nome].attaks[quantidade_pool-2][movi] = temp_attack
                    print (temp_poke.id())
            else:
                print ("Esse pokemon nao pode aprender esse ataque")

##CRIANDO POKEMON NAO PRECISO ESCOLHER

        elif nome in pokemons.keys() and sure_mov != 1 and movi in rc.races_learn[temp_race] and movi not in attack_list:
            if movi in mv.moves.keys():                                                   
                    print (movi)
                    temp_attack = mv.moves[movi]
                    temp_pp = temp_attack.PP
                    temp_poke.attaks[id_chosen][movi] = temp_attack
                    temp_poke.attaks_pp[id_chosen][movi] = temp_pp
            print (temp_poke.id())
        else:
            print (sure_mov)
            print (f"\nPokemon ou Move nao existe\n")
## criar um pokemon

    def build_pk (nome,lvl,race):
        if nome not in pokemons.keys():
            temp_race = rc.race.race_id(race)
            temp_poke = pokemon(name=nome,lvl=lvl,race=temp_race)
            pokemons[nome] = temp_poke
            for i in range(4):
                temp_index = rm.randint(0,len(rc.races_learn[race]))-1
                move = (rc.races_learn[race][temp_index])
                pokemon.add_mov(nome,move,id_chosen=i)
            print (temp_poke.id())
        else:
            print ("Pokemon ja existe")

## calculo dos stats  

    def base_stat_calc(self):
        self.HP = (((2*self.base[0]+self.iv[0])*self.lvl)//100)+self.lvl+10
        self.hp = self.HP
        self.max_hp = self.HP
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
        attacks_id = []
        for i in self.attaks:
            name = ([j for j in i])
            for index in name:
                attacks_id.append(index)
        PP_id = []
        for i in self.attaks_pp:
            PPSd = ([j for j in i.values()])
            for index in PPSd:
                PP_id.append(index)
        moves_id = []
        for i in range(len(attacks_id)):
            moves_id.append(f"{attacks_id[i-1]} PP: {PP_id[i-1]}")

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

pokemon.build_pk(nome='Thuol',lvl=10,race="Bulbasaur")

pokemon.build_pk(nome='Alfaro',lvl=15,race="Charmander")

pokemon.build_pk(nome='Trotsky',lvl=25,race="Abra")

pokemon.build_pk(nome='Puta',lvl=10,race="Vaporeon")

pokemon.build_pk(nome='Lula',lvl=100,race="Tentacool")

pokemon.build_pk(nome='Gui',lvl=100,race="Grimer")

pokemon.build_pk(nome='Mendigo',lvl=50,race="Gengar")

pokemon.build_pk(nome='Rodrigo',lvl=50,race="Blastoise")

pokemon.build_pk(nome='Wagner',lvl=50,race="Charizard")

pokemon.build_pk(nome='Luccas',lvl=50,race="Venusaur")
