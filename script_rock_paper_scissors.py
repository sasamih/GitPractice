from random import randint

#create a list of options
t = ["Rock", "Papir", "Makaze"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False

while True:
    player = input("Kamen, Papir, Makaze?")

    if player == computer:
        print("Tie!")
    elif player == "Kamen":
        if computer == "Papir":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Papir":
        if computer == "Makaze":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Makaze":
        if computer == "Kamen":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    
    computer = t[randint(0,2)]

    while(True):
        play_again = input("Yes, No?")
        if play_again == "Yes":
            player = False
            break
        elif play_again == "No":
            player = True
            break
        else:
            print("That's not a valid play. Check your spelling!")

    if player == True:
        break
