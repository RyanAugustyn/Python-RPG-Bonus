from random import randrange

def attack(combatant1, combatant2):
        chance = randrange(0, 100)
        #check for hit chance
        if chance + combatant1.agility < 50:
            print(f"{combatant1.name} misses!\n")  
        elif chance + combatant1.agility > 95:
            print("CRITICAL HIT!!")
            attack_damage = 5 * combatant1.active_weapon.attack_power 
            print(f"{combatant1.name} hits for {attack_damage} damge")
            combatant2.health -= attack_damage
            if combatant2.health < 0:
                combatant2.health = 0
            print(f"{combatant2.name} currently has {combatant2.health} health remaining\n\n")
        else:
            attack_damage = randrange(1,3) * combatant1.active_weapon.attack_power 
            print(f"{combatant1.name}  hits for {attack_damage} damge")
            combatant2.health -= attack_damage
            if combatant2.health < 0:
                combatant2.health = 0
            print(f"{combatant2.name}  currently has {combatant2.health} health remaining\n\n")