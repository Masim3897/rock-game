import random
l=["Rock", "Scissor", "Paper"]

while True:
    ccount=0
    ucount=0
    uc = int(input('''
    Game Start...
    1 Yes
    2 No | Exit
    '''))
    if uc == 1:
        for a in range(1, 6):
            userInput = int(input('''
            1 Rock
            2 Scissor
            3 Paper
            '''))
            if userInput == 1:
                uchoice = "Rock"
            elif userInput == 2:
                uchoice = "Scissor"
            elif userInput == 3:
                uchoice = "Paper"
            Cchoice=random.choice(l)
            if Cchoice == uchoice:
                print("computer value",Cchoice)
                print("user value",uchoice)
                print("Game Draw")
                ucount = ucount+1
                ccount = ccount+1
            elif (uchoice=="Rock" and Cchoice=="Scissor") or \
                    (uchoice=="Paper" and Cchoice=="Rock") or\
                    (uchoice=="Scissor" and Cchoice=="Paper"):
                print("computer value",Cchoice)
                print("user value",uchoice)
                print("User win")
                ucount=ucount+1
            else:
                print("computer value", Cchoice)
                print("user value", uchoice)
                print("Computer Win")
                ccount=ccount + 1
        if ccount==ucount:
            print("Final Game Draw...")
            print("user score",ucount)
            print("computer score",ccount)
        elif ucount>ccount:
            print("Final user win the game...")
            print("user score", ucount)
            print("computer score", ccount)
        else:
            print("Final computer win the game...")
            print("user score", ucount)
            print("computer score", ccount)
    else:
        break