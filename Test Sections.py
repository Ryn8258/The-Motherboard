done3= True
while (done3):
    import time
    print("You have received a Sturdy Helm for defeating a lost soul, it will give you + 75 max health")
    time.sleep(5)
    print("Your health has been returned to MAX")
    time.sleep(3.2)
    N_A = 0
    character = 600                                                                                                                #change this number to whatever the health was before the last battle, i think it was 600
    sturdy_helm = 75
    helm = sturdy_helm
    character = character + helm
    chestplate = N_A
    leggings = N_A
    boots = N_A
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
    copper_helm = 175
    bronze_helm = 275
    silver_helm = 375
    gold_helm = 475
    enchanted_helm = 575
    sturdy_chestplate = 100
    copper_chestplate = 200
    bronze_chestplate = 300
    silver_chestplate = 400
    gold_chestplate = 500
    enchanted_chestplate = 600
    sturdy_leggings =  50
    copper_leggings = 150
    bronze_leggings = 250
    silver_leggings = 350
    gold_leggings = 450
    enchanted_leggings = 550
    sturdy_boots = 25
    copper_boots = 125
    bronze_boots = 225
    silver_boots = 325
    gold_boots = 425
    enchanted_boots = 525
    print("She takes the paper and performs some magic")
    time.sleep(3)
    print("Lady Oriel hands you the spell, it is a pixie, which will heal you for 350 health. But you can only use it once per battle.")
    pixie = 2
    time.sleep(4.5)
    print("For your good work, Lady Oriel advises you to visit the shop")
    time.sleep(4)
    print("You leave the Hedge Maze")
    time.sleep(3)
    shoptravel = raw_input("Would u like to travel to the shop(yes or no)")
    time.sleep(2)
    if shoptravel== ("yes") or shop== ("y") or shop== ("Yes"):
        print("Traveling to shop...")
        time.sleep(3)
        print("Your money =")
        print money
        time.sleep(2)
        print("If you visit the shop but you don't want to buy anything, press enter without typing anything. The shop has a sturdy(75), copper(175), bronze(275), silver(375), gold(475), and enchanted helm(575). It has a sturdy(100), copper(200), bronze(300), silver(400), gold(500), and enchanted chestplate(600).. It has sturdy(50), copper(150), bronze(250), silver(350), gold(450), and enchanted leggins(550).. It has sturdy(25), copper(125), bronze(225), silver(325), gold(425), and enchanted boots(525)..")
        time.sleep(28)
        raw_input("You may buy 1 item at a time. What would you like to buy?")
        time.sleep(2)
        if raw_input== ("sturdy helm"):
            if money >= 75:
                if helm== 75:
                    print("You already own this item, and you will not get to purchase this time")
                elif helm >= 75:
                    print("You own a better item, and will not got to purchase this time")
                else:
                    helm = sturdy_helm
                    character = character - sturdy_helm
                    character = character + sturdy_helm
                    money = money - helm
                    print("You now have" + character + "health")
                    print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        elif raw_input== ("copper helm"):
            if money >= 175:
                if helm== 175:
                    print("You alreardy own this item, and will not get to purchase this time")
                elif helm >=175:
                    print("You own a better item, and will not get to purchase this time")
                else:
                    character = character - helm
                    helm = copper_helm
                    character = character + helm
                    money = money - helm
                    print("You now have" + character + "health")
                    print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        elif raw_input== ("bronze helm"):
            if money >= 275:
                if helm== 275:
                    print("You already own this item, and will not get to purhcase this time")
                elif helm >= 275:
                    print("You own a better item and will not be able to purchase this time")
                else:
                    character = character - helm
                    helm = bronze_helm
                    character = character + helm
                    money = money - helm
                    print("You now have" + character + "health")
                    print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        elif raw_input== ("silver helm"):
            if money >= 375: 
                if helm== 375:
                    print("You already own this item, and will not get to purchase this time")
                elif helm >= (375):
                    print("You own a better item, and will not get to purchase this time")
                else:
                    character = character - helm
                    helm = silver_helm
                    character = character + helm
                    money = money - helm
                    print("You now have" + character + "health")
                    print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        elif raw_input== ("gold helm"):
            if money >= 475:
                if helm== 475:
                    print("You already own this item, and will not get to purchase this time")
                elif helm >= 475:
                    print("You own a better item, and will not get to purchase this time")
                else:
                    character = character - helm
                    helm = gold_helm
                    character = character + helm
                    money = money - helm
                    print("You now have" + character + "health")
                    print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        elif raw_input== ("enchanted helm"):
            if money >= 575:
                if helm== 575:
                    print("You already own this item, and will not get to purchase this time")
                elif helm >= 575:
                    print("You own a better item, and will not get to purchase this time")
                else:
                    character = character - helm
                    helm = enchanted_helm
                    character = character + helm
                    money = money - helm
                    print("You now have" + character + "health")
                    print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        elif raw_input== ("sturdy chestplate"):
            if money >= 100:
                if chestplate== 100:
                    print("You already own this item, and will not get to purchase this time")
                elif chesplate >= 100:
                    print("You own a better item, and will not get to purchase this time")
                else:
                    character = character - chestplate
                    chestplate = sturdy_chestplate
                    character = character + chestplate
                    money = money - chestplate
                    print("You now have" + character + "health")
                    print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        elif raw_input== ("copper chestplate"):
            if money >= 100:
                if chestplate== 200:
                    print("You already own this item, and will not get to purchase this time")
                elif chesplate >= 200:
                    print("You own a better item, and will not get to purchase this time")
                else:
                    character = character - chestplate
                    chestplate = copper_chestplate
                    character = character + chestplate
                    money = money - chestplate
                    print("You now have" + character + "health")
                    print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        elif raw_input== ("bronze chestplate"):
            if money >= 300:
                if chestplate== 300:
                    print("You already own this item, and will not get to purchase this time")
                elif chesplate >= 300:
                    print("You own a better item, and will not get to purchase this time")
                else:
                    character = character - chestplate
                    chestplate = bronze_chestplate
                    character = character + chestplate
                    money = money - chestplate
                    print("You now have" + character + "health")
                    print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        elif raw_input== ("silver chestplate"):
            if money >= 400:
                if chestplate== 400:
                    print("You already own this item, and will not get to purchase this time")
                elif chesplate >= 400:
                    print("You own a better item, and will not get to purchase this time")
                else:
                    character = character - chestplate
                    chestplate = silver_chestplate
                    character = character + chestplate
                    money = money - chestplate
                    print("You now have" + character + "health")
                    print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        elif raw_input== ("gold chestplate"):
            if money >= 500:
                if chestplate== 500:
                    print("You already own this item, and will not get to purchase this time")
                elif chesplate >= 500:
                    print("You own a better item, and will not get to purchase this time")
                else:
                    character = character - chestplate
                    chestplate = gold_chestplate
                    character = character + chestplate
                    money = money - chestplate
                    print("You now have" + character + "health")
                    print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        elif raw_input== ("enchanted chestplate"):
            if money >= 600:
                if chestplate== 600:
                    print("You already own this item, and will not get to purchase this time")
                elif chesplate >= 600:
                    print("You own a better item, and will not get to purchase this time")
                else:
                    character = character - chestplate
                    chestplate = enchanted_chestplate
                    character = character + chestplate
                    money = money - chestplate
                    print("You now have" + character + "health")
                    print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        elif raw_input== ("sturdy leggings"):
            if money >= 50:
                if leggings== 50:
                    print("You already own this item, and will not get to purchase this time")
                elif leggings >= 50:
                    print("You own a better item, and will not get to purchase this time")
                else:
                    character = character - leggings
                    leggings = sturdy_leggings
                    character = character + leggings
                    money = money - leggings
                    print("You now have" + character + "health")
                    print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        elif raw_input== ("copper leggings"):
            if money >= 150:
                if leggings== 150:
                    print("You already own this item, and will not get to purchase this time")
                elif leggings >= 150:
                    print("You own a better item, and will not get to purchase this time")
                else:
                    character = character - leggings
                    leggings = copper_leggings
                    character = character + leggings
                    money = money - leggings
                    print("You now have" + character + "health")
                    print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        elif raw_input== ("bronze leggings"):
            if money >= 250:
                if leggings== 250:
                    print("You already own this item, and will not get to purchase this time")
                elif leggings >= 250:
                    print("You own a better item, and will not get to purchase this time")
                else:
                    character = character - leggings
                    leggings = bronze_leggings
                    character = character + leggings
                    money = money - leggings
                    print("You now have" + character + "health")
                    print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        elif raw_input== ("silver leggings"):
            if money >= 350:
                if leggings== 350:
                    print("You already own this item, and will not get to purchase this time")
                elif leggings >= 350:
                    print("You own a better item, and will not get to purchase this time")
                else:
                    character = character - leggings
                    leggings = silver_leggings
                    character = character + chestplate
                    money = money - leggings
                    print("You now have" + character + "health")
                    print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        elif raw_input== ("gold leggings"):
            if money >= 450:
                if leggings== 450:
                    print("You already own this item, and will not get to purchase this time")
                elif leggings >= 450:
                    print("You own a better item, and will not get to purchase this time")
                else:
                    character = character - leggings
                    leggings = gold_leggings
                    character = character + chestplate
                    money = money - leggings
                    print("You now have" + character + "health")
                    print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        elif raw_input== ("enchanted leggings"):
            if money >= 550:
                if leggings== 550:
                    print("You already own this item, and will not get to purchase this time")
                elif leggings >= 550:
                    print("You own a better item, and will not get to purchase this time")
                else:
                    character = character - leggings
                    leggings = enchanted_leggings
                    character = character + leggings
                    money = money - leggings
                    print("You now have" + character + "health")
                    print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        elif raw_input== ("sturdy boots"):
            if money >= 25:
                if boots== 25:
                    print("You already own this item, and will not get to purchase this time")
                elif boots >= 25:
                    print("You own a better item, and will not get to purchase this time")
                else:
                    character = character - boots
                    boots = sturdy_boots
                    character = character + boots
                    money = money - boots
                    print("You now have" + character + "health")
                    print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        elif raw_input== ("copper boots"):
            if money >= 125:
                if boots== 125:
                    print("You already own this item, and will not get to purchase this time")
                elif boots >= 125:
                    print("You own a better item, and will not get to purchase this time")
                else:
                    character = character - boots
                    boots = copper_boots
                    character = character + boots
                    money = money - boots
                    print("You now have" + character + "health")
                    print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        elif raw_input== ("bronze boots"):
            if money >= 225:
                if boots== 225:
                    print("You already own this item, and will not get to purchase this time")
                elif boots >= 225:
                    print("You own a better item, and will not get to purchase this time")
                else:
                    character = character - boots
                    boots = bronze_boots
                    character = character + boots
                    money = money - boots
                    print("You now have" + character + "health")
                    print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        elif raw_input== ("silver boots"):
            if money >= 325:
                if boots== 325:
                    print("You already own this item, and will not get to purchase this time")
                elif boots >= 325:
                    print("You own a better item, and will not get to purchase this time")
                else:
                    character = character - boots
                    boots = silver_boots
                    character = character + boots
                    money = money - boots
                    print("You now have" + character + "health")
                    print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        elif raw_input== ("gold boots"):
            if money >= 425:
                if boots== 425:
                    print("You already own this item, and will not get to purchase this time")
                elif boots >= 425:
                    print("You own a better item, and will not get to purchase this time")
                else:
                    character = character - boots
                    boots = gold_boots
                    character = character + boots
                    money = money - boots
                    print("You now have" + character + "health")
                    print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        elif raw_input== ("enchanted boots"):
            if money >= 525:
                if boots== 525:
                    print("You already own this item, and will not get to purchase this time")
                elif boots >= 525:
                    print("You own a better item, and will not get to purchase this time")
                else:
                    character = character - boots
                    boots = enchanted_boots
                    character = character + boots
                    money = money - boots
                    print("You now have" + character + "health")
                    print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        else:
            print("You have typed inccorectly, and will not get to use the shop this time")
        
            time.sleep(3)
        print("Continuing journey...")
        time.sleep(2)
    elif shoptravel== ("no") or shop== ("n") or shop== ("No"):
        print("Continuing journey...")
        time.sleep(3)
    else:
        print("You have typed inccorectly, and will not get to use the shop this time")
        print("Continuing journey...")