import element as el
import effect as ef
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
    def __str__ (self):
        return (f"{self.name}\n{self.element.element_name}\n{self.power}\n{self.category}\n{self.PP}\n{self.accuracy}\n{self.priority}\n{self.effect.nome}")

    
with open("Moves.txt", "r") as info:
    for linhas in info:
        command = (linhas.strip())
        exec(command)

