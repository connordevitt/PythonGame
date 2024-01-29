def guess_the_number():
    import random

    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"Debug: The number to guess is {number_to_guess}")  # Debug 

    # The game 
    while True:
        
        try:
            # Player guess
            guess = int(input("Make a guess: "))
            print(f"Debug: You guessed {guess}")  # Debug

            # Check the guess
            if guess < number_to_guess:
                print("Too low. Try again!")
            elif guess > number_to_guess:
                print("Too high. Try again!")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} correctly!")
                break
        except ValueError:
            print("Please enter a valid number.")

    # Prompt to type exit when finished.
            
def main():
    while True:
        guess_the_number()  # Start the game

        user_choice = input("Do you want to play again? (yes/no): ").lower()
        if user_choice != 'yes':
            print("Thanks for playing! See you soon!")
            break

if __name__ == "__main__":
    main()




# How to create a new .exe python -m PyInstaller --onefile Number.py
