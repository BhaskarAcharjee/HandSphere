import tkinter as tk
from tkinter import messagebox
import random

class HandCricketGame:
    def __init__(self, window):
        self.window = window
        self.window.title("Hand Cricket Game")
        
        # Create GUI elements
        self.runs_label = tk.Label(window, text="Runs: 0")
        self.runs_label.pack(pady=10)
        
        self.outs_label = tk.Label(window, text="Wickets: 0 / 10")
        self.outs_label.pack(pady=10)
        
        self.user_buttons_frame = tk.Frame(window)
        self.user_buttons_frame.pack(pady=10)
        
        self.bot_label = tk.Label(window, text="Bot's Guess: ")
        self.bot_label.pack(pady=10)
        
        self.reset_button = tk.Button(window, text="Reset", command=self.reset_game)
        self.reset_button.pack(pady=10)
        
        # Scorecard
        self.scorecard_label = tk.Label(window, text="Scorecard:")
        self.scorecard_label.pack(pady=10)
        
        self.scorecard_text = tk.Text(window, width=30, height=10)
        self.scorecard_text.pack()
        
        # Game variables
        self.runs = 0
        self.wickets = 0
        self.bot_guess = 0
        self.scorecard = []
        
        # Create user buttons
        self.user_buttons = []
        for i in range(7):
            button = tk.Button(self.user_buttons_frame, text=str(i), command=lambda i=i: self.user_bat(i))
            button.pack(side="left", padx=5)
            self.user_buttons.append(button)
        
    def user_bat(self, runs):
        self.bot_guess = random.randint(0, 6)

        self.runs += runs
        self.runs_label.config(text="Runs: " + str(self.runs))

        self.bot_label.config(text="Bot's Guess: " + str(self.bot_guess))

        if runs == self.bot_guess:
            self.wickets += 1
            self.outs_label.config(text="Wickets: " + str(self.wickets) + " / 10")
            self.scorecard.append("Out")
            messagebox.showinfo("Out!", "You're out!")
        else:
            self.scorecard.append(str(runs))

        self.update_scorecard()

        if self.wickets == 10:
            messagebox.showinfo("Game Over", "All wickets are down. Game over!")
            self.reset_game()


    def update_scorecard(self):
        self.scorecard_text.delete(1.0, tk.END)
        player_totals = {}  # Dictionary to store each player's total runs
        
        player_number = 1
        player_total_runs = 0

        for score in self.scorecard:
            if score == "Out":
                player_totals["Player " + str(player_number)] = player_total_runs
                player_number += 1
                player_total_runs = 0
            else:
                runs = int(score)
                player_total_runs += runs

        # Add the total runs for the last player if they have not been out yet
        if player_number not in player_totals:
            player_totals["Player " + str(player_number)] = player_total_runs

        # Display the individual player's total runs in the scorecard
        for player, total_runs in player_totals.items():
            self.scorecard_text.insert(tk.END, player + ": " + str(total_runs) + "\n")

        
    def reset_game(self):
        self.runs = 0
        self.wickets = 0
        self.bot_guess = 0
        self.scorecard = []
        
        self.runs_label.config(text="Runs: 0")
        self.outs_label.config(text="Wickets: 0 / 10")
        self.bot_label.config(text="Bot's Guess: ")
        
        self.update_scorecard()
        
# Create the main window
window = tk.Tk()

# Create the Hand Cricket game instance
game = HandCricketGame(window)

# Run the GUI event loop
window.mainloop()