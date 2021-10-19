import random

nturns=1
your_score=0
computer_score=0
print("s for stone","\np for paper","\nsc for scissor")
while(nturns<=10):
    lst = ["s", "p", "sc"]
    ch = random.choice(lst)

    print("choose: s,p,sc")
    userch=input("enter your choice\n")

    if(ch=="s" and userch=="s"):
        print("tie,you both choose same")

    elif(ch=="p" and userch=="p"):
        print("tie,you both choose same")

    elif(ch=="sc" and userch=="sc"):
        print("tie,you both choose same")

    elif(ch=="s" and userch=="sc" ):
        print("computer win this round")
        computer_score=computer_score+1
        print(f"computer score:{computer_score}")

    elif(ch=="s" and userch=="p"):
        print("you win this round")
        your_score=your_score+1
        print(f"your score:{your_score}")

    elif(ch=="sc" and userch=="p"):
        print("computer win this round")
        computer_score=computer_score+1
        print(f"computer score:{computer_score}")

    elif(ch=="sc" and userch=="s"):
        print("you win this round")
        your_score=your_score+1
        print(f"your score:{your_score}")

    elif(ch=="p" and userch=="s"):
        print("computer win this round")
        computer_score=computer_score+1
        print(f"computer score:{computer_score}")

    elif(ch=="p" and userch=="sc"):
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





