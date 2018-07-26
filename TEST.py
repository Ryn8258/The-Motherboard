import time
wizard = "fire"
character = 100000000000000000000000000000000000000000000000
pixie = 1
enemy = 7963679376
print("Your turn is starting")
time.sleep(2)
if wizard== "Fire" or wizard== "fire":
    print("You have flame spark, fire cat and fire elf in your spell deck")
elif wizard== "Ice" or wizard== "ice":
    print("You have ice shard, frost beetle, and snow serpent in your spell deck")
elif wizard== "Life" or wizard== "life":
                            print("You have life beam, imp, and leprechaun in your spell deck")
elif wizard== "Death" or wizard== "death":
    print("You have death blast, dark pixie, ghoul in your spell deck")
elif wizard== "Myth" or wizard== "myth":
    print("You have myth blast, blood bat, and troll in your spell deck")
elif wizard== "Storm" or wizard== "storm":
    print("You have lightning spark, storm snake, and lightning bat in your spell deck")
elif wizard== "Balance" or wizard== "balance":
    print("You have balance beam, scarab, and scorpion in your spell deck")
else:
    print("Because you picked an invalid class you cannot continue the game, please reload the page")
spell= raw_input("Enter your spell (please use only lowercase):")
if spell== "flame spark" or spell== "ice shard" or spell== "life beam" or spell== "death blast" or spell== "myth blast" or spell== "lightning spark" or spell== "balance beam":
    enemy = enemy - 60
    print ("You have delt 60 dam to the enemy. Enemy health =")
    print enemy
elif spell== "storm snake":
    enemy = enemy -130
    print ("You have delt 130 dam to the enemy. Enemy health =")
    print enemy
elif spell== "fire cat": 
    enemy = enemy -120
    print ("You have delt 120 dam to the enemy. Enemy health =")
    print enemy
elif spell== "blood bat":
    enemy = enemy -110
    print ("You have delt 110 dam to the enemy. Enemy health =")
    print enemy
elif spell== "fire elf":
    enemy = enemy- 220
    print("You have delt 220 dam to the enemy. Enemy helath =")
    print enemy
elif spell== "pixie":
    if pixie <= 0:
        print("sorry you are out of pixies and you have fizzled")
    else:
        character = character + 300
        pixie = pixie - 2
        print("You have healed yourself, your health =")
        print character
elif spell== ("lightning bat"):
    enemy = enemy -240
    print("You have delt 240 dam to the enemy. Enemy health =")
    print enemy
elif spell== ("troll"):
    enemy = enemy - 200
    print("You have delt 200 dam to the enemy. Enemy health =")
    print enemy
elif spell== ("ghoul"):
    enemy = enemy -160
    character = character + 80
    print("You have delt 160 dam the enemy and restored 80 health to your self.")
    time.sleep(4)
    print("Enemy health = " + enemy)
    time.sleep(2)
    print("Your health = " + character)
    time.sleep(2)
elif spell== ("snow serpent") or spell== ("leprachaun") or spell== ("scorpion"):
    enemy = enemy -190
    print("You have del 190 dam to the enemy. Enemy health =")
    print enemy
elif spell== "frost beetle" or spell== "dark pixie" or spell== "imp" or spell== "scarab":
    enemy = enemy - 100
    print ("You have delt 100 dam to the enemy. Enemy health =")
    print enemy
else:
    print("You mistyped and your spell fizzled")
    print("Your turn is starting")
time.sleep(2)
if wizard== "Fire" or wizard== "fire":
    print("You have flame spark, fire cat and fire elf in your spell deck")
elif wizard== "Ice" or wizard== "ice":
    print("You have ice shard, frost beetle, and snow serpent in your spell deck")
elif wizard== "Life" or wizard== "life":
                            print("You have life beam, imp, and leprechaun in your spell deck")
elif wizard== "Death" or wizard== "death":
    print("You have death blast, dark pixie, ghoul in your spell deck")
elif wizard== "Myth" or wizard== "myth":
    print("You have myth blast, blood bat, and troll in your spell deck")
elif wizard== "Storm" or wizard== "storm":
    print("You have lightning spark, storm snake, and lightning bat in your spell deck")
elif wizard== "Balance" or wizard== "balance":
    print("You have balance beam, scarab, and scorpion in your spell deck")
else:
    print("Because you picked an invalid class you cannot continue the game, please reload the page")
spell= raw_input("Enter your spell (please use only lowercase):")
if spell== "flame spark" or spell== "ice shard" or spell== "life beam" or spell== "death blast" or spell== "myth blast" or spell== "lightning spark" or spell== "balance beam":
    enemy = enemy - 60
    print ("You have delt 60 dam to the enemy. Enemy health =")
    print enemy
elif spell== "storm snake":
    enemy = enemy -130
    print ("You have delt 130 dam to the enemy. Enemy health =")
    print enemy
elif spell== "fire cat": 
    enemy = enemy -120
    print ("You have delt 120 dam to the enemy. Enemy health =")
    print enemy
elif spell== "blood bat":
    enemy = enemy -110
    print ("You have delt 110 dam to the enemy. Enemy health =")
    print enemy
elif spell== "fire elf":
    enemy = enemy- 220
    print("You have delt 220 dam to the enemy. Enemy helath =")
    print enemy
elif spell== "pixie":
    if pixie <= 0:
        print("sorry you are out of pixies and you have fizzled")
    else:
        character = character + 300
        pixie = pixie - 2
        print("You have healed yourself, your health =")
        print character
elif spell== ("lightning bat"):
    enemy = enemy -240
    print("You have delt 240 dam to the enemy. Enemy health =")
    print enemy
elif spell== ("troll"):
    enemy = enemy - 200
    print("You have delt 200 dam to the enemy. Enemy health =")
    print enemy
elif spell== ("ghoul"):
    enemy = enemy -160
    character = character + 80
    print("You have delt 160 dam the enemy and restored 80 health to your self.")
    time.sleep(4)
    print("Enemy health = " + enemy)
    time.sleep(2)
    print("Your health = " + character)
    time.sleep(2)
elif spell== ("snow serpent") or spell== ("leprachaun") or spell== ("scorpion"):
    enemy = enemy -190
    print("You have del 190 dam to the enemy. Enemy health =")
    print enemy
elif spell== "frost beetle" or spell== "dark pixie" or spell== "imp" or spell== "scarab":
    enemy = enemy - 100
    print ("You have delt 100 dam to the enemy. Enemy health =")
    print enemy
else:
    print("You mistyped and your spell fizzled")