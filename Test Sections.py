
done3= True
while (done3):
    import time
    wizard = "life"
    person = "john"
    print("You have received a Sturdy Helm for defeating a lost soul, it will give you + 75 max health")
    time.sleep(5)
    print("Your health has been returned to MAX")
    time.sleep(3.2)
    character = 600                                                                                                                #change this number to whatever the health was before the last battle, i think it was 600
    sturdy_helm = 75
    character = character + sturdy_helm
    print("Your character now has" + character + "health")
    time.sleep(3.7)
    print("You continue on down the alley, to the Hedge Maze, in Unicorn Way")
    time.sleep(4.5)
    print("Lady Oriel greets you" + person + "She thanks you for your service")
    time.sleep(5)
    print("Lad Oriel says" + person + "I need you to search three bone cages along the alley, I believe that they have something to do with the brainwashings.")
    time.sleep(9)
    print("You walk along the alley and search the cages, looking for clues")
    time.sleep(4)
    print("In one of the cages you find a gold coin and and an enchanted piece of paper. You pick them up.")
    time.sleep(5)
    print("You return to Lady Oriel and tell her what you discovered, you also show her the gold coin, and paper")
    time.sleep(6)
    print("Lady Oriel tells you that the coin is worth one hundred dollars in the market, and she says that paper can be made into a healing spell")
    time.sleep(9)
    money = 100
    print("She takes the paper and performs some magic")
    time.sleep(3)
    print("Lady Oriel hands you the spell, it is a pixie, which will heal you for 350 health. But you can only use it once per battle.")
    pixie = 1
    time.sleep(4.5)
    print("For your good work, Lady Oriel advises you to visit the shop")
    time.sleep(4)
    print("You leave the Hedge Maze")
    time.sleep(3)
    shop = raw_input("Would u like to travel to the shop(yes or no)")
    time.sleep(2)
    if shop== ("yes") or shop== ("y") or shop== ("Yes"):
        print("Traveling to shop...")
        time.sleep(3)
        print("All items in the shop cost 100 dollars or less (right now). If you enter but you don't want to buy press enter without typing anything. The shop has a Sturdy Helm($75), Studry Chestplate($100, Long Leggings($50), or Big Boots ($25)")
        time.sleep(14)
        item = raw_input("What would you like to buy?")
        time.sleep(2)
        if item== ("Sturdy Helm"):
            print("Yeet you already have that, so you wasted 75 dollars lol")
            money = money - 75
            time.sleep(4)
            print("You have" + money + "dollars remaining")
            time.sleep(3)
        elif item== ("Sturdy Chestplate"):
            money = money - 100
            character = character + 100
            print ("You have bought Sturdy Chestplate for $100")
            time.sleep(4)
            print ("You have" + money + "dollars remaing")
            time.sleep(3.4)
            print ("You now have" + character + "health")
            time.sleep(3)
        elif item== ("Long Leggings"):
            money = money - 50
            character = character + 50
            print("You have bought Long Leggings for $50")
            time.sleep(3.4)
            print("You have" + money + "money remaining")
            time.sleep(3)
            print("You now have" + character + "health")
            time.sleep(3)
        elif item== ("Big Boots"):
            money = money -25
            character = character + 25
            print("You have bought Bib Boots for $25")
            time.sleep(3)
            print("You have" + money + "money remaining")
            time.sleep(3)
            print("You now have" + character + "health")
            time.sleep(3)
        else:
            print("You have typed inccorectly, and will not get to use the shop this time")
            time.sleep(3)
        print("Continuing journey...")
        time.sleep(2)
    elif shop== ("no") or shop== ("n") or shop== ("No"):
        print("Continuing journey...")
        time.sleep(3)
    else:
        print("You have typed inccorectly, and will not get to use the shop this time")
        print("Continuing journey")
    print("You return to the Hedge Maze")
    time.sleep(3)
    print("Lady Oriel says" + person + ", according to your evidence, it appears that farther up the alley there is a powerful wizard who is conjouring this magic. Defeat him and the pixies will be free")
    time.sleep(12)
    print("I will leave you with a new spell to defeat such an enemy")
    time.sleep(3)
    if wizard== "Fire" or wizard== "fire":
        print("Lady Oriel has rewarded you with a Sun Bird!")
    elif wizard== "Ice" or wizard== "ice":
        print("Lady Oriel has rewarded you with a Evil Snowman!")
    elif wizard== "Life" or wizard== "life":
        print("Lady Oriel has reward you with a Seraph!")
    elif wizard== "Death" or wizard== "death":
        print("Lady Oriel has rewarded you with a Banshee")
    elif wizard== "Myth" or wizard== "myth":
        print("Lady Oriel has rewarded you with a Cyclops")
    elif wizard== "Storm" or wizard== "storm":
        print("Lady Oriel has rewarded you with a Storm Shark")
    elif wizard== "Balance" or wizard== "balance":
        print("Lady Oriel has rewarded you a Sandstorm")
    else:
        print("You picked an invalid class please restart your game")
    sun_bird= 2
    evil_snowman= 2
    seraph= 2
    banshe= 2
    cyclops= 2
    storm_shark= 2
    sandstorm= 2  
    time.sleep(4)
    print("You can currently only use this spell once per match after turn 6 but im sure in the future you'll be stronger")
    time.sleep(8.9)
    print("You make your way up the alley alone in search of this powerfull wizard. You search with the intent to kill")
    time.sleep(5)
    print("As you are walking down the alley, everything seems to get darker and darker")
    time.sleep(4.2)
    print("You since a presence amitst")
    time.sleep(3)
    print("Sudenly, when everything was almost pitch black, the only thing you could make out was a banshee conjouring dark magic") 
    time.sleep(5.3)
    print("This must be the one Lady Oriel was talking about")
    time.sleep(3.4) #type here when you are online
    print("You think I must stop him")
    time.sleep(2)
    print("You approach the banshee")
    time.sleep(2)
    print("As you approach, the banshee turns around")
    time.sleep(3)
    print("I am Lady Black Hope and I will crush you")
    time.sleep(3)
    print("Your turn is starting")                                                                                              #turn 1
    enemy = 1050
    time.sleep(2)
    if wizard== "Fire" or wizard== "fire":
        print("You have flame spark, and fire cat in your spell deck")
    elif wizard== "Ice" or wizard== "ice":
        print("You have ice shard, and frost beetle in your spell deck")
    elif wizard== "Life" or wizard== "life":
        print("You have life beam, and in your spell deck")
    elif wizard== "Death" or wizard== "death":
        print("You have death blast, and dark pixie")
    elif wizard== "Myth" or wizard== "myth":
        print("You have myth blast, and blood bat in your spell deck")
    elif wizard== "Storm" or wizard== "storm":
        print("You have lightning spark, and storm snake in your spell deck")
    elif wizard== "Balance" or wizard== "balance":
        print("You have balance beam, and scarab in your spell deck")
    else:
        print("Because you picked an invalid class you cannot continue the game, please reload the page")
    time.sleep(4)
    if pixie >= 0:
        print("you have" + pixie + "pixies")
    else:
        print("You have used your pixie")
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
    elif spell== "pixie":
        if pixie <= 0:
            print("sorry you are out of pixies and you have fizzled")
        else:
            character = character + 350
            pixie = pixie - 2
            print("You have healed yourself, your health =")
            print character
    elif spell== "frost beetle" or spell== "dark pixie" or spell== "imp" or spell== "scarab":
        enemy = enemy - 100
        print ("You have delt 100 dam to the enemy. Enemy health =")
        print enemy
    else:
        print("You mistyped and your spell fizzled")
    time.sleep(4)
    print("Lady Black Hope is starting her turn")
    time.sleep(4)
    print("Lady Black Hope uses dark pixie and deals 100 dam")
    character = character -100
    print("Your health =")
    print character
    print("Your turn is starting")                                                                                                  #turn 2 battle 3
    time.sleep(2)
    if wizard== "Fire" or wizard== "fire":
        print("You have flame spark, fire cat in your spell deck")
    elif wizard== "Ice" or wizard== "ice":
        print("You have ice shard, and frost beetle in your spell deck")
    elif wizard== "Life" or wizard== "life":
        print("You have life beam, and imp in your spell deck")
    elif wizard== "Death" or wizard== "death":
        print("You have death blast, and dark pixie your spell deck")
    elif wizard== "Myth" or wizard== "myth":
        print("You have myth blast, and blood bat in your spell deck")
    elif wizard== "Storm" or wizard== "storm":
        print("You have lightning spark, and storm snake in your spell deck")
    elif wizard== "Balance" or wizard== "balance":
        print("You have balance beam, and scarab in your spell deck")
    else:
        print("Because you picked an invalid class you cannot continue the game, please reload the page")
    time.sleep(4)
    if pixie >= 0:
        print("you have" + pixie + "pixies")
    else:
        print("You have used your pixie")
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
    elif spell== "pixie":
        if pixie <= 0:
            print("sorry you are out of pixies and you have fizzled")
        else:
            character = character + 350
            pixie = pixie - 2
            print("You have healed yourself, your health =")
            print character
    elif spell== "frost beetle" or spell== "dark pixie" or spell== "imp" or spell== "scarab":
        enemy = enemy - 100
        print ("You have delt 100 dam to the enemy. Enemy health =")
        print enemy
    else:
        print("You mistyped and your spell fizzled")
    time.sleep(4)
    print("Lady Black Hope is starting her turn")
    time.sleep(4)
    print("Lady uses dark pixie and deals 100 dam")
    character = character -100
    print("Your turn is starting")                                                                                          #turn 3 battle 3
    time.sleep(2)
    if wizard== "Fire" or wizard== "fire":
        print("You have flame spark, fire cat, and fire elf in your spell deck")
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
        print("Because you picked an invalid class you cannot continue the game, please reload the page")
    time.sleep(4)
    if pixie >= 0:
        print("you have" + pixie + "pixies")
    else:
        print("You have used your pixie")
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
    else:
        print("You mistyped and your spell fizzled")
    time.sleep(4)
    print("Lady Black Hope is starting her turn")
    time.sleep(4)
    print("Lady uses ghoul and deals 160 dam to you and heals herself for 80")
    time.sleep(3)
    character = character -100 
    enemy = enemy + 80
    print("Enemy health = " + enemy)
    time.sleep(3)
    print("Your health = " + character)                                                                                                 #the year we started this
    print("Your turn is starting")                                                                                          #turn 4 battle 3
    time.sleep(2)
    if wizard== "Fire" or wizard== "fire":
        print("You have flame spark, fire cat, and fire elf in your spell deck")
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
        print("Because you picked an invalid class you cannot continue the game, please reload the page")
    time.sleep(4)
    if pixie >= 0:
        print("you have" + pixie + "pixies")
    else:
        print("You have used your pixie")
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
    else:
        print("You mistyped and your spell fizzled")
    time.sleep(4)
    print("Lady Black Hope is starting her turn")
    time.sleep(4)
    print("Lady Black Hope uses dark pixie and deals 100 dam")
    character = character -100
    print("Your health =")
    print character
    time.sleep(3)
    print("Your turn is starting")                                                                                          #turn 5 battle 3
    time.sleep(2)
    if wizard== "Fire" or wizard== "fire":
        print("You have flame spark, fire cat, and fire elf in your spell deck")
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
        print("Because you picked an invalid class you cannot continue the game, please reload the page")
    time.sleep(4)
    if pixie >= 0:
        print("you have" + pixie + "pixies")
    else:
        print("You have used your pixie")
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
    else:
        print("You mistyped and your spell fizzled")
    time.sleep(4)
    print("Lady Black Hope is starting her turn")
    time.sleep(4)
    print("Lady Black Hope uses dark pixie and deals 100 dam")
    character = character -100
    print("Your health =")
    print character
    time.sleep(3)
    print("Your turn is starting")                                                                                                  #turn 6 battle 3
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
        if sun_bird <= 1:
            print("You have" + sun_bird / 2 + "sunbirds left")
        else:
            print("You have no sunbirds left")
    elif wizard== "Ice" or wizard== "ice":
        if evil_snowman <= 1:
            print("You have" + evil_snowman / 2 + "evil snowmans left")
        else:
            print("You have no evil snowmans left")
    elif wizard== "Life" or wizard== "life":
        if seraph <= 1:
            print("You have" + seraph / 2 + "seraphs left")
        else:
            print("You have no seraphs left")
    elif wizard== "Death" or wizard== "death":
        if banshee <= 1:
            print("You have" + banshee / 2 + "banshees left")
        else:
            print("You have no banshees left")
    elif wizard== "Myth" or wizard== "myth":
        if cyclops <= 1:
            print("You have" + cyclops / 2 + "cyclops's left")
        else:
            print("You have no cyclops's left")
    elif wizard== "Storm" or wizard== "storm":
        if storm_shark <= 1:
            print("You have" + storm_shark / 2 + "storm sharks left")
        else:
            print("You have no storm sharks left")
    elif wizard== "Balance" or wizard== "balance":
        if sandstorm <= 1:
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
        if evil_snowman <= 1:
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
    if enemy <= 0:
        print("You win!")
        done= False
        break
    else:
        time.sleep(4)
        print("Lady Black Hope is starting her turn")
        time.sleep(4)
        print("Lady uses ghoul and deals 160 dam to you and heals herself for 80")
        time.sleep(3)
        character = character -100 
        enemy = enemy + 80
        print("Enemy health = " + enemy)
        print("Your health =" + enemy)
        time.sleep(3)
        if character <= 0:
            print("You have died. Please restart your game and try again")
            done= False
            break
        else:
            print("Your turn is starting")                                                                                              #turn 7 battle 3
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
                if sun_bird <= 1:
                    print("You have" + sun_bird / 2 + "sunbirds left")
                else:
                    print("You have no sunbirds left")
            elif wizard== "Ice" or wizard== "ice":
                if evil_snowman <= 1:
                    print("You have" + evil_snowman / 2 + "evil snowmans left")
                else:
                    print("You have no evil snowmans left")
            elif wizard== "Life" or wizard== "life":
                if seraph <= 1:
                    print("You have" + seraph / 2 + "seraphs left")
                else:
                    print("You have no seraphs left")
            elif wizard== "Death" or wizard== "death":
                if banshee <= 1:
                    print("You have" + banshee / 2 + "banshees left")
                else:
                    print("You have no banshees left")
            elif wizard== "Myth" or wizard== "myth":
                if cyclops <= 1:
                    print("You have" + cyclops / 2 + "cyclops's left")
                else:
                    print("You have no cyclops's left")
            elif wizard== "Storm" or wizard== "storm":
                if storm_shark <= 1:
                    print("You have" + storm_shark / 2 + "storm sharks left")
                else:
                    print("You have no storm sharks left")
            elif wizard== "Balance" or wizard== "balance":
                if sandstorm <= 1:
                    print("You have" + sandstorm / 2 + "sandstorms left")
                else:
                    print("You have no sandstorms left")
            else:
                print("Because you picked an invalid class you cannot continue the game, please reload the page")
            time.sleep(3)
            spell= raw_input("Enter your spell (please use only lowercase):")
            time.sleep(2)
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
                if evil_snowman <= 1:
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
                if enemy <= 0:
                    print("You win!")
                    done= False
                    break
                else:
                    time.sleep(4)
                    print("Lady Black Hope is starting her turn")
                    time.sleep(4)
                    print("Lady Black Hope uses dark pixie and deals 100 dam")
                    character = character -100
                    print("Your health =")
                    print character
                    time.sleep(3)
                    if character <= 0:
                        print("You have died. Please restart your game and try again")
                        done= False
                        break
                    else:
                        print("Your turn is starting")                                                                                  #turn 8 battle 3
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
                            if sun_bird <= 1:
                                print("You have" + sun_bird / 2 + "sunbirds left")
                            else:
                                print("You have no sunbirds left")
                        elif wizard== "Ice" or wizard== "ice":
                            if evil_snowman <= 1:
                                print("You have" + evil_snowman / 2 + "evil snowmans left")
                            else:
                                print("You have no evil snowmans left")
                        elif wizard== "Life" or wizard== "life":
                            if seraph <= 1:
                                print("You have" + seraph / 2 + "seraphs left")
                            else:
                                print("You have no seraphs left")
                        elif wizard== "Death" or wizard== "death":
                            if banshee <= 1:
                                print("You have" + banshee / 2 + "banshees left")
                            else:
                                print("You have no banshees left")
                        elif wizard== "Myth" or wizard== "myth":
                            if cyclops <= 1:
                                print("You have" + cyclops / 2 + "cyclops's left")
                            else:
                                print("You have no cyclops's left")
                        elif wizard== "Storm" or wizard== "storm":
                            if storm_shark <= 1:
                                print("You have" + storm_shark / 2 + "storm sharks left")
                            else:
                                print("You have no storm sharks left")
                        elif wizard== "Balance" or wizard== "balance":
                            if sandstorm <= 1:
                                print("You have" + sandstorm / 2 + "sandstorms left")
                            else:
                                print("You have no sandstorms left")
                        else:
                            print("Because you picked an invalid class you cannot continue the game, please reload the page")
                        time.sleep(3)
                        spell= raw_input("Enter your spell (please use only lowercase):")
                        time.sleep(2)
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
                            if evil_snowman <= 1:
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
                        if enemy <= 0:
                            print("You win!")
                            done= False
                            break
                        else:
                            time.sleep(4)
                            print("Lady Black Hope is starting her turn")
                            time.sleep(4)
                            print("Lady Black Hope uses dark pixie and deals 100 dam")
                            character = character -100
                            print("Your health =")
                            print character
                            time.sleep(3)
                            if character <= 0:
                                print("You have died. Please restart your game and try again")
                                done= False
                                break
                            else:
                                print("Your turn is starting")                                                                                              #turn 9 battle 3
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
                                    if sun_bird <= 1:
                                        print("You have" + sun_bird / 2 + "sunbirds left")
                                    else:
                                        print("You have no sunbirds left")
                                elif wizard== "Ice" or wizard== "ice":
                                    if evil_snowman <= 1:
                                        print("You have" + evil_snowman / 2 + "evil snowmans left")
                                    else:
                                        print("You have no evil snowmans left")
                                elif wizard== "Life" or wizard== "life":
                                    if seraph <= 1:
                                        print("You have" + seraph / 2 + "seraphs left")
                                    else:
                                        print("You have no seraphs left")
                                elif wizard== "Death" or wizard== "death":
                                    if banshee <= 1:
                                        print("You have" + banshee / 2 + "banshees left")
                                    else:
                                        print("You have no banshees left")
                                elif wizard== "Myth" or wizard== "myth":
                                    if cyclops <= 1:
                                        print("You have" + cyclops / 2 + "cyclops's left")
                                    else:
                                        print("You have no cyclops's left")
                                elif wizard== "Storm" or wizard== "storm":
                                    if storm_shark <= 1:
                                        print("You have" + storm_shark / 2 + "storm sharks left")
                                    else:
                                        print("You have no storm sharks left")
                                elif wizard== "Balance" or wizard== "balance":
                                    if sandstorm <= 1:
                                        print("You have" + sandstorm / 2 + "sandstorms left")
                                    else:
                                        print("You have no sandstorms left")
                                else:
                                    print("Because you picked an invalid class you cannot continue the game, please reload the page")
                                time.sleep(3)
                                spell= raw_input("Enter your spell (please use only lowercase):")
                                time.sleep(2)
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
                                    if evil_snowman <= 1:
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
                                        print("Sorry, you are out of cyclops' and you have fizzled")
                                    else:
                                        enemy = enemy - 320
                                        cyclops = cyclops - 2
                                        print("You have delt 320 dam, enemy health =")
                                        print enemy
                                else:
                                    print("You mistyped and your spell fizzled")
                                    if enemy <= 0:
                                        print("You win! Enemy Defeated!")
                                        done= False
                                        break
                                    else:
                                        time.sleep(4)
                                        print("Lady Black Hope is starting her turn")
                                        time.sleep(4)
                                        print("Lady Black Hope uses ghoul and deals 160 dam")
                                        character = character -160
                                        enemy = enemy + 80
                                        print("Your health =")
                                        print character
                                        print("Enemy health =")
                                        print enemy
                                        time.sleep(3)
                                        if character <= 0:
                                            print("You have died. Please restart your game and try again")
                                            done= False
                                            break
                                        else:
                                            print("Your turn is starting")                                                                                              #turn 10 battle 3
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
                                                if sun_bird <= 1:
                                                    print("You have" + sun_bird / 2 + "sunbirds left")
                                                else:
                                                    print("You have no sunbirds left")
                                            elif wizard== "Ice" or wizard== "ice":
                                                if evil_snowman <= 1:
                                                    print("You have" + evil_snowman / 2 + "evil snowmans left")
                                                else:
                                                    print("You have no evil snowmans left")
                                            elif wizard== "Life" or wizard== "life":
                                                if seraph <= 1:
                                                    print("You have" + seraph / 2 + "seraphs left")
                                                else:
                                                    print("You have no seraphs left")
                                            elif wizard== "Death" or wizard== "death":
                                                if banshee <= 1:
                                                    print("You have" + banshee / 2 + "banshees left")
                                                else:
                                                    print("You have no banshees left")
                                            elif wizard== "Myth" or wizard== "myth":
                                                if cyclops <= 1:
                                                    print("You have" + cyclops / 2 + "cyclops's left")
                                                else:
                                                    print("You have no cyclopses left")
                                            elif wizard== "Storm" or wizard== "storm":
                                                if storm_shark <= 1:
                                                    print("You have" + storm_shark / 2 + "storm sharks left")
                                                else:
                                                    print("You have no storm sharks left")
                                            elif wizard== "Balance" or wizard== "balance":
                                                if sandstorm <= 1:
                                                    print("You have" + sandstorm / 2 + "sandstorms left")
                                                else:
                                                    print("You have no sandstorms left")
                                            else:
                                                print("Because you picked an invalid class you cannot continue the game, please reload the page")
                                            time.sleep(3)
                                            spell= raw_input("Enter your spell (please use only lowercase):")
                                            time.sleep(2)
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
                                                    print("Sorry you are out of pixies, and your spell has fizzled")
                                                else:
                                                    character = character + 350
                                                    pixie = pixie - 2
                                                    print("You have healed yourself, your health =")
                                                    print character
                                            elif spell== ("lightning bat"):
                                                enemy = enemy -240
                                                print("You have dealt 240 dam to the enemy. Enemy health =")
                                                print enemy
                                            elif spell== ("troll"):
                                                enemy = enemy - 200
                                                print("You have dealt 200 dam to the enemy. Enemy health =")
                                                print enemy
                                            elif spell== ("ghoul"):
                                                enemy = enemy -160
                                                character = character + 80
                                                print("You have dealt 160 dam the enemy and restored 80 health to your self.")
                                                time.sleep(4)
                                                print("Enemy health = " + enemy)
                                                time.sleep(2)
                                                print("Your health = " + character)
                                                time.sleep(2)
                                            elif spell== ("snow serpent") or spell== ("leprachaun") or spell== ("scorpion"):
                                                enemy = enemy -190
                                                print("You have dealt 190 dam to the enemy. Enemy health =")
                                                print enemy
                                            elif spell== "frost beetle" or spell== "dark pixie" or spell== "imp" or spell== "scarab":
                                                enemy = enemy - 100
                                                print ("You have dealt 100 dam to the enemy. Enemy health =")
                                                print enemy
                                            elif spell== "evil snowman":
                                                if evil_snowman <= 1:
                                                    print("Sorry, you are out of evil snowman and you have fizzled")
                                                else:
                                                    enemy = enemy -290
                                                    evil_snowman = evil_snowman - 2
                                                    print("You have dealt 290 dam, enemy health =")
                                                    print enemy
                                            elif spell== "sun bird":
                                                if sun_bird <= 0:
                                                    print("Sorry, you are out of sun birds and you have fizzled")
                                                else:
                                                    enemy = enemy - 340
                                                    sun_bird = sun_bird - 2
                                                    print("You have dealt 340 dam, enemy health =")
                                                    print enemy
                                            elif spell== "sandstorm":
                                                if sandstorm <= 1:
                                                    print("Sorry, you are out of evil snowman and you have fizzled")
                                                else:
                                                    enemy = enemy -290
                                                    sandstorm = sandstorm -2
                                                    print("You have dealt 290 dam, enemy health =")
                                                    print enemy
                                            elif spell== "banshee":
                                                if banshee <= 1:
                                                    print("Sorry, you are out of banshees and have fizzled")
                                                else:
                                                    enemy = enemy - 290
                                                    banshee = banshee - 2
                                                    print("You have dealt 290 dam, your enemy =")
                                                    print enemy
                                            elif spell== "seraph":
                                                if seraph <= 1:
                                                    print("Sorry, you are out of seraphs and you have fizzled")
                                                else:
                                                    enemy = enemy - 290
                                                    seraph = seraph - 2
                                                    print("You have dealt 290 dam, enemy health =")
                                                    print enemy
                                            elif spell== "storm shark":
                                                if storm_shark <= 1:
                                                    print("sorry you are out of storm sharks and have fizzled")
                                                else:
                                                    enemy = enemy - 380
                                                    banshee = banshee - 2
                                                    print("You have dealt 380 dam, your enemy =")
                                                    print enemy
                                            elif spell== "cyclops":
                                                if cyclops <= 1:
                                                    print("Sorry, you are out of cyclops' and you have fizzled")
                                                else:
                                                    enemy = enemy - 320
                                                    cyclops = cyclops - 2
                                                    print("You have dealt 320 dam, enemy health =")
                                                    print enemy
                                            else:
                                                print("You mistyped and your spell fizzled")
                                                if enemy <= 0:
                                                    print("You win!")
                                                    done= False
                                                    break
                                                else:
                                                    time.sleep(4)
                                                    print("Lady Black Hope is starting her turn")
                                                    time.sleep(4)
                                                    print("Lady Black Hope wails, your end is near")
                                                    time.sleep(3)
                                                    print("Lady Black Hope uses banshee and deals 290 dam")
                                                    time.sleep(3)
                                                    character = character -290
                                                    print("Your health =")
                                                    print character
                                                    time.sleep(3)
                                                    if character <= 0:
                                                        print("You have died. Please restart your game and try again")
                                                        done= False
                                                        break
                                                    else:
                                                        print("Your turn is starting")                                                                                              #turn 11 battle 3
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
                                                            if sun_bird <= 1:
                                                                print("You have" + sun_bird / 2 + "sunbirds left")
                                                            else:
                                                                print("You have no sunbirds left")
                                                        elif wizard== "Ice" or wizard== "ice":
                                                            if evil_snowman <= 1:
                                                                print("You have" + evil_snowman / 2 + "evil snowmans left")
                                                            else:
                                                                print("You have no evil snowmans left")
                                                        elif wizard== "Life" or wizard== "life":
                                                            if seraph <= 1:
                                                                print("You have" + seraph / 2 + "seraphs left")
                                                            else:
                                                                print("You have no seraphs left")
                                                        elif wizard== "Death" or wizard== "death":
                                                            if banshee <= 1:
                                                                print("You have" + banshee / 2 + "banshees left")
                                                            else:
                                                                print("You have no banshees left")
                                                        elif wizard== "Myth" or wizard== "myth":
                                                            if cyclops <= 1:
                                                                print("You have" + cyclops / 2 + "cyclops's left")
                                                            else:
                                                                print("You have no cyclops's left")
                                                        elif wizard== "Storm" or wizard== "storm":
                                                            if storm_shark <= 1:
                                                                print("You have" + storm_shark / 2 + "storm sharks left")
                                                            else:
                                                                print("You have no storm sharks left")
                                                        elif wizard== "Balance" or wizard== "balance":
                                                            if sandstorm <= 1:
                                                                print("You have" + sandstorm / 2 + "sandstorms left")
                                                            else:
                                                                print("You have no sandstorms left")
                                                        else:
                                                            print("Because you picked an invalid class you cannot continue the game, please reload the page")
                                                        time.sleep(3)
                                                        spell= raw_input("Enter your spell (please use only lowercase):")
                                                        time.sleep(2)
                                                        if spell== "flame spark" or spell== "ice shard" or spell== "life beam" or spell== "death blast" or spell== "myth blast" or spell== "lightning spark" or spell== "balance beam":
                                                            enemy = enemy - 60
                                                            print ("You have dealt 60 dam to the enemy. Enemy health =")
                                                            print enemy
                                                        elif spell== "storm snake":
                                                            enemy = enemy -130
                                                            print ("You have dealt 130 dam to the enemy. Enemy health =")
                                                            print enemy
                                                        elif spell== "fire cat": 
                                                            enemy = enemy -120
                                                            print ("You have dealt 120 dam to the enemy. Enemy health =")
                                                            print enemy
                                                        elif spell== "blood bat":
                                                            enemy = enemy -110
                                                            print ("You have dalt 110 dam to the enemy. Enemy health =")
                                                            print enemy
                                                        elif spell== "fire elf":
                                                            enemy = enemy- 220
                                                            time.sleep(2)
                                                            print("You have dealt 220 dam to the enemy. Enemy helath =")
                                                            print enemy
                                                        elif spell== "pixie":
                                                            if pixie <= 0:
                                                                print("Sorry, you are out of pixies and you have fizzled")
                                                            else:
                                                                character = character + 350
                                                                pixie = pixie - 2
                                                                print("You have healed yourself, your health =")
                                                                print character
                                                        elif spell== ("lightning bat"):
                                                            enemy = enemy -2
                                                            40
                                                            print("You have delt 240 dam to the enemy. Enemy health =")
                                                            print enemy
                                                        elif spell== ("troll"):
                                                            enemy = enemy - 200
                                                            print("You have dealt 200 dam to the enemy. Enemy health =")
                                                            print enemy
                                                        elif spell== ("ghoul"):
                                                            enemy = enemy -160
                                                            character = character + 80
                                                            print("You have dealt 160 dam the enemy and restored 80 health to your self.")
                                                            time.sleep(4)
                                                            print("Enemy health = " + enemy)
                                                            time.sleep(2)
                                                            print("Your health = " + character)
                                                            time.sleep(2)
                                                        elif spell== ("snow serpent") or spell== ("leprachaun") or spell== ("scorpion"):
                                                            enemy = enemy -190
                                                            print("You have dealt 190 dam to the enemy. Enemy health =")
                                                            print enemy
                                                        elif spell== "frost beetle" or spell== "dark pixie" or spell== "imp" or spell== "scarab":
                                                            enemy = enemy - 100
                                                            print ("You have dealt 100 dam to the enemy. Enemy health =")
                                                            print enemy
                                                        elif spell== "evil snowman":
                                                            if evil_snowman <= 1:
                                                                print("Sorry, you are out of evil snowman and you have fizzled")
                                                            else:
                                                                enemy = enemy -290
                                                                evil_snowman = evil_snowman - 2
                                                                print("You have dealt 290 dam, enemy health =")
                                                                print enemy
                                                        elif spell== "sun bird":
                                                            if sun_bird <= 0:
                                                                print("Sorry, you are out of sun birds and you have fizzled")
                                                            else:
                                                                enemy = enemy - 340
                                                                sun_bird = sun_bird - 2
                                                                print("You have dealt 340 dam, enemy health =")
                                                                print enemy
                                                        elif spell== "sandstorm":
                                                            if sandstorm <= 1:
                                                                print("sorry you are out of evil snowman and you have fizzled")
                                                            else:
                                                                enemy = enemy -290
                                                                sandstorm = sandstorm -2
                                                                print("You have dealt 290 dam, enemy health =")
                                                                print enemy
                                                        elif spell== "banshee":
                                                            if banshee <= 1:
                                                                print("Sorry, you are out of banshees and have fizzled")
                                                            else:
                                                                enemy = enemy - 290
                                                                banshee = banshee - 2
                                                                print("You have dealt 290 dam, your enemy =")
                                                                print enemy
                                                        elif spell== "seraph":
                                                            if seraph <= 1:
                                                                print("Sorry, you are out of seraphs and you have fizzled")
                                                            else:
                                                                enemy = enemy - 290
                                                                seraph = seraph - 2
                                                                print("You have dealt 290 dam, enemy health =")
                                                                print enemy
                                                        elif spell== "storm shark":
                                                            if storm_shark <= 1:
                                                                print("Sorry, you are out of storm sharks and have fizzled")
                                                            else:
                                                                enemy = enemy - 380
                                                                banshee = banshee - 2
                                                                print("You have dealt 380 dam, your enemy =")
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
                                                            if enemy <= 0:
                                                                print("You win!")
                                                                done= False
                                                                break
                                                            else:
                                                                time.sleep(4)
                                                                print("Lady Black Hope is starting her turn")
                                                                time.sleep(2)
                                                                print("Lady Black Hope wails, your end is near")
                                                                time.sleep(4)
                                                                print("Lady Black Hope uses banshee deals 290 dam")
                                                                character = character -100
                                                                print("Your health =")
                                                                print character
                                                                time.sleep(3)
                                                                if character <= 0:
                                                                    print("You have died. Please restart your game and try again")
                                                                    done= False
                                                                    break