#As a developer, I want to use an Attack() function that will terminate when Hercules or an enemy’s health reaches zero.  
import random

def print_attacks():
    print("1 for Slash\n2 for Heavy Blow\n3 for Shield Bash\n")

def attack(player, enemy):
    while player["Health"] > 0 and enemy["Health"] > 0:
        #initiative = 0 
        print_attacks()
        attack_choice = int(input("Enter number of attack you would like to use:\n"))
        if attack_choice == 1:
            if random.randrange(1,10) + player["Attack Power"] > 12:
                enemy["Health"] -= 5
        if attack_choice == 2:
            if random.randrange(1,10) + player["Attack Power"] > 15:
                enemy["Health"] -= 10
        if attack_choice == 3:
            if random.randrange(1,10) + player["Attack Power"] > 10:
                enemy["Health"] -= 3
        print("Enemy slashes at you! You take ")
        enemy_attack = random.randrange(1,3)
        if enemy_attack < 3:
            print("no damage!")
        else:
            print("3 damage")
            player["Health"] -= 3

