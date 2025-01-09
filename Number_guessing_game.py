#Looking to learn how to create random numbers to make a guessing game out of it
import random
print("Lets play a guessing game. Choose a number between 1 and 10")
Number = random.randint(1,10)
#This line sets up the Guess variable to be maleable in the While If Else loop
Guess = None
while Guess != Number:
    Guess = int(input("What is your guess? :"))
    if Guess == Number:
        print("you got it!")
        print("It was ", Number)
        break
    else:
        print("Try again")
#Once the loop is completed the code breaks and ends the game.