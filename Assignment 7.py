import tkinter as tk
from tkinter import ttk, messagebox

# List of sentences with missing words
sentences = [
    ("The cat is sitting on the ____.", "mat"),
    ("She is reading a very interesting ____.", "book"),
    ("He is the best ____ in the world.", "player"),
    ("I need to buy some fresh ____.", "fruits"),
]


class CleanCryptarithmeticGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Cryptarithmetic Game")
        self.index = 0
        self.attempts = 3  # Set initial number of attempts

        # Set window size and center it
        self.root.geometry('400x350')
        self.root.eval('tk::PlaceWindow . center')

        # Configure a clean look for the grid layout
        self.root.configure(padx=20, pady=20)

        # Style configuration for modern look
        style = ttk.Style()
        style.configure("TLabel", font=("Arial", 14), padding=15)
        style.configure("TButton", font=("Arial", 12), padding=10)
        style.configure("TEntry", font=("Arial", 14), padding=5)

        # Instruction label
        self.instruction_label = ttk.Label(root, text="Fill in the missing word:")
        self.instruction_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        # Sentence label
        self.sentence_label = ttk.Label(root, text="")
        self.sentence_label.grid(row=1, column=0, columnspan=2, pady=10)

        # Input field
        self.input_entry = ttk.Entry(root, font=("Arial", 14), width=20)
        self.input_entry.grid(row=2, column=0, columnspan=2, pady=10)

        # Submit button
        self.submit_button = ttk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.grid(row=3, column=0, pady=10)

        # Next button (disabled initially)
        self.next_button = ttk.Button(root, text="Next", command=self.next_sentence, state=tk.DISABLED)
        self.next_button.grid(row=3, column=1, pady=10)

        # Feedback label
        self.feedback_label = ttk.Label(root, text="", foreground="green")
        self.feedback_label.grid(row=4, column=0, columnspan=2, pady=10)

        # Attempts left label
        self.attempts_label = ttk.Label(root, text=f"Attempts left: {self.attempts}")
        self.attempts_label.grid(row=5, column=0, columnspan=2, pady=10)

        # Start with the first sentence
        self.show_sentence()

    def show_sentence(self):
        sentence, _ = sentences[self.index]
        self.sentence_label.config(text=sentence.replace("____", "______"))
        self.feedback_label.config(text="")
        self.input_entry.delete(0, tk.END)
        self.attempts = 3  # Reset attempts for new sentence
        self.attempts_label.config(text=f"Attempts left: {self.attempts}")
        self.submit_button.config(state=tk.NORMAL)
        self.next_button.config(state=tk.DISABLED)

    def check_answer(self):
        user_guess = self.input_entry.get().strip().lower()
        correct_word = sentences[self.index][1]

        if user_guess == correct_word:
            self.feedback_label.config(text=f"Correct! The word is '{correct_word}'", foreground="green")
            self.submit_button.config(state=tk.DISABLED)
            self.next_button.config(state=tk.NORMAL)
        else:
            self.attempts -= 1
            if self.attempts > 0:
                self.feedback_label.config(text=f"Incorrect. Try again! Attempts left: {self.attempts}", foreground="red")
                self.attempts_label.config(text=f"Attempts left: {self.attempts}")
            else:
                self.feedback_label.config(text=f"Out of attempts! The correct word was '{correct_word}'", foreground="red")
                self.submit_button.config(state=tk.DISABLED)
                self.next_button.config(state=tk.NORMAL)

    def next_sentence(self):
        self.index += 1
        if self.index < len(sentences):
            self.show_sentence()
        else:
            messagebox.showinfo("Game Over", "You've completed all the sentences!")
            self.root.quit()


# Create the main window
root = tk.Tk()
game = CleanCryptarithmeticGame(root)
root.mainloop()
