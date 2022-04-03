#Jenny Korkeamäki

import random
import rps

state = True
while state == True:

    print("Rock, paper, scissors?")
    choice = input("You choose: ").lower()

    if choice == "rock" or choice == "paper" or choice == "scissors":

        rpslist = ["rock", "paper", "scissors"]

        rchoice = random.choice(rpslist)
        print("The game picked " + rchoice + ".")

        result = rps.RockPaperScissors(choice, rchoice)

        print(result + " Try again? (Y/N)")
        cont = input().upper()
        
        if cont == "N" or cont == "Y":
            if cont == "N":
                state = False
                if state == False:
                    print("The game ended.")
            if cont == "Y":
                continue
        else:
            print("That's not valid input but we'll keep going.")
            
    else:
        print("That's not valid input.")
