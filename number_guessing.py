"""
    
  You are required to build a simple number guessing game where the computer randomly selects a 
    number and the user has to guess it. The user will be given a limited number of chances to guess the number. 
    If the user guesses the number correctly, the game will end, and the user will win. 
    Otherwise, the game will continue until the user runs out of chances.

"""

import random
to_guess = random.randint(1,100)

def main():

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    print("======================\n")
    print("Please select the difficulty level")
    print("1. Easy (10 guesses)")
    print("2. Medium (5 guesses)")
    print("3. Hard (3 guesses)")


    choice = input("\n\nEnter your choice: ")


    if choice == '1':
        choice = 10 #10 guesses if easy was chosen
        difficulty = 'Easy'
    elif choice == '2':
        choice = 5 #5 guesses if medium was chosen
        difficulty = 'Medium'
    elif choice == '3':
        choice = 3 #3 guesses if hard was chosesn
        difficulty = 'Hard'
    else:
        print("Please select a valid difficulty")

    print(f"\nGreat! You have selected {difficulty} difficulty level.")
    print(f"\nYou have {choice} choices to guess the correct number")
    print("\nLet's start the game!\n")

    attempts = choice
    guessed = False #flag to say that the user did not guess the number

    while attempts > 0 and not guessed: #while the guesses are not yet fully consumed and the number is not yet guessed, this code runs
        guess = int(input("\nEnter your guess: ")) 
        attempts -= 1
        print(f"You have {attempts} remaining guesses")
        if guess != to_guess:
            if guess > to_guess:
                print(f"\nIncorrect! The number is less than {guess}")
            else:
                print(f"\nIncorrect The number is greater than {guess}")
        else:
            print(f"\nCongratulations! You guessed the correct number in {choice - attempts} attempt(s)") 
            guessed = True #the flag is true; meaning it guessed the number
            
    if not guessed: #if the user did not guess the number the flag is still 'false' so, not 'false' means true so it will run this condition
        print(f"\nThank you for playing! Unfortunately, the number was {to_guess}") 

main()
