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
        linhas[7] = int(linhas[7])
        effec_temp = ef.Effect(linhas[4])
        elemento_temp = el.elements[linhas[1]]
        temp_race = move(linhas[0],elemento_temp,linhas[2],linhas[3],linhas[4],linhas[5],linhas[6],linhas[7],linhas[8])
print (moves["Pound"].element)

can_learn = {}