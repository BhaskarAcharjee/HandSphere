import tkinter as tk
from PIL import ImageTk, Image
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

        stone_image = Image.open("hand_gestures/stone.png")
        stone_image = stone_image.resize((100, 100), Image.LANCZOS)
        stone_photo = ImageTk.PhotoImage(stone_image)
        stone_button = tk.Button(choices_frame, image=stone_photo, command=lambda: self.make_choice("Stone"))
        stone_button.image = stone_photo
        stone_button.pack(side="left", padx=10)

        paper_image = Image.open("hand_gestures/paper.png")
        paper_image = paper_image.resize((100, 100), Image.LANCZOS)
        paper_photo = ImageTk.PhotoImage(paper_image)
        paper_button = tk.Button(choices_frame, image=paper_photo, command=lambda: self.make_choice("Paper"))
        paper_button.image = paper_photo
        paper_button.pack(side="left", padx=10)

        scissors_image = Image.open("hand_gestures/scissors.png")
        scissors_image = scissors_image.resize((100, 100), Image.LANCZOS)
        scissors_photo = ImageTk.PhotoImage(scissors_image)
        scissors_button = tk.Button(choices_frame, image=scissors_photo, command=lambda: self.make_choice("Scissors"))
        scissors_button.image = scissors_photo
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