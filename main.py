import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from HandSphere import HandCricketGame
from stonepaperscissors import StonePaperScissorsGame

class MainMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Game Selection")
        self.geometry("500x400")
        self.configure(background="#F0F0F0")

        # Main heading label
        heading_label = ttk.Label(self, text="Game Selection", font=("Arial", 24, "bold"), background="#F0F0F0")
        heading_label.pack(pady=20)

        # Frame to contain the buttons and labels
        game_frame = tk.Frame(self, background="#F0F0F0")
        game_frame.pack()

        # Hand Cricket button with image and label
        hand_cricket_image = Image.open("icons/hand_cricket.png")
        hand_cricket_image = hand_cricket_image.resize((150, 150), Image.LANCZOS)
        hand_cricket_photo = ImageTk.PhotoImage(hand_cricket_image)

        hand_cricket_button = ttk.Button(game_frame, image=hand_cricket_photo, command=self.play_hand_cricket, style="GameButton.TButton")
        hand_cricket_button.image = hand_cricket_photo  # Store reference to avoid garbage collection
        hand_cricket_button.grid(row=0, column=0, padx=20, pady=10)

        hand_cricket_label = ttk.Label(game_frame, text="Hand Cricket", font=("Arial", 12, "bold"), background="#F0F0F0")
        hand_cricket_label.grid(row=1, column=0, pady=5)

        # Stone Paper Scissors button with image and label
        stone_paper_image = Image.open("icons/stone_paper.png")
        stone_paper_image = stone_paper_image.resize((150, 150), Image.LANCZOS)
        stone_paper_photo = ImageTk.PhotoImage(stone_paper_image)

        stone_paper_button = ttk.Button(game_frame, image=stone_paper_photo, command=self.play_stone_paper_scissors, style="GameButton.TButton")
        stone_paper_button.image = stone_paper_photo  # Store reference to avoid garbage collection
        stone_paper_button.grid(row=0, column=1, padx=20, pady=10)

        stone_paper_label = ttk.Label(game_frame, text="Stone Paper Scissors", font=("Arial", 12, "bold"), background="#F0F0F0")
        stone_paper_label.grid(row=1, column=1, pady=5)

        # Styling
        self.style = ttk.Style()
        self.style.configure("GameButton.TButton", font=("Arial", 12), foreground="#FFFFFF", background="#4CAF50", width=150, height=150)

    def play_hand_cricket(self):
        self.destroy()
        window = tk.Tk()
        window.title("Virtual Cricket Game")
        game = HandCricketGame(window)
        window.mainloop()

    def play_stone_paper_scissors(self):
        self.destroy()
        game = StonePaperScissorsGame()
        game.start_game()

if __name__ == "__main__":
    app = MainMenu()
    app.mainloop()
