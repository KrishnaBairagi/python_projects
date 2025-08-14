from logo import logo
print(logo)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("You're at a crossroad, where do you want to go?\n type 'left' or 'right'.\n").lower()

if choice1 == "left":
        choice2 = input("You've come to a lake. there is a island in the middle of the lake.\nType 'wait' to wait for a boat.\n Type 'swim' to swim across\n").lower()

        if choice2 == "wait":
                choice3=input("You arrive at the island safely.\nThere is house with 3 doors.\nOne yellow, one blue & one red.\nWhich colour do you choose?\n").lower()

                if choice3 == "red":
                        print("It's a room full of fire. Game over!")

                elif choice3 == "yellow":
                        print("Congratulations!. You found the treasure. You win!")

                elif choice3 == "blue":
                        print("You enter a room of beasts. Game over!")

                else:
                        print("You chose a door that doesn't exist. Game over!")

        else:
                print("You got attacked by an angry trout. Game over!")


else:
        print("You fell in to a hole. Game over!")
  
