import tkinter as tk
import random

class GuessTheNumberApp:
    def __init__(self, root):
        self.root = root
        root.title("Guess the Number Game")

        # Entry for guesses
        self.guess_entry = tk.Entry(root)
        self.guess_entry.pack()

        # Submit button
        self.submit_button = tk.Button(root, text="Submit", command=self.submit_guess)
        self.submit_button.pack()

        # Result label
        self.result_label = tk.Label(root, text="Guess a number between 1 and 100")
        self.result_label.pack()

        # Debug label (hidden initially)
        self.debug_label = tk.Label(root, text="")
        self.debug_label.pack()

        # Restart button
        self.restart_button = tk.Button(root, text="Restart", command=self.initialize_game)
        self.restart_button.pack()

        # Exit button
        self.exit_button = tk.Button(root, text="Exit", command=root.quit)
        self.exit_button.pack()

        # Initialize game variables
        self.initialize_game()

    def initialize_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.result_label.config(text="Guess a number between 1 and 100")
        
        # Update the debug label with the number to guess
        self.debug_label.config(text=f"Debug: Number to guess is {self.number_to_guess}")

    def submit_guess(self):
        try:
            guess = int(self.guess_entry.get())
            if guess < self.number_to_guess:
                self.result_label.config(text="Too low. Try again!")
            elif guess > self.number_to_guess:
                self.result_label.config(text="Too high. Try again!")
            else:
                self.result_label.config(text=f"Congratulations! You guessed it right: {self.number_to_guess}")
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GuessTheNumberApp(root)
    root.mainloop()

