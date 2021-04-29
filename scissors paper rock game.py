import random
while True:
    choice=["scissors","paper","rock"]

    computer=random.choice(choice)
    player=None

    while player not in choice:
        player=input("scissors,paper,rock\n").lower()

    if player==computer:
        print("tie!!")
        print("computer:",computer)
        print("players:",player)
    elif player=="rock":
        if computer=="scissiors":
            print("you win!!")
            print("computer:",computer)
            print("players:",player)
        if computer=="paper":
            print("you loose!!")
            print("computer:",computer)
            print("players:",player)

    elif player=="paper":
        if computer=="scissiors":
            print("you loose!!")
            print("computer:",computer)
            print("players:",player)
        if computer=="rock":
            print("you win!!")
            print("computer:",computer)
            print("players:",player)
    elif player=="scissors":
        if computer=="paper":
            print("you win!!")
            print("computer:",computer)
            print("players:",player)
        if computer=="rock":
            print("you lose!!")
            print("computer:",computer)
            print("players:",player)
    play_again=input("play_again?? (yes/no):").lower()
    if play_again!="yes":
        break

print("bye!! thank you for playing this game")






