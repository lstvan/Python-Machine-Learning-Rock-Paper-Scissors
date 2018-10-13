import random as r

totalRounds = 1
selection = ["rock", "paper", "scissors"]
playOpposition = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
selectionFrequency = {"rock": 1, "paper": 1, "scissors": 1}
selectionDiscriminators = {"rock": selectionFrequency["rock"] / totalRounds, "paper": selectionFrequency["paper"] / totalRounds, "scissors": selectionFrequency["scissors"] / totalRounds}

def generateSelection():
    selecteditem = r.choice(selection)
    itemdiscriminator = r.random()
    return selecteditem,itemdiscriminator

def play():
    global totalRounds
    item, discriminator = generateSelection()
    if discriminator > selectionDiscriminators[item]:
        play()
    playerselection = input("Please Enter a Choice of Rock, Paper, or Scissors. Rock|Paper|Scissors\n")
    if playerselection.lower() not in selection:
        print("Error Accounting Response")
        play()
    else:
        if playerselection == playOpposition[item]:
            print("YOU WIN!\nYou Chose:", playerselection, "\nA.I Chose:", item)
        elif (playerselection != playOpposition[item]) and (playerselection != item):
            print("YOU LOSE!\nYou Chose:", playerselection, "\nA.I Chose:", item)
        elif playerselection == item:
            print("TIE!\nYou Chose:", playerselection, "\nA.I Chose:", item)
        play()

play()