#Jenny Korkeamäki

def RockPaperScissors(choice, rchoice):
    if choice == rchoice:
        return "It's a tie."

    if choice == "rock" and rchoice == "scissors":
        return "You won."

    if choice == "paper" and rchoice == "rock":
        return "You won."

    if choice == "scissors" and rchoice == "paper":
        return "You won."

    else:
        return "You lost."
