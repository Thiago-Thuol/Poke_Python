class Effect:
    def __init__ (self,nome):
        self.nome = nome
        self.condicion = 0
        self.Effect = 0

# Status Conditions
Paralyze = Effect("Paralyze")
Sleep = Effect("Sleep")
Burn = Effect("Burn")
Freeze = Effect("Freeze")
Poison = Effect("Poison")
Confusion = Effect("Confusion")
Disable = Effect("Disable")
HighCrit = Effect("HighCrit")
Flinch = Effect("Flinch")

# Stat Changes – Buffs
Raise_Attack = Effect("Raise Attack")
Raise_Defense = Effect("Raise Defense")
Raise_Special = Effect("Raise Special")
Raise_Speed = Effect("Raise Speed")
Raise_Evasion = Effect("Raise Evasion")

# Stat Changes – Debuffs
Lower_Attack = Effect("Lower Attack")
Lower_Defense = Effect("Lower Defense")
Lower_Special = Effect("Lower Special")
Lower_Speed = Effect("Lower Speed")
Lower_Accuracy = Effect("Lower Accuracy")

Nones = Effect("None")
