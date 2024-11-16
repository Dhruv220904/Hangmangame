import random
import tkinter as tk
from tkinter import messagebox

# List of words to choose from
WORDS = ['python', 'java', 'hangman', 'programming', 'developer', 'computer', 'algorithm']

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("400x400")
        
        self.word_to_guess = random.choice(WORDS)
        self.guessed_letters = []
        self.attempts_left = 6
        self.guessed_correctly = False
        
        self.create_widgets()

    def create_widgets(self):
        # Label for word display
        self.word_label = tk.Label(self.root, text=self.get_display_word(), font=("Arial", 24))
        self.word_label.pack(pady=20)
        
        # Label for attempts left
        self.attempts_label = tk.Label(self.root, text=f"Attempts left: {self.attempts_left}", font=("Arial", 14))
        self.attempts_label.pack(pady=10)

        # Entry for letter input
        self.letter_entry = tk.Entry(self.root, font=("Arial", 14), width=3)
        self.letter_entry.pack(pady=10)
        
        # Button to submit the letter
        self.submit_button = tk.Button(self.root, text="Guess", font=("Arial", 14), command=self.submit_guess)
        self.submit_button.pack(pady=10)
        
        # Button to restart the game
        self.restart_button = tk.Button(self.root, text="Restart", font=("Arial", 14), command=self.restart_game)
        self.restart_button.pack(pady=10)
        self.restart_button.config(state=tk.DISABLED)  # Disable restart button until the game ends
    
    def get_display_word(self):
        display_word = ''
        for letter in self.word_to_guess:
            if letter in self.guessed_letters:
                display_word += letter + ' '
            else:
                display_word += '_ '
        return display_word.strip()

    def submit_guess(self):
        guess = self.letter_entry.get().lower()
        
        # Validate the input
        if len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Invalid Input", "Please enter a valid single letter.")
            return
        
        if guess in self.guessed_letters:
            messagebox.showwarning("Repeated Guess", "You've already guessed that letter.")
            return
        
        # Add the guess to the list of guessed letters
        self.guessed_letters.append(guess)
        
        # Check if the guess is in the word
        if guess in self.word_to_guess:
            self.word_label.config(text=self.get_display_word())
        else:
            self.attempts_left -= 1
            self.attempts_label.config(text=f"Attempts left: {self.attempts_left}")
        
        # Check for win or loss
        if self.attempts_left == 0:
            self.end_game("Game Over", "You've run out of attempts! The word was: " + self.word_to_guess)
        elif all(letter in self.guessed_letters for letter in self.word_to_guess):
            self.end_game("Congratulations!", "You've guessed the word: " + self.word_to_guess)
    
    def end_game(self, title, message):
        messagebox.showinfo(title, message)
        self.submit_button.config(state=tk.DISABLED)  # Disable the submit button
        self.restart_button.config(state=tk.NORMAL)  # Enable the restart button

    def restart_game(self):
        self.word_to_guess = random.choice(WORDS)
        self.guessed_letters = []
        self.attempts_left = 6
        self.guessed_correctly = False
        self.word_label.config(text=self.get_display_word())
        self.attempts_label.config(text=f"Attempts left: {self.attempts_left}")
        self.submit_button.config(state=tk.NORMAL)  # Enable the submit button
        self.restart_button.config(state=tk.DISABLED)  # Disable the restart button

# Set up the main Tkinter window
root = tk.Tk()

# Create an instance of the HangmanGame class
game = HangmanGame(root)

# Run the game
root.mainloop()
