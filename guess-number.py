
import random

def main():
    #Initialize program
    print("Guess a number from 1 to 100.")

    randNum = random.randint(1,100)
    found = False

    while not found:
        userGuess = int(input("Your guess: "))
        if userGuess == randNum:
             print("got it!")
             found = True
        elif userGuess > randNum:
             print("Lower")
        else:
             print("Higher")

    print("Good guess! Thanks for playing")
	
if __name__ == "__main__":
    main()