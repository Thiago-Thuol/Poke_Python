from classes import element as el
class race:
    def __init__(self,race,types:list,base_stats:list):
        self._race = race
        self._element = types
        self.base = base_stats

try:
    with open("Races.txt", "r") as info:
        for linhas in info:
            command = (linhas.strip())
            exec(command)
except:
    while True:
        a = input("errorr")



