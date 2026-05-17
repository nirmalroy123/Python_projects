import random

game_images=[rock,paper,scissors]
user_choice=int(input("what do u choose?type 0 for rock,1 for paper or2 for scissors"))
if user_choice>=3 or user_choice<0:
    print("you typed an invalid number,you lose")
else:
    print(game_images[user_choice])
    computer_choice=random.randint(0,2)
    print("computer_choice")
    print(game_images[computer_choice])
    if user_choice==0 and computer_choice==2:
        print("you win")
    elif computer_choice==0 and user_choice==2:
        print("you lose")
    elif computer_choice>user_choice:
        print("you lose")
    elif user_choice> computer_choice:
        print("you win!")
    elif computer_choice==user_choice:
        print("its a draw")
