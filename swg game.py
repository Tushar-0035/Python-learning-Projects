import random

nturns=1
your_score=0
computer_score=0
while(nturns<=10):
    lst = ["snake", "gun", "water"]
    ch = random.choice(lst)

    print("choose: snake,gun,water")
    userch=input("enter your choice\n")

    if(ch=="snake" and userch=="snake"):
        print("tie,you both choose same")

    elif(ch=="gun" and userch=="gun"):
        print("tie,you both choose same")

    elif(ch=="water" and userch=="water"):
        print("tie,you both choose same")

    elif(ch=="snake" and userch=="water" ):
        print("computer win this round")
        computer_score=computer_score+1
        print(f"computer score:{computer_score}")

    elif(ch=="snake" and userch=="gun"):
        print("you win this round")
        your_score=your_score+1
        print(f"your score:{your_score}")

    elif(ch=="gun" and userch=="snake"):
        print("computer win this round")
        computer_score=computer_score+1
        print(f"computer score:{computer_score}")

    elif(ch=="gun" and userch=="water"):
        print("you win this round")
        your_score=your_score+1
        print(f"your score:{your_score}")

    elif(ch=="water" and userch=="gun"):
        print("computer win this round")
        computer_score=computer_score+1
        print(f"computer score:{computer_score}")

    elif(ch=="water" and userch=="snake"):
        print("you win this round")
        your_score=your_score+1
        print(f"your score:{your_score}")

    else:
        print("inavlid input")
        continue

    print(10-nturns,"no.of turns left")
    nturns=nturns+1

if(computer_score>your_score):
    print(f"computer_score is {computer_score} and your_score is {your_score}")
    print("\t\t\tComputer won this game")

elif(computer_score<your_score):
    print(f"computer_score is {computer_score} and your_score is {your_score}")
    print("\t\t\tyou won this game")

else:
    print("game draw")
    print(f"computer_score is {computer_score} and your_score is {your_score}")

if(nturns>10):
    print("\t\t\t\t\t\tGAME OVER")





