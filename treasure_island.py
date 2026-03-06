import waiting

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
crossRoad = input("you're at a cross road. Where do you want to go?\n    Type \"Left\" or \"right\"").lower()
if crossRoad == "right":
    print("you fall into a hole! Game Over!")
elif crossRoad == "left":
    print("you've come to a lake. There is an island in the middle of the lake.")
    waiting = input("  Type \"wait\" to wait for a boat. Type \"swim\" to swim across. ").lower()
    if waiting == "swim":
        print("you are attacked by gobind sarvar staff. Game over")
    elif waiting == "wait":
        print("you arrive at the island unharmed. And you see janat de darvaje with 3 paths")
        janat = input(" type \"yellow\", \"red\" or \"blue\" or \"white\"").lower()
        if janat == "red":
            print("you get trapped in the gurmat building! GAME OVER!")
        elif janat == "blue":
            print("you enter Mr. B's classroom and he chucks a chair across the room and hits you right in the head!")
        elif janat == "white":
            print("you get chased by Yuvi because you taxed his munchies! GAME OVER!")
        elif janat == "yellow":
            print("YOU BEAT THE ODDS YOU HAVE WON..... sike i lied you suck. SIKE AGAIN YOU ARE A WINNER AKALLL!")
