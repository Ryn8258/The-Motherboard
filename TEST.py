    print("Your turn is starting")                                                                                                  #turn 2 battle 3
    time.sleep(2)
    if wizard== "Fire" or wizard== "fire":
        print("You have flame spark, fire cat, fire elf, and sun bird in your spell deck")
    elif wizard== "Ice" or wizard== "ice":
        print("You have ice shard, frost beetle, snow serpent, and evil snowman in your spell deck")
    elif wizard== "Life" or wizard== "life":
        print("You have life beam, imp, leprechaun, and seraph in your spell deck")
    elif wizard== "Death" or wizard== "death":
        print("You have death blast, dark pixie, ghoul, and banshee your spell deck")
    elif wizard== "Myth" or wizard== "myth":
        print("You have myth blast, blood bat, troll, and cyclops in your spell deck")
    elif wizard== "Storm" or wizard== "storm":
        print("You have lightning spark, storm snake, lightning bat, and storm shark in your spell deck")
    elif wizard== "Balance" or wizard== "balance":
        print("You have balance beam, scarab, scorpion, sandstorm in your spell deck")
    else:
        print("Because you picked an invalid class you cannot continue the game, please reload the page")
    time.sleep(4)
    if pixie >= 0:
        print("you have" + pixie + "pixies")
    else:
        print("You have used your pixie")
    if wizard== "Fire" or wizard== "fire":
        if 
    elif wizard== "Ice" or wizard== "ice":
        print("You have ice shard, frost beetle, and snow serpent in your spell deck")
    elif wizard== "Life" or wizard== "life":
        print("You have life beam, imp, and leprechaun in your spell deck")
    elif wizard== "Death" or wizard== "death":
        print("You have death blast, dark pixie, and ghoul your spell deck")
    elif wizard== "Myth" or wizard== "myth":
        print("You have myth blast, blood bat, and troll in your spell deck")
    elif wizard== "Storm" or wizard== "storm":
        print("You have lightning spark, storm snake, and lightning bat in your spell deck")
    elif wizard== "Balance" or wizard== "balance":
        print("You have balance beam, scarab, and scorpion in your spell deck")
    else:
        print("Because you picked an invalid class you cannot continue the game, please reload the page")l
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
            character = character + 350
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
    elif spell== "evil snowman":
        if evil_snowman <= 0:
            print("sorry you are out of evil snowman and you have fizzled")
        else:
            enemy = enemy -290
            evil_snowman = evil_snowman - 2
            print("You have delt 290 dam, enemy health =")
            print enemy
    elif spell== "sun bird":
        if sun_bird <= 0:
            print("sorry you are out of sun birds and you have fizzled")
        else:
            enemy = enemy - 340
            sun_bird = sun_bird - 2
            print("You have delt 340 dam, enemy health =")
            print enemy
    elif spell== "sandstorm":
        if sandstorm <= 0:
            print("sorry you are out of evil snowman and you have fizzled")
        else:
            enemy = enemy -290
            sandstorm = sandstorm -2
            print("You have delt 290 dam, enemy health =")
            print enemy
    elif spell== "banshee":
        if banshee <= 0:
            print("sorry you are out of banshees and have fizzled")
        else:
            enemy = enemy - 290
            banshee = banshee - 2
            print("You have delt 290 dam, your enemy =")
            print enemy
    elif spell== "seraph":
        if seraph <= 0:
            print("sorry you are out of seraphs and you have fizzled")
        else:
            enemy = enemy - 290
            seraph = seraph - 2
            print("You have delt 290 dam, enemy health =")
            print enemy
    elif spell== "storm shark":
        if storm_shark <= 0:
            print("sorry you are out of storm sharks and have fizzled")
        else:
            enemy = enemy - 380
            banshee = banshee - 2
            print("You have delt 380 dam, your enemy =")
            print enemy
    elif spell== "cyclops":
        if cyclops <= 0:
            print("sorry you are out of cyclops' and you have fizzled")
        else:
            enemy = enemy - 320
            cyclops = cyclops - 2
            print("You have delt 320 dam, enemy health =")
            print enemy
    else:
        print("You mistyped and your spell fizzled")