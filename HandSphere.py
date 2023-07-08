import tkinter as tk
from tkinter import messagebox
import random

class HandCricketGame:
    def __init__(self, window):
        self.window = window
        self.window.title("Cricket Game")

        # ---------GUI elements---------
        # Toss Result
        self.toss_label = tk.Label(window, text="Toss Result:", font=("Arial", 10, "bold"))
        self.toss_label.pack(pady=6)

        # Toss buttons
        self.toss_buttons_frame = tk.Frame(window)
        self.toss_buttons_frame.pack(pady=5)

        self.toss_buttons = []
        for option in ["Heads", "Tails"]:
            button = tk.Button(self.toss_buttons_frame, text=option, command=lambda o=option: 
                               self.choose_toss_option(o), font=("Arial", 10))
            button.pack(side="left", padx=5)
            self.toss_buttons.append(button)

        # Batting/Bowling
        self.bat_bowl_buttons_frame = tk.Frame(window)
        self.bat_bowl_buttons_frame.pack(pady=5)

        self.bat_bowl_buttons = []
        for option in ["Batting", "Bowling"]:
            button = tk.Button(self.bat_bowl_buttons_frame, text=option, command=lambda option=option: 
                               self.choose_bat_bowl_option(option), font=("Arial", 10))
            button.pack(side="left", padx=5)
            self.bat_bowl_buttons.append(button)

        # Runs and Wickets
        self.runs_wickets_frame = tk.Frame(window)
        self.runs_wickets_frame.pack(pady=10)

        self.runs_label = tk.Label(self.runs_wickets_frame, text="Runs: 0", font=("Arial", 12))
        self.runs_label.pack(side="left", padx=5)

        self.outs_label = tk.Label(self.runs_wickets_frame, text="Wickets: 0 / 3", font=("Arial", 12))
        self.outs_label.pack(side="left", padx=5)

        # Bot's Guess
        self.bot_label = tk.Label(window, text="Bot's Guess:", font=("Arial", 12, "bold"))
        self.bot_label.pack(pady=10)

        # Actual Scorecard
        self.scorecards_label = tk.Label(window, text="Actual Scorecard:", font=("Arial", 12, "bold"))
        self.scorecards_label.pack(pady=10)

        self.scorecards_text = tk.Text(window, width=50, height=5, font=("Arial", 10))
        self.scorecards_text.pack()

        # Your input to Batting or Bowling
        self.runs_buttons_label = tk.Label(window, text="Your Input:", font=("Arial", 12, "bold"))
        self.runs_buttons_label.pack(pady=6)

        # Runs buttons
        self.runs_buttons_frame = tk.Frame(window)
        self.runs_buttons_frame.pack(pady=5)

        self.run_buttons = []
        for i in range(7):
            button = tk.Button(self.runs_buttons_frame, text=str(i), command=lambda r=i: self.user_bat_bowl(r), font=("Arial", 10))
            button.pack(side="left", padx=5)
            self.run_buttons.append(button)

        # Additional GUI elements for batting shots
        self.batting_shots_label = tk.Label(window, text="Batting Shots:", font=("Arial", 12, "bold"))
        self.batting_shots_label.pack(pady=5)

        self.batting_shots_frame = tk.Frame(window)
        self.batting_shots_frame.pack(pady=8)

        self.batting_shots = ["Defensive Shot", "Attacking Shot", "Lofted Shot"]
        self.batting_buttons = []
        for shot in self.batting_shots:
            button = tk.Button(self.batting_shots_frame, text=shot, command=lambda s=shot: self.user_bat_with_shot(s), font=("Arial", 10))
            button.pack(side="left", padx=5)
            self.batting_buttons.append(button)

        # Additional GUI elements for bowling variations
        self.bowling_variations_label = tk.Label(window, text="Bowling Variations:", font=("Arial", 12, "bold"))
        self.bowling_variations_label.pack(pady=5)

        self.bowling_variations_frame = tk.Frame(window)
        self.bowling_variations_frame.pack(pady=8)

        self.bowling_variations = ["Fast Bowling", "Spin Bowling", "Swing Bowling"]
        self.bowling_buttons = []
        for variation in self.bowling_variations:
            button = tk.Button(self.bowling_variations_frame, text=variation, command=lambda v=variation: 
                               self.bot_bowl_with_variation(v), font=("Arial", 10))
            button.pack(side="left", padx=5)
            self.bowling_buttons.append(button)

        # Players Scorecard
        self.scorecard_label = tk.Label(window, text="Scorecard:", font=("Arial", 12, "bold"))
        self.scorecard_label.pack(pady=10)

        self.scorecard_text = tk.Text(window, width=30, height=10, font=("Arial", 10))
        self.scorecard_text.pack()

        # Reset Button
        self.reset_button = tk.Button(window, text="Reset", command=self.reset_game, font=("Arial", 12))
        self.reset_button.pack(pady=10)

        # Initially Enable/Disable Buttons
        self.enable_toss_buttons()
        self.disable_runs_buttons()
        self.disable_bat_bowl_buttons()
        self.disable_batting_buttons()
        self.disable_bowling_buttons()

        # Game variables
        self.runs = 0
        self.wickets = 0
        self.bot_runs = 0
        self.bot_wickets = 0
        self.bot_guess = 0
        self.scorecard = []
        self.target_score = 0
        self.overs = 0
        self.balls_bowled = 0
        self.bot_overs = 0
        self.bot_balls_bowled = 0
        self.innings_count = 0

        self.batting_enabled = False
        self.bowling_enabled = False

        # Toss variables
        self.toss_result = ""
        self.user_won_toss = False
        
    
    def user_bat_bowl(self, runs):
        if self.batting_enabled:
            self.bot_guess = random.randint(0, 6)
            self.bot_label.config(text="Bot's Guess: " + str(self.bot_guess))

            if runs != self.bot_guess:
                self.runs += runs
                self.runs_label.config(text="Your Runs: " + str(self.runs))

            if runs == self.bot_guess:
                self.wickets += 1
                self.outs_label.config(text="Your Wickets: " + str(self.wickets) + " / 3")
                self.scorecard.append("Out")
            else:
                self.scorecard.append("Player: " + str(runs))

            self.bot_balls_bowled += 1
            if self.bot_balls_bowled % 6 == 0:  # Check if the over is complete
                self.bot_overs += 1
                self.bot_balls_bowled = 0

            self.update_scorecard()
            self.update_actual_scorecard()

            if self.wickets == 3:
                messagebox.showinfo("Innings Over", "All your's wickets are down. Innings is over!")
                self.innings_count += 1
                self.between_innings()
                    
        elif self.bowling_enabled:
            self.bot_guess = random.randint(0, 6)
            self.bot_label.config(text="Bot's Guess: " + str(self.bot_guess))

            if runs != self.bot_guess:
                self.bot_runs += self.bot_guess
                self.runs_label.config(text="Bot's Runs: " + str(self.bot_runs))

            if runs == self.bot_guess:
                self.bot_wickets += 1
                self.outs_label.config(text="Bot's Wickets: " + str(self.bot_wickets) + " / 3")
                self.scorecard.append("Bot Out")
            else:
                self.scorecard.append("Bot: " + str(self.bot_guess))

            self.balls_bowled += 1
            if self.balls_bowled % 6 == 0:  # Check if the over is complete
                self.overs += 1
                self.balls_bowled = 0

            self.update_scorecard()
            self.update_actual_scorecard()

            if self.bot_wickets == 3:
                self.innings_count += 1
                messagebox.showinfo("Innings Over", "All bot's wickets are down. Innings is over!")
                self.between_innings()


    def choose_toss_option(self, option):
        toss_options = ["Heads", "Tails"]
        self.toss_result = random.choice(toss_options)
        self.toss_label.config(text="Toss Result: " + self.toss_result)

        if option == self.toss_result:
            self.user_won_toss = True
            messagebox.showinfo("Toss Result", "You won the toss! Choose Batting or Bowling.")
        else:
            self.user_won_toss = False
            messagebox.showinfo("Toss Result", "You lost the toss! Bot will choose Batting or Bowling.")

        self.disable_toss_buttons()
        self.enable_bat_bowl_buttons()
    
    def select_bat(self):
        self.batting_enabled = True
        self.bowling_enabled = False
        self.enable_runs_buttons()
        self.disable_bat_bowl_buttons()
        self.enable_batting_buttons()
        self.disable_bowling_buttons()

    def select_bowl(self):
        self.batting_enabled = False
        self.bowling_enabled = True
        self.enable_runs_buttons()
        self.disable_bat_bowl_buttons()
        self.disable_batting_buttons()
        self.enable_bowling_buttons()
        
    def choose_bat_bowl_option(self, option):
        self.disable_bat_bowl_buttons()

        if option == "Batting":
            self.select_bat()
        else:
            self.select_bowl()
    
    def user_bat_with_shot(self, shot):
        # Simulate batting shot behavior
        if shot == "Defensive Shot":
            runs = random.choice([0, 1])
        elif shot == "Attacking Shot":
            runs = random.choice([2, 3, 4, 5, 6])
        elif shot == "Lofted Shot":
            runs = random.choice([4, 6])
        
        self.user_bat_bowl(runs)
    
    def bot_bowl_with_variation(self, variation):
        # Simulate bowling variation behavior
        if variation == "Fast Bowling":
            runs = random.choice([0, 4, 6])  
        elif variation == "Spin Bowling":
            runs = random.choice([2, 4, 5])  
        elif variation == "Swing Bowling":
            runs = random.choice([1, 3, 6]) 
        
        self.user_bat_bowl(runs)

    def between_innings(self):
        inning_scorecard = self.get_inning_scorecard()

        self.runs_label.config(text="Runs: 0")
        self.outs_label.config(text="Wickets: 0 / 3")
        self.bot_label.config(text="Bot's Guess: ")

        if self.innings_count == 1:
            messagebox.showinfo("Between Innings", "First innings is over!\n\n" + inning_scorecard)
        else:
            messagebox.showinfo("Between Innings", "Second innings is over!\n\n" + inning_scorecard)

        self.calculate_target_score()

        self.enable_bat_bowl_buttons()
        self.disable_runs_buttons()

        self.check_game_over() #Checks Game Over

    def update_scorecard(self):
        self.scorecard_text.delete(1.0, tk.END)
        inning_scorecard = ""
        player_score = 0
        bot_score = 0

        for score in self.scorecard:
            if score == "Out":
                inning_scorecard += "Player: " + str(player_score) + "\n"
                player_score = 0
            elif score == "Bot Out":
                inning_scorecard += "Bot: " + str(bot_score) + "\n"
                bot_score = 0
            elif score.startswith("Player"):
                player_score += int(score.split(": ")[1])
            elif score.startswith("Bot"):
                bot_score += int(score.split(": ")[1])

        if self.batting_enabled:
            inning_scorecard += "Player: " + str(player_score) + "\n"
        else:
            inning_scorecard += "Bot: " + str(bot_score) + "\n"
        self.scorecard_text.insert(tk.END, inning_scorecard)

    def get_inning_scorecard(self):
        inning_scorecard = ""
        player_score = 0
        bot_score = 0

        for score in self.scorecard:
            if score.startswith("Player"):
                score_parts = score.split(": ")
                if len(score_parts) > 1:
                    player_score += int(score_parts[1])
            elif score.startswith("Bot"):
                score_parts = score.split(": ")
                if len(score_parts) > 1:
                    bot_score += int(score_parts[1])

        inning_scorecard += "Player: " + str(player_score) + "\n"
        inning_scorecard += "Bot: " + str(bot_score) + "\n"

        return inning_scorecard

    def calculate_target_score(self):
        self.target_score = self.runs + 1
    
    def get_actual_scorecard(self):
        return f"Your Stat: Runs: {self.runs} - Overs: {self.bot_overs}.{self.bot_balls_bowled % 6} -  Wickets: {self.wickets}" + "\n" + f"Bot's Stat: Runs: {self.bot_runs} - Overs: {self.overs}.{self.balls_bowled % 6} -  Wickets: {self.bot_wickets}"

    def update_actual_scorecard(self):
        self.scorecards_text.delete(1.0, tk.END)
        self.scorecards_text.insert(tk.END, self.get_actual_scorecard())

    def enable_toss_buttons(self):
        for button in self.toss_buttons:
            button.config(state="normal")

    def disable_toss_buttons(self):
        for button in self.toss_buttons:
            button.config(state="disabled")

    def enable_bat_bowl_buttons(self):
        for button in self.bat_bowl_buttons:
            button.config(state="normal")

    def disable_bat_bowl_buttons(self):
        for button in self.bat_bowl_buttons:
            button.config(state="disabled")

    def enable_runs_buttons(self):
        for button in self.run_buttons:
            button.config(state="normal")

    def disable_runs_buttons(self):
        for button in self.run_buttons:
            button.config(state="disabled")
    
    def enable_batting_buttons(self):
        for button in self.batting_buttons:
            button.config(state="normal")

    def disable_batting_buttons(self):
        for button in self.batting_buttons:
            button.config(state="disabled")

    def enable_bowling_buttons(self):
        for button in self.bowling_buttons:
            button.config(state="normal")

    def disable_bowling_buttons(self):
        for button in self.bowling_buttons:
            button.config(state="disabled")

    def check_game_over(self):
        inning_scorecard = self.get_inning_scorecard()

        if self.innings_count == 2:
            player_total_runs = sum([int(score.split(": ")[1]) for score in self.scorecard if
                                        score.startswith("Player") and len(score.split(": ")) > 1])
            bot_total_runs = sum([int(score.split(": ")[1]) for score in self.scorecard if
                                    score.startswith("Bot") and len(score.split(": ")) > 1])

            if player_total_runs > bot_total_runs:
                winner_message = "You win!"
            elif player_total_runs < bot_total_runs:
                winner_message = "Bot wins!"
            else:
                winner_message = "It's a tie!"

            messagebox.showinfo("Game Over", f"{winner_message}\n\n{inning_scorecard}")
            self.reset_game() # Reset Innings 

    def reset_game(self):
        self.runs = 0
        self.wickets = 0
        self.bot_runs = 0
        self.bot_wickets = 0
        self.overs = 0
        self.balls_bowled = 0
        self.bot_overs = 0
        self.bot_balls_bowled = 0
        self.bot_guess = 0
        self.scorecard = []
        self.target_score = 0
        self.innings_count = 0

        self.batting_enabled = False
        self.bowling_enabled = False

        self.toss_result = ""
        self.user_won_toss = False

        self.runs_label.config(text="Runs: 0")
        self.outs_label.config(text="Wickets: 0 / 3")
        self.bot_label.config(text="Bot's Guess: ")
        self.toss_label.config(text="Toss Result: ")

        self.scorecard_text.delete(1.0, tk.END)
        self.scorecards_text.delete(1.0, tk.END)

        # Enable/Disable Buttons on Reset Game
        self.enable_toss_buttons()
        self.disable_bat_bowl_buttons()
        self.disable_runs_buttons()
        self.disable_batting_buttons()
        self.disable_bowling_buttons()

    
# Create the main window
window = tk.Tk()

# Create the Hand Cricket game instance
game = HandCricketGame(window)

# Run the GUI event loop
window.mainloop()