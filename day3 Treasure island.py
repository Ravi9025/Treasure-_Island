                                   # Treasure Island
  # Branch
  
  
print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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
choice1 = input('You\'re at a cross road. where do you want to go?type "left" or "right" \n').lower()

if  choice1 == "left":
    choice2 = input('You\'ve come to the lake. There is a island middle of the lake, type "wait" to wait for the boat or type "swim" to swim through the lake \n').lower()
    if choice2 == "wait":
       choice3 = input('You can go island unharmed. There is a house in there, it has three color doors.\n Thats "red" and "yellow" and "green"\n ').lower()
       if choice3 == "red":
           print("You are fall in fire: Game Over.")
       elif choice3 == "yellow":
           print("Congratulation, You got the Treasure.")
       elif choice3 == "green":
           print("You are entering to the deadly trap room: Game Over.")
       else:
           print("You choose a door does not exist: Game Over.")
    else:
        print("You are attacked by crocodiles: Game Over. ")       
else:
    choice1 == "right"
    print("you fall into the hole : Game Over")
    
    fuck
   

