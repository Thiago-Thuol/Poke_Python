class element:
    def __init__ (self,name: str,weakness: str="None",super_effective: str="None"):
        self.element_name = name
        self.weakness = weakness
        self.super_effective = super_effective

    def id (self):
        return (f"{self.element_name}")

Normal = element("Normal",
    weakness=["Fighting"],
    super_effective=[]
)

Fire = element("Fire",
    weakness=["Water","Ground","Rock"],
    super_effective=["Grass","Ice","Bug","Steel"]
)

Water = element("Water",
    weakness=["Electric","Grass"],
    super_effective=["Fire","Ground","Rock"]
)

Electric = element("Electric",
    weakness=["Ground"],
    super_effective=["Water","Flying"]
)

Grass = element("Grass",
    weakness=["Fire","Ice","Poison","Flying","Bug"],
    super_effective=["Water","Ground","Rock"]
)

Ice = element("Ice",
    weakness=["Fire","Fighting","Rock","Steel"],
    super_effective=["Grass","Ground","Flying","Dragon"]
)

Fighting = element("Fighting",
    weakness=["Flying","Psychic","Fairy"],
    super_effective=["Normal","Ice","Rock","Dark","Steel"]
)

Poison = element("Poison",
    weakness=["Ground","Psychic"],
    super_effective=["Grass","Fairy"]
)

Ground = element("Ground",
    weakness=["Water","Grass","Ice"],
    super_effective=["Fire","Electric","Poison","Rock","Steel"]
)

Flying = element("Flying",
    weakness=["Electric","Ice","Rock"],
    super_effective=["Grass","Fighting","Bug"]
)

Psychic = element("Psychic",
    weakness=["Bug","Ghost","Dark"],
    super_effective=["Fighting","Poison"]
)

Bug = element("Bug",
    weakness=["Fire","Flying","Rock"],
    super_effective=["Grass","Psychic","Dark"]
)

Rock = element("Rock",
    weakness=["Water","Grass","Fighting","Ground","Steel"],
    super_effective=["Fire","Ice","Flying","Bug"]
)

Ghost = element("Ghost",
    weakness=["Ghost","Dark"],
    super_effective=["Psychic","Ghost"]
)

Dragon = element("Dragon",
    weakness=["Ice","Dragon","Fairy"],
    super_effective=["Dragon"]
)

Fairy = element("Fairy",
    weakness=["Poison","Steel"],
    super_effective=["Fighting","Dragon","Dark"]
)

Steel = element("Steel",
    weakness=["Fire","Fighting","Ground"],
    super_effective=["Ice","Rock","Fairy"]
)

Dark = element("Dark",
    weakness=["Fighting","Bug","Fairy"],
    super_effective=["Psychic","Ghost"]
)