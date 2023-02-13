#As a developer, I want to use an Attack() function that will terminate when Hercules or an enemy’s health reaches zero.  
import random

def print_attacks():
    print("1 for Slash\n2 for Heavy Blow\n3 for Shield Bash\n")

def battle(player, enemy):
    while player["Health"] > 0 and enemy["Health"] > 0:
        #initiative = 0 
        player_attack(player, enemy)
        enemy_attack(player, enemy)
    if player["Health"] > 0:
        ("You won the fight!")
    else:
        print("You died in battle...glorious!")
        

def player_attack(player, enemy):
    print_attacks() #show choices 
    attack_choice = int(input("Enter number of attack you would like to use:\n"))
    if attack_choice == 1:
        if random.randrange(1,10) + player["Attack Power"] > 12:
            enemy["Health"] -= player["Attack Power"] * 5
    if attack_choice == 2:
        if random.randrange(1,10) + player["Attack Power"] > 15:
            enemy["Health"] -= player["Attack Power"] * 8
    if attack_choice == 3:
        if random.randrange(1,10) + player["Attack Power"] > 10:
            enemy["Health"] -= player["Attack Power"] * 3

def enemy_attack(player, enemy):
    print("Enemy slashes at you! You take ")
    enemy_attack = random.randrange(1,3)
    if enemy_attack == 1:
        print("Enemy slashes at you!\n")
        if random.randrange(1,20) + player["Agility"] < 15:
            damage = enemy["Attack Power"] * 5
            player["Health"] -= damage
            print(f"The enemy successfully slashes you, causing {damage} points in health damage")
    if enemy_attack == 2:
        print("Enemy swings hard at you!\n")
        if random.randrange(1,20) + player["Agility"] < 12:
            damage = enemy["Attack Power"] * 8
            player["Health"] -= damage
            print(f"The enemy successfully slashes you, causing {damage} points in health damage")
    if enemy_attack == 1:
        print("Enemy attempts to hit you with their shield\n")
        if random.randrange(1,20) + player["Agility"] < 18:
            damage = enemy["Attack Power"] * 3
            player["Health"] -= damage
            print(f"The enemy successfully slashes you, causing {damage} points in health damage")
