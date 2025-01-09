#Looking to learn how to create random numbers to make a guessing game out of it
import random
print("Lets play a guessing game. Choose a number between 1 and 10")
Number = random.randint(1,10)
Guess = None
while Guess != Number:
    Guess = int(input("What is your guess? :"))
    if Guess == Number:
        print("you got it!")
        print("It was ", Number)
        break
    else:
        print("Try again")
