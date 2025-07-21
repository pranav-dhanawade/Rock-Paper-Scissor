import random
print("\n\nWelcome To Game\n\n")
print("Pick Your Choose(Write only number):")
listOfChoice={1:"Rock",2:"Paper",3:"Scissor"}
listOfBot = ['Rock','Paper','Scissor']
userScore = 0
botScore = 0
def chose(dict):
    for i in dict:
        print(i,".",dict[i])
    user = int(input("-->"))
    print("\n")
    global userChioce
    userChioce = 0
    userChioce = userChioce + user
def game(choice):
    BotChoice = random.choice(listOfBot)
    global userScore
    global botScore
    match choice:
        
        case 1:
            print(f"Your Choice = {listOfChoice[userChioce]}")
            print(f"Bot Choice= {BotChoice}\n")
            if choice==1 and BotChoice=='Scissor':
                print("You Win")
                userScore+=1
            elif choice==1  and BotChoice=='Paper':
                print("Bot Wins")
                botScore+=1
            else:
                print("Tie")
        case 2:
            print(f"Your Choice = {listOfChoice[userChioce]}")
            print(f"Bot Choice= {BotChoice}")
            if choice==2 and BotChoice=='Scissor':
                print("Bot Wins")
                botScore+=1
            elif choice==2  and BotChoice=='Rock':
                print("You Wins")
                userScore+=1
            else:
                print("Tie")
        case 3:
            print(f"Your Choice = {listOfChoice[userChioce]}")
            print(f"Bot Choice= {BotChoice}")
            if choice==3 and BotChoice=='Scissor':
                print("Tie")
            elif choice==3  and BotChoice=='Paper':
                print("You Wins")
                userScore+=1
            else:
                print("Bot Wins")
                botScore+=1
        case _:
            print("Give Correct Response..Try Again")
            play()
def again():
    print("\n1.Play Again ")
    print("2.Check Score")
    print("3.Quit")
    agn = int(input("-->"))
    print("\n")
    match agn:
        case 1:
            play()
        case 2:
            print(f"Your Score is {userScore} & Bot Score is {botScore}")
            play()
        case 3:
            print("Thanks For Playing")
        case _:
            print("Invalid Choice...Try Again")

def play():
    chose(listOfChoice)
    game(userChioce)
    again()

play()

