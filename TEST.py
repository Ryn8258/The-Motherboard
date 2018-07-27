leggings= 100
character= 250
boots= 100                             # 
chestplate= 200
helm= 150
money = 999999999999
character = character + helm                           #copy over before battles
character = character + chestplate  
character = character + leggings
character = character + boots

print character
import time
def shop():
    shop = raw_input("Would u like to travel to the shop(yes or no)")
    time.sleep(2)
    if shop== ("yes") or shop== ("y") or shop== ("Yes"):
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
                helm = sturdy_helm
                character = character + helm
                money = money -helm
                print("You now have" + character + "health")
                print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        elif raw_input== ("copper helm"):
            if money >= 175:
                helm = copper_helm
                character = character + helm
                money = money -helm
                print("You now have" + character + "health")
                print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        elif raw_input== ("bronze helm"):
            if money >= 275:    
                helm = bronze_helm
                character = character + helm
                money = money -helm
                print("You now have" + character + "health")
                print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        elif raw_input== ("silver helm"):
            if money >= 375: 
                helm = silver_helm
                character = character + helm
                money = money -helm
                print("You now have" + character + "health")
                print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        elif raw_input== ("gold helm"):
            if money >= 475:
                helm = gold_helm
                character = character + helm
                money = money -helm
                print("You now have" + character + "health")
                print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        elif raw_input== ("sturdy chestplate"):
            if money >= 100:
                chestplate = sturdy_chestplate
                character = character + chestplate
                money = money -chestplate
                print("You now have" + character + "health")
                print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        elif raw_input== ("copper chestplate"):
            if money >= 200:
                chestplate = copper_chestplate
                character = character + chestplate
                money = money -chestplate
                print("You now have" + character + "health")
                print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        elif raw_input== ("bronze chestplate"):
            if money >= 300:
                chestplate = bronze_chestplate
                character = character + chestplate
                money = money -chestplate
                print("You now have" + character + "health")
                print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        elif raw_input== ("silver chestplate"):
            if money >= 400:
                chestplate = sturdy_chestplate
                character = character + chestplate
                money = money -chestplate
                print("You now have" + character + "health")
                print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        elif raw_input== ("gold chestplate"):
            if money >= 500:
                chestplate = gold_chestplate
                character = character + chestplate
                money = money -chestplate
                print("You now have" + character + "health")
                print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        elif raw_input== ("enchanted chestplate"):
            if money >= 600:
                chestplate = enchanted_chestplate
                character = character + chestplate
                money = money -chestplate
                print("You now have" + character + "health")
                print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        elif raw_input== ("sturdy leggings"):
            if money >= 50:
                leggings = sturdy_leggings
                character = character + leggings
                money = money -leggings
                print("You now have" + character + "health")
                print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        elif raw_input== ("copper leggings"):
            if money >= 150:
                leggings = copper_leggings
                character = character + leggings
                money = money -leggings
                print("You now have" + character + "health")
                print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        elif raw_input== ("bronze leggings"):
            if money >= 250:
                leggings = bronze_leggings
                character = character + leggings
                money = money -leggings
                print("You now have" + character + "health")
                print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        elif raw_input== ("silver leggings"):
            if money >= 350:
                leggings = silver_leggings
                character = character + leggings
                money = money -leggings
                print("You now have" + character + "health")
                print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        elif raw_input== ("gold leggings"):
            if money >= 450:
                leggings = gold_leggings
                character = character + leggings
                money = money -leggings
                print("You now have" + character + "health")
                print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        elif raw_input== ("enchanted leggings"):
            if money >= 550:
                leggings = enchanted_leggings
                character = character + leggings
                money = money -leggings
                print("You now have" + character + "health")
                print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        elif raw_input== ("sturdy boots"):
            if money >= 25:
                boots = sturdy_boots
                character = character + boots
                money = money -leggings
                print("You now have" + character + "health")
                print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        elif raw_input== ("copper boots"):
            if money >= 125:
                boots = copper_boots
                character = character + boots
                money = money -boots
                print("You now have" + character + "health")
                print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        elif raw_input== ("bronze boots"):
            if money >= 225:
                boots = bronze_boots
                character = character + boots
                money = money -boots
                print("You now have" + character + "health")
                print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        elif raw_input== ("silver boots"):
            if money >= 325:
                boots = silver_boots
                character = character + boots
                money = money -boots
                print("You now have" + character + "health")
                print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        elif raw_input== ("gold boots"):
            if money >= 425:
                boots = gold_boots
                character = character + boots
                money = money -boots
                print("You now have" + character + "health")
                print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        elif raw_input== ("enchanted boots"):
            if money >= 525:
                boots = enchanted_boots
                character = character + boots
                money = money -boots
                print("You now have" + character + "health")
                print("You also have" + money + "dollars remaining")
            else:
                print("You do not have enough money to purchase this item. The vendors have chased you out.")
        else:
            print("You have typed inccorectly, and will not get to use the shop this time")
        
            time.sleep(3)
        # print("Continuing journey...")
        # time.sleep(2)
    elif shop== ("no") or shop== ("n") or shop== ("No"):
        print("Continuing journey...")
        
shop()
print("done")