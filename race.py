import element as el

races={}

class race:
    def __init__(self,race,types:list,base_stats:list):
        self._race = race
        self._element = types
        self.base = base_stats
        races[race] = self

    def race_id(key):
        result = races[key]
        return result



with open("Races.txt") as info:
    for linhas in info:
        linhas = linhas.split(",")
        linhas[1] = linhas[1].split(" ")
        linhas[1] = list(linhas[1])
        temp_ele =[]
        for z in linhas[1]:
            temp_ele.append(el.elements[z])
        linhas[2] = linhas[2].split(" ")
        linhas[2] = list(linhas[2])
        linhas[2] = [int(i) for i in linhas[2]]
        temp_race = race(linhas[0],temp_ele,linhas[2])


