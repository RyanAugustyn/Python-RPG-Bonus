#As a user, I want Hercules (and each enemy) to have health, attack power, and a List of attack names saved in a Dictionary. 

class Character:
    def __init__(self, name, health, attack_power, agility):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.agility = agility




class Player(Character):
    def __init__(self, name, health, attack_power, agility):
        Character.__init__(self, name, health, attack_power, agility)
        # self.abilities = {"slash": 10, 
        # "lunge": 5,
        # "shield_bash": 3}


class Bandit(Character):
    def __init__(self, name, health, attack_power, agility):
        Character.__init__(self, name, health, attack_power, agility)


