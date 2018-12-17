#this is code for mana and power pip chance
import random
mana = 0
character = 300
print("Your turn is starting")
roll = random.randint(1,10)
if roll == 5 or roll == 6 or roll == 7 or roll == 8 or roll == 9:
    mana = mana + 2
    print("You have gained a power pip. Your mana =")
    print mana
else:
    print ("You have gained a pip. Your mana =")
    mana = mana + 1
    print mana
#this is code for fizzle chance
roll2 = random.randint(1,100)
if roll2 <= ("75"):
    print ("No fizzle")
else:
    print("Sorry but you have fizzled")
#this is code for randomized damage
roll3 = random.randint(105,145)
character = character - roll3
print ("Your health now equals", character)