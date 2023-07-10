import tkinter as tk
import random

class StonePaperScissorsGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Stone Paper Scissors")

        self.choices = ["Stone", "Paper", "Scissors"]

        self.player_choice = ""
        self.bot_choice = ""

        self.result_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self.window, text="Stone Paper Scissors", font=("Arial", 18, "bold"))
        title_label.pack(pady=20)

        # Player choice buttons
        choices_frame = tk.Frame(self.window)
        choices_frame.pack()

        stone_button = tk.Button(choices_frame, text="Stone", width=10, command=lambda: self.make_choice("Stone"))
        stone_button.pack(side="left", padx=10)

        paper_button = tk.Button(choices_frame, text="Paper", width=10, command=lambda: self.make_choice("Paper"))
        paper_button.pack(side="left", padx=10)

        scissors_button = tk.Button(choices_frame, text="Scissors", width=10, command=lambda: self.make_choice("Scissors"))
        scissors_button.pack(side="left", padx=10)

        result_label = tk.Label(self.window, textvariable=self.result_text, font=("Arial", 16))
        result_label.pack(pady=20)

    def make_choice(self, choice):
        self.player_choice = choice
        self.bot_choice = random.choice(self.choices)

        self.display_result()

    def display_result(self):
        result = self.get_result()

        if result == "Win":
            result_text = "You Win!"
        elif result == "Loss":
            result_text = "You Lose!"
        else:
            result_text = "It's a Tie!"

        result_text += f" (You: {self.player_choice} | Bot: {self.bot_choice})"
        self.result_text.set(result_text)

    def get_result(self):
        if self.player_choice == self.bot_choice:
            return "Tie"
        elif (
            (self.player_choice == "Stone" and self.bot_choice == "Scissors")
            or (self.player_choice == "Paper" and self.bot_choice == "Stone")
            or (self.player_choice == "Scissors" and self.bot_choice == "Paper")
        ):
            return "Win"
        else:
            return "Loss"

    def start_game(self):
        self.window.mainloop()

# if __name__ == "__main__":
#     game = StonePaperScissorsGame()
#     game.start_game()