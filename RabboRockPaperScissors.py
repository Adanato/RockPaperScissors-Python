#Rabbo the Rat Rock Paper Scissors Game in Python.
import random
#User only has 5 chances before Rabbo the Rat terminates their lifespan.
Fail = 0
Games = 0

#Offers the player the choice to keep playing or quit the game.
def PlayAgain():
    global Fail
    Confirm = input("Do you want to play again with me? Yes/No\n")
    if Confirm == "Yes":
            Fail = 0
            RockPaperScissors()
    elif Confirm == "No":
            quit()
    else:
        print("You didn't type Yes/No properly")
        PlayAgain()
        
            
#Checks the users fail count before having them restart or quit the game.            
def FailCheck():
    if Fail > 5:
        print("Nvm You suck at rock paper scissors. Hmph!. *Rabbo pulls out his glock and kills you.")
        print("You Died")
        PlayAgain()

#Rabbo aka the computer picks uses the random choice function to pick an action from the moves list.
#The function returns a string from the array
def RabboChoice():
    Action = ["Rock", "Paper", "Scissors"]
    return random.choice(Action)

#Checks the users answers before passing before comparing it with the CPU's move.
#If the user is wrong the function will keep calling itself.

def UserChoice():
    global Fail
    
    Action = str(input("Rock, Paper, or Scissors?\n"))
    match Action:
        case "Rock":
            return "Rock"
        case "Paper":
            return "Paper"
        case "Scissors":
            return "Scissors"
        case _:
            Fail += 1
            FailCheck()
            print("Type it properly NOW")
            UserChoice()
            
#To be inserted inside the RockPaperScissors Function.
#Tells you if you won using the variables from the RPS Function.           
def Winner(P,R):
    print("You picked " + P + " and Rabbo picked " + R)
    print("You won!")
    
#To be inserted inside the RockPaperScissors Function.
#Tells you if you lost using the variables from the RPS Function.
def Loser(P,R):
    print("You picked " + P + " and Rabbo picked " + R)
    print("You Lost!")

#To be inserted inside the RockPaperScissors Function.
#This function checks if the amount of rounds the user requested has been met or not.
def RoundsChecker(Rounds):
    print("We have " + str(Rounds) + " Rounds left") 

#Compares the stat of the User and the Cpu.
#Gives the final results at the end.
#def StatResult():
    
#Main Function that operates the game by comparing the player and Rabbo's actions.    
def RockPaperScissors():
    Rounds = int(input("How many times do you want to play?\n"))
    if Rounds > 10:
        print("I'm not playing that long idiot")
    while Rounds > 0:
        Player = UserChoice()
        Rabbo = RabboChoice()
    
        if Player == Rabbo:
            print("Dang it we tied")
            Rounds -= 1
            RoundsChecker(Rounds)
        elif Player == "Rock" and Rabbo == "Scissors":
            Winner(Player,Rabbo)
            Rounds -= 1
            RoundsChecker(Rounds)
        elif Player == "Scissor" and Rabbo == "Paper":
            Winner(Player,Rabbo)
            Rounds -= 1
            RoundsChecker(Rounds)
        elif Player == "Paper" and Rabbo == "Rock":
            Winner(Player,Rabbo)
            Rounds -= 1
            RoundsChecker(Rounds)
        else:
            Loser(Player,Rabbo)
            Rounds -= 1
            RoundsChecker(Rounds)
    
    print("Huhu thanks for playing that was fun")
    PlayAgain()
#Long list of Functions end here.

        
#Start of the game    
print("Hi ugly rat what is your name?")
UserName = input()

while UserName != "Anna" and UserName != "anna":
    print("Lol you think I'm stupid. I know your name is Anna, so type it properly or ELSE.")
    FailCheck()
    Fail = Fail + 1
    UserName = input()

if Fail > 1:
    print("Imagine not typing your name right. Lol.")
    RockPaperScissors()
else:
    print("cool lets play huhu.")
    RockPaperScissors()


