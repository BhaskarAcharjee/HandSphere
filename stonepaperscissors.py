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
        self.current_round = 1
        self.total_rounds = 0
        self.player_wins = 0
        self.bot_wins = 0

        self.player_score = tk.IntVar()
        self.bot_score = tk.IntVar()

        self.result_text = tk.StringVar()

        self.create_widgets()
        # Update initial score values
        self.update_scores()
        self.display_default_images()

        self.window.mainloop()

    def create_widgets(self):
        # Game Heading
        game_heading_label = tk.Label(self.window, text="Stone Paper Scissors Game", font=("Arial", 24, "bold"))
        game_heading_label.pack(pady=10)

        # Left Panel
        self.left_panel = tk.Frame(self.window)
        self.left_panel.pack(side="left", padx=10)

        # Player and Bot Images
        images_frame = tk.Frame(self.left_panel)
        images_frame.pack(pady=10)

        self.player_image_label = tk.Label(images_frame)
        self.player_image_label.pack(side="left", padx=10)

        self.bot_image_label = tk.Label(images_frame)
        self.bot_image_label.pack(side="left", padx=10)

        # Your Input and Bot's Input Labels
        input_labels_frame = tk.Frame(self.left_panel)
        input_labels_frame.pack(pady=5)

        self.your_input_label = tk.Label(input_labels_frame, text="Your Input: ", font=("Arial", 12,"bold"))
        self.your_input_label.pack(side="left", padx=10)

        self.bot_input_label = tk.Label(input_labels_frame, text="Bot's Input: ", font=("Arial", 12, "bold"))
        self.bot_input_label.pack(side="left", padx=10)

        # Scorecard and Commentary Box
        score_comment_frame = tk.Frame(self.left_panel)
        score_comment_frame.pack(pady=10)

        commentary_frame = tk.Frame(score_comment_frame)
        commentary_frame.pack(side="left", padx=10)

        self.commentary_label = tk.Label(commentary_frame, text="Commentary Box:", font=("Arial", 12, "bold"))
        self.commentary_label.pack(pady=5)

        self.commentary_text = tk.Text(commentary_frame, width=50, height=10, font=("Arial", 10))
        self.commentary_text.pack()

        # Right Panel
        self.right_panel = tk.Frame(self.window)
        self.right_panel.pack(side="left", padx=10)

        # Total Rounds Entry
        total_rounds_frame = tk.Frame(self.right_panel)
        total_rounds_frame.pack(pady=10)

        total_rounds_label = tk.Label(total_rounds_frame, text="Total Rounds:", font=("Arial", 12))
        total_rounds_label.pack(side="left")

        self.total_rounds_entry = tk.Entry(total_rounds_frame, font=("Arial", 12), width=5)
        self.total_rounds_entry.pack(side="left", padx=5)

        self.start_button = tk.Button(total_rounds_frame, text="Start Game", command=self.start_game, font=("Arial", 12), bg="blue")
        self.start_button.pack(side="left")

        # Predefined Rounds Buttons
        predefined_rounds_frame = tk.Frame(self.right_panel)
        predefined_rounds_frame.pack(pady=10)

        predefined_rounds = [3, 5, 10]  # List of predefined rounds
        self.predefined_buttons = []

        for rounds in predefined_rounds:
            round_button = tk.Button(predefined_rounds_frame, text=str(rounds), command=lambda r=rounds: self.select_predefined_rounds(r), font=("Arial", 12))
            round_button.pack(side="left", padx=5)
            self.predefined_buttons.append(round_button)

        # Player choice buttons
        choices_frame = tk.Frame(self.right_panel)
        choices_frame.pack(pady=20)

        stone_frame = tk.Frame(choices_frame)
        stone_frame.pack(side="left", padx=10)

        stone_image = Image.open("hand_gestures/stone.png")
        stone_image = stone_image.resize((100, 100), Image.LANCZOS)
        stone_photo = ImageTk.PhotoImage(stone_image)
        self.stone_button = tk.Button(stone_frame, image=stone_photo, command=lambda: self.make_choice("Stone"))
        self.stone_button.image = stone_photo
        self.stone_button.pack()

        stone_text = tk.Label(stone_frame, text="Stone", font=("Arial", 12, "bold"))
        stone_text.pack()

        paper_frame = tk.Frame(choices_frame)
        paper_frame.pack(side="left", padx=10)

        paper_image = Image.open("hand_gestures/paper.png")
        paper_image = paper_image.resize((100, 100), Image.LANCZOS)
        paper_photo = ImageTk.PhotoImage(paper_image)
        self.paper_button = tk.Button(paper_frame, image=paper_photo, command=lambda: self.make_choice("Paper"))
        self.paper_button.image = paper_photo
        self.paper_button.pack()

        paper_text = tk.Label(paper_frame, text="Paper", font=("Arial", 12, "bold"))
        paper_text.pack()

        scissors_frame = tk.Frame(choices_frame)
        scissors_frame.pack(side="left", padx=10)

        scissors_image = Image.open("hand_gestures/scissors.png")
        scissors_image = scissors_image.resize((100, 100), Image.LANCZOS)
        scissors_photo = ImageTk.PhotoImage(scissors_image)
        self.scissors_button = tk.Button(scissors_frame, image=scissors_photo, command=lambda: self.make_choice("Scissors"))
        self.scissors_button.image = scissors_photo
        self.scissors_button.pack()

        scissors_text = tk.Label(scissors_frame, text="Scissors", font=("Arial", 12, "bold"))
        scissors_text.pack()

        self.stone_button.config(state="disabled")
        self.paper_button.config(state="disabled")
        self.scissors_button.config(state="disabled")

        # Rounds Label
        rounds_label = tk.Label(self.right_panel, text="Rounds:", font=("Arial", 12))
        rounds_label.pack()

        self.rounds_text = tk.Text(self.right_panel, width=5, height=1, font=("Arial", 12))
        self.rounds_text.pack(pady=10)

        # Player Score
        player_score_frame = tk.Frame(self.right_panel)
        player_score_frame.pack(pady=3)

        player_score_label = tk.Label(player_score_frame, text="Player Score:", font=("Arial", 12, "bold"))
        player_score_label.pack(side="left", padx=10)

        player_score_value = tk.Label(player_score_frame, textvariable=self.player_score, font=("Arial", 12, "bold"), fg="blue")
        player_score_value.pack(side="left")

        # Bot Score
        bot_score_frame = tk.Frame(self.right_panel)
        bot_score_frame.pack(pady=5)

        bot_score_label = tk.Label(bot_score_frame, text="Bot Score:", font=("Arial", 12, "bold"))
        bot_score_label.pack(side="left", padx=10)

        bot_score_value = tk.Label(bot_score_frame, textvariable=self.bot_score, font=("Arial", 12, "bold"), fg="red")
        bot_score_value.pack(side="left")

        # Reset Button
        reset_button = tk.Button(self.right_panel, text="Reset", command=self.reset_game, font=("Arial", 12, "bold"), bg="red")
        reset_button.pack(pady=20)

    def start_game(self):
        self.total_rounds = int(self.total_rounds_entry.get())
        self.rounds_text.insert(tk.END, f"{self.current_round}/{self.total_rounds}")

        self.rounds_text.config(state="disabled")
        self.start_button.config(state="disabled", bg="grey")
        self.stone_button.config(state="normal")
        self.paper_button.config(state="normal")
        self.scissors_button.config(state="normal")
        # Disable predefined buttons
        for button in self.predefined_buttons:
            button.config(state="disabled")

    def select_predefined_rounds(self, rounds):
        self.total_rounds = rounds
        self.total_rounds_entry.delete(0, tk.END)
        self.total_rounds_entry.insert(tk.END, str(rounds))
        self.start_game()

    def set_total_rounds(self, rounds):
        self.total_rounds_entry.delete(0, tk.END)
        self.total_rounds_entry.insert(tk.END, str(rounds))
    
    def update_rounds_text(self):
        self.rounds_text.config(state="normal")
        self.rounds_text.delete("1.0", tk.END)
        self.rounds_text.insert(tk.END, f"{self.current_round}/{self.total_rounds}")
        self.rounds_text.config(state="disabled")

    def make_choice(self, choice):
        self.player_choice = choice
        self.bot_choice = random.choice(self.choices)

        self.display_images()
        self.display_result()
    
    def display_images(self):
        player_image_path = f"hand_gestures/{self.player_choice.lower()}.png"
        bot_image_path = f"hand_gestures/{self.bot_choice.lower()}.png"

        player_image = Image.open(player_image_path)
        player_image = player_image.resize((150, 150), Image.LANCZOS)
        player_photo = ImageTk.PhotoImage(player_image)

        self.player_image_label.configure(image=player_photo)
        self.player_image_label.image = player_photo

        bot_image = Image.open(bot_image_path)
        bot_image = bot_image.resize((150, 150), Image.LANCZOS)
        bot_photo = ImageTk.PhotoImage(bot_image)

        self.bot_image_label.configure(image=bot_photo)
        self.bot_image_label.image = bot_photo

    def display_result(self):
        result = self.get_result()

        if result == "Win":
            result_text = "You Win!"
            self.player_wins += 1
        elif result == "Loss":
            result_text = "You Lose!"
            self.bot_wins += 1
        else:
            result_text = "It's a Tie!"

        result_text += f" (You: {self.player_choice} | Bot: {self.bot_choice})"
        self.result_text.set(result_text)

        self.current_round += 1
        self.update_scores()
        self.update_scorecard(result_text)
        self.update_rounds_text()

        if self.current_round > self.total_rounds:
            self.declare_winner()
        else:
            self.display_player_bot_inputs()

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

    def update_scores(self):
        self.player_score.set(self.player_wins)
        self.bot_score.set(self.bot_wins)

    def update_scorecard(self, result_text):
        scorecard_text = self.commentary_text.get("1.0", tk.END)
        scorecard_text += f"Round {self.current_round}: {result_text}"
        self.commentary_text.delete("1.0", tk.END)
        self.commentary_text.insert(tk.END, scorecard_text)
        self.commentary_text.see(tk.END)  # Enable autoscroll to the end
    
    def display_player_bot_inputs(self):
        self.your_input_label.config(text=f"Your Input: {self.player_choice}")
        self.bot_input_label.config(text=f"Bot's Input: {self.bot_choice}")

    def display_default_images(self):
        default_image = Image.open("hand_gestures/sps_default.png")
        default_image = default_image.resize((150, 150), Image.LANCZOS)
        default_photo = ImageTk.PhotoImage(default_image)

        self.player_image_label.config(image=default_photo)
        self.player_image_label.image = default_photo

        self.bot_image_label.config(image=default_photo)
        self.bot_image_label.image = default_photo

    def declare_winner(self):
        if self.player_wins > self.bot_wins:
            winner_text = "You are the Winner!"
        elif self.player_wins < self.bot_wins:
            winner_text = "Bot is the Winner!"
        else:
            winner_text = "It's a Tie!"

        winner_text += f"\nFinal Score - You: {self.player_wins} | Bot: {self.bot_wins}"
        self.commentary_text.insert(tk.END, winner_text)
        self.commentary_text.see(tk.END)  # Enable autoscroll to the end

    def reset_game(self):
        self.current_round = 1
        self.total_rounds = 0
        self.player_wins = 0
        self.bot_wins = 0
        self.player_score.set(0)
        self.bot_score.set(0)

        self.commentary_text.delete("1.0", tk.END)
        self.commentary_text.delete("1.0", tk.END)
        self.total_rounds_entry.delete(0, tk.END)
        # self.rounds_text.delete("1.0", tk.END)

        self.your_input_label.config(text="Your Input: ")
        self.bot_input_label.config(text="Bot's Input: ")
        self.start_button.config(state="normal", bg="blue")
        self.stone_button.config(state="disabled")
        self.paper_button.config(state="disabled")
        self.scissors_button.config(state="disabled")
        # Enable predefined buttons
        for button in self.predefined_buttons:
            button.config(state="normal")
        
        self.display_default_images()

# if __name__ == "__main__":
#     game = StonePaperScissorsGame()
#     game.start_game()