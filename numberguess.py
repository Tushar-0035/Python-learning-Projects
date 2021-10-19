import random
n=random.randint(0,100)
number_of_guesses=1
while(number_of_guesses<=9):
    guess_number=int(input("guess the number"))
    if(guess_number>n):
        print("you have enterd larger number")
    elif(guess_number<n):
        print("you have entered smaller number")
    else:
        print("you won")
        print(number_of_guesses,"no. of guesses took to finish")
        break
    print(9-number_of_guesses,"no. of guesses left")
    number_of_guesses=number_of_guesses+1
if(number_of_guesses>9):
    print("game over")



