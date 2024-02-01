import tkinter as tk
import random

class GuessTheNumberApp:
    def __init__(self, root):
        self.root = root
        root.title("THE Guess the Number Game")
        root.configure(bg='dark blue')
        self.guess_entry.bind("<Return>", lambda event: self.submit_guess())


        # Create a frame for the widgets
        frame = tk.Frame(root, bg='dark blue', padx=10, pady=10)
        frame.pack(padx=10, pady=10)

        # Entry for guesses
        self.guess_entry = tk.Entry(frame, font=('Helvetica', 14), width=15)
        self.guess_entry.pack(pady=5)

        # Submit button
        self.submit_button = tk.Button(frame, text="Submit", command=self.submit_guess, font=('Helvetica', 12), bg='light green')
        self.submit_button.pack(pady=5)

        # Result label
        self.result_label = tk.Label(frame, text="Guess a number between 1 and 100", bg='light blue', font=('Helvetica', 12))
        self.result_label.pack(pady=5)

        # Debug label (hidden initially)
        self.debug_label = tk.Label(frame, text="", bg='light blue', font=('Helvetica', 12))
        self.debug_label.pack(pady=5)

        # Restart button
        self.restart_button = tk.Button(frame, text="Restart", command=self.initialize_game, font=('Helvetica', 12), bg='yellow')
        self.restart_button.pack(pady=5)

        # Exit button
        self.exit_button = tk.Button(frame, text="Exit", command=root.quit, font=('Helvetica', 12), bg='red')
        self.exit_button.pack(pady=5)

        # Initialize game variables
        self.initialize_game()

    def initialize_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.result_label.config(text="Guess a number between 1 and 100.")
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
