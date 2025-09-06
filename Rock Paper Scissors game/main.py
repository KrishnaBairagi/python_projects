import random
from logo import Rock,Paper,Scissor
image=[Rock,Paper,Scissor]
want_to_continue=True
while want_to_continue:
    user_choice=int(input("What do you want to choose? type 0 for 'Rock', 1 for 'Paper' or 2 for 'Scissor'\n"))
    print(image[user_choice])

    computer_choice=random.randint(0,2)
    print("Computer choose: \n",image[computer_choice])

    if user_choice >= 3 or user_choice < 0:
        print("Invalid choice.... You loose!👎")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!👍")
    elif user_choice == 2 and computer_choice == 0:
        print("You loose!👎")
    elif user_choice == computer_choice:
        print("It's draw!☹️")

    elif user_choice > computer_choice:
        print('You win!👍')

    elif computer_choice > user_choice:
        print("You loose!👎")
    want_to_continue=input("Do you want to continue game: y/n \n")
    if want_to_continue == "y":
        want_to_continue=True
    elif want_to_continue == "n":
        want_to_continue=False
    else:
        print("Invalid choice")
        want_to_continue=False
  
