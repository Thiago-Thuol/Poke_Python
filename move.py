import element as el
import effect as ef

moves = {}

class move:
    def __init__ (self,name,element:list=[],power:int=0,accuracy:int=0,category:str="Physical",PP:int=0,priority:int=0,effect=ef.Nones,multi_hit = 0,recoil = 0):
        self.name = name
        self.element = element
        self.power = power
        self.category = category
        self.PP = PP
        self.accuracy = accuracy
        self.priority = priority
        self.effect = effect
        self.multi_hit = multi_hit
        self.recoil = recoil
        moves[name] = self

    def __str__ (self):
        return (f"{self.name}\n{self.element.element_name}\n{self.power}\n{self.category}\n{self.PP}\n{self.accuracy}\n{self.priority}\n{self.effect.nome}")

    
with open("Moves.txt", "r") as info:
    for linhas in info:
        linhas = linhas.split(",")
        linhas[2] = int(linhas[2])
        linhas[3] = int(linhas[3])
        linhas[5] = int(linhas[5])
        linhas[5] = int(linhas[5])
        linhas[6] = int(linhas[6])
        linhas[8] = int(linhas[8])
        effect_temp = ef.effects[linhas[7]]
        type_temp = ef.Effect(linhas[4])
        elemento_temp = el.elements[linhas[1]]
        temp_race = move(linhas[0],type_temp,linhas[2],linhas[3],linhas[4],linhas[5],linhas[6],linhas[7],linhas[8],linhas[9])

teste = move(name="Teste",element=el.elements["Fire"],power=100,accuracy=100,category="status",PP=10,priority=1,effect=ef.Burn,multi_hit=2,recoil=0)

can_learn = {}