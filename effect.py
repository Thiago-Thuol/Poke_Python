effects = {}

class Effect:
    def __init__ (self,nome):
        self.nome = nome
        self.condicion = 0
        self.Effect = 0
        effects[nome] = self

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
Raise_Attack = Effect("Raise_Attack")
Raise_Defense = Effect("Raise_Defense")
Raise_Special = Effect("Raise_Special")
Raise_Speed = Effect("Raise_Speed")
Raise_Evasion = Effect("Raise_Evasion")

# Stat Changes – Debuffs
Lower_Attack = Effect("Lower_Attack")
Lower_Defense = Effect("Lower_Defense")
Lower_Special = Effect("Lower_Special")
Lower_Speed = Effect("Lower_Speed")
Lower_Accuracy = Effect("Lower_Accuracy")
Lower_Evasion = Effect("Lower_Evasion")

Nones = Effect("Nones")
