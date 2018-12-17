done= True
while (done):
    import time
    import random
    def wizard_battle(): #this is the code for your turn
        print("Your turn is starting")                                                                     
        time.sleep(2)
        if wizard== "Fire" or wizard== "fire":
            print("You have flame spark, fire cat, fire elf, and sun bird in your spell deck")
        elif wizard== "Ice" or wizard== "ice":
            print("You have ice shard, frost beetle, snow serpent, and evil snowman in your spell deck")
        elif wizard== "Life" or wizard== "life":
            print("You have life beam, imp, leprechaun and seraphin your spell deck")
        elif wizard== "Death" or wizard== "death":
            print("You have death blast, dark pixie, ghou, and banshee in your spell deck")
        elif wizard== "Myth" or wizard== "myth":
            print("You have myth blast, blood bat, troll, and cyclops in your spell deck")
        elif wizard== "Storm" or wizard== "storm":
            print("You have lightning spark, storm snake, lightning bat, and storm shark in your spell deck")
        elif wizard== "Balance" or wizard== "balance":
            print("You have balance beam, scarab, scorpion, and sandstorm in your spell deck")
        else:
            print("Because you picked an invalid class you cannot continue the game, please reload the page")
        time.sleep(4)
        if pixie >= 1:
            print("you have" + pixie / 2 + "pixies")
        else:
            print("You have already used your pixie and have fizzled")
        if wizard== "Fire" or wizard== "fire":
            if sun_bird >= 1:
                print("You have" + sun_bird / 2 + "sunbirds left")
            else:
                print("You have no sunbirds left")
        elif wizard== "Ice" or wizard== "ice":
            if evil_snowman >= 1:
                print("You have" + evil_snowman / 2 + "evil snowmans left")
            else:
                print("You have no evil snowmans left")
        elif wizard== "Life" or wizard== "life":
            if seraph >= 1:
                print("You have" + seraph / 2 + "seraphs left")
            else:
                print("You have no seraphs left")
        elif wizard== "Death" or wizard== "death":
            if banshee >= 1:
                print("You have" + banshee / 2 + "banshees left")
            else:
                print("You have no banshees left")
        elif wizard== "Myth" or wizard== "myth":
            if cyclops >= 1:
                print("You have" + cyclops / 2 + "cyclops's left")
            else:
                print("You have no cyclops's left")
        elif wizard== "Storm" or wizard== "storm":
            if storm_shark >= 1:
                print("You have" + storm_shark / 2 + "storm sharks left")
            else:
                print("You have no storm sharks left")
        elif wizard== "Balance" or wizard== "balance":
            if sandstorm >= 1:
                print("You have" + sandstorm / 2 + "sandstorms left")
            else:
                print("You have no sandstorms left")
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
            if pixie <= 1:
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
            if evil_snowman <= 1:
                print("sorry you are out of evil snowman and you have fizzled")
            else:
                enemy = enemy -290
                evil_snowman = evil_snowman - 2
                print("You have delt 290 dam, enemy health =")
                print enemy
        elif spell== "sun bird":
            if sun_bird <= 1:
                print("sorry you are out of sun birds and you have fizzled")
            else:
                enemy = enemy - 340
                sun_bird = sun_bird - 2
                print("You have delt 340 dam, enemy health =")
                print enemy
        elif spell== "sandstorm":
            if sandstorm <= 1:
                print("sorry you are out of evil snowman and you have fizzled")
            else:
                enemy = enemy -290
                sandstorm = sandstorm -2
                print("You have delt 290 dam, enemy health =")
                print enemy
        elif spell== "banshee":
            if banshee <= 1:
                print("sorry you are out of banshees and have fizzled")
            else:
                enemy = enemy - 290
                banshee = banshee - 2
                print("You have delt 290 dam, your enemy =")
                print enemy
        elif spell== "seraph":
            if seraph <= 1:
                print("sorry you are out of seraphs and you have fizzled")
            else:
                enemy = enemy - 290
                seraph = seraph - 2
                print("You have delt 290 dam, enemy health =")
                print enemy
        elif spell== "storm shark":
            if storm_shark <= 1:
                print("sorry you are out of storm sharks and have fizzled")
            else:
                enemy = enemy - 380
                banshee = banshee - 2
                print("You have delt 380 dam, your enemy =")
                print enemy
        elif spell== "cyclops":
            if cyclops <= 1:
                print("sorry you are out of cyclops' and you have fizzled")
            else:
                enemy = enemy - 320
                cyclops = cyclops - 2
                print("You have delt 320 dam, enemy health =")
                print enemy
        else:
            print("You mistyped and your spell fizzled")
