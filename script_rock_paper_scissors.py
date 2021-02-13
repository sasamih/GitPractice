from random import randint

#create a list of play options
t = ["Rock", "Papir", "Makaze"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False

while player == False:
#set player to True
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
    
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]
