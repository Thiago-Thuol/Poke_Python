class effect:
    def __init__ (self,nome):
        self.nome = nome
        self.condicion = 0
        self.effect = 0

# Status Conditions
Paralyze = effect("Paralyze")
Sleep = effect("Sleep")
Burn = effect("Burn")
Freeze = effect("Freeze")
Poison = effect("Poison")
Confusion = effect("Confusion")
Disable = effect("Disable")
HighCrit = effect("HighCrit")
Flinch = effect("Flinch")

# Stat Changes – Buffs
Raise_Attack = effect("Raise Attack")
Raise_Defense = effect("Raise Defense")
Raise_Special = effect("Raise Special")
Raise_Speed = effect("Raise Speed")
Raise_Evasion = effect("Raise Evasion")

# Stat Changes – Debuffs
Lower_Attack = effect("Lower Attack")
Lower_Defense = effect("Lower Defense")
Lower_Special = effect("Lower Special")
Lower_Speed = effect("Lower Speed")
Lower_Accuracy = effect("Lower Accuracy")

Nones = effect("None")
