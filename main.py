#RPG Hercules Adventure 
from story import *
from characters import *
from functions import *

'''As a developer, I want to make at least five commits on GitHub with descriptive messages.  

As a user, I want the ability to select Hercules’ attack using a menu prompt. 


As a user, I want the foe’s attack to be chosen at random. 


As a user, I want the results of each attack to be logged in the terminal.  


As a developer, I want my RunGame() function to call my other functions in a logical order that will determine game flow. 


As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!

fighting: light attack, hard attack
'''

print(preamble)
print(introduction)
battle(player, bandit)

