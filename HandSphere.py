import tkinter as tk
from tkinter import messagebox
import random

class HandCricketGame:
    def __init__(self, window):
        self.window = window
        self.window.title("Cricket Game")

        # Create GUI elements
        self.toss_label = tk.Label(window, text="Toss Result: ")
        self.toss_label.pack(pady=3)

        self.option_buttons_frame = tk.Frame(window)
        self.option_buttons_frame.pack(pady=3)

        self.runs_buttons_label = tk.Label(window, text="Your input to Batting or Bowling:")
        self.runs_buttons_label.pack(pady=3)

        # Runs buttons
        self.runs_buttons_frame = tk.Frame(window)
        self.runs_buttons_frame.pack(pady=3)

        self.runs_label = tk.Label(window, text="Runs: 0")
        self.runs_label.pack(pady=3)

        self.outs_label = tk.Label(window, text="Wickets: 0 / 3")
        self.outs_label.pack(pady=3)

        self.bot_label = tk.Label(window, text="Bot's Guess: ")
        self.bot_label.pack(pady=3)

        self.reset_button = tk.Button(window, text="Reset", command=self.reset_game)
        self.reset_button.pack(pady=3)

        self.batting_enabled = False
        self.bowling_enabled = False

        # Actual Scorecard
        self.scorecards_label = tk.Label(window, text="Actual Scorecard:")
        self.scorecards_label.pack(pady=10)

        self.scorecards_text = tk.Text(window, width=40, height=2)
        self.scorecards_text.pack()

        # Scorecard
        self.scorecard_label = tk.Label(window, text="Scorecard:")
        self.scorecard_label.pack(pady=3)

        self.scorecard_text = tk.Text(window, width=30, height=10)
        self.scorecard_text.pack()

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

        # Toss variables
        self.toss_result = ""
        self.user_won_toss = False

        # Toss buttons
        self.toss_buttons = []
        for option in ["Heads", "Tails"]:
            button = tk.Button(self.option_buttons_frame, text=option, command=lambda o=option: self.choose_toss_option(o))
            button.pack(side="left", padx=5)
            self.toss_buttons.append(button)

        # Batting/bowling buttons
        self.bat_bowl_buttons = []
        for option in ["Batting", "Bowling"]:
            button = tk.Button(self.option_buttons_frame, text=option, command=lambda option=option: self.choose_bat_bowl_option(option))
            button.pack(side="left", padx=5)
            self.bat_bowl_buttons.append(button)

        # Runs Buttons
        self.run_buttons = []
        for i in range(7):
            button = tk.Button(self.runs_buttons_frame, text=str(i), command=lambda r=i: self.user_bat_bowl(r))
            button.pack(side="left", padx=5)
            self.run_buttons.append(button)

        # Initially Enable/Disable Buttons
        self.enable_toss_buttons()
        self.disable_runs_buttons()
        self.disable_bat_bowl_buttons()
    
    def user_bat_bowl(self, runs):
        if self.batting_enabled:
            self.bot_guess = random.randint(0, 6)

            self.runs += runs
            self.runs_label.config(text="Runs: " + str(self.runs))

            self.bot_label.config(text="Bot's Guess: " + str(self.bot_guess))

            if runs == self.bot_guess:
                self.wickets += 1
                self.outs_label.config(text="Wickets: " + str(self.wickets) + " / 3")
                self.scorecard.append("Out")
            else:
                self.scorecard.append("Player: " + str(runs))

            self.balls_bowled += 1
            if self.balls_bowled % 6 == 0:  # Check if the over is complete
                self.overs += 1
                self.balls_bowled = 0

            self.update_scorecard()
            self.update_actual_scorecard()

            if self.wickets == 3:
                messagebox.showinfo("Innings Over", "All wickets are down. Innings is over!")
                if self.batting_enabled:
                    self.between_innings()
                else:
                    self.game_over()
        elif self.bowling_enabled:
            self.bot_guess = random.randint(0, 6)

            self.bot_runs += runs
            self.runs_label.config(text="Bot's Runs: " + str(self.bot_runs))

            self.bot_label.config(text="Bot's Guess: " + str(self.bot_guess))

            if runs == self.bot_guess:
                self.bot_wickets += 1
                self.outs_label.config(text="Bot's Wickets: " + str(self.bot_wickets) + " / 3")
                self.scorecard.append("Bot Out")
            else:
                self.scorecard.append("Bot: " + str(runs))

            self.balls_bowled += 1
            if self.balls_bowled % 6 == 0:  # Check if the over is complete
                self.overs += 1
                self.balls_bowled = 0

            self.update_scorecard()
            self.update_actual_scorecard()

            if self.bot_wickets == 3:
                messagebox.showinfo("Innings Over", "All bot's wickets are down. Innings is over!")
                if self.batting_enabled:
                    self.game_over()
                else:
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
    
    # def show_bat_bowl_options(self):
    #     self.bat_bowl_label.pack(pady=3)

    #     if self.user_won_toss:
    #         self.bat_button = tk.Button(self.bat_bowl_buttons_frame, text="Batting", command=self.select_bat)
    #         self.bat_button.pack(side="left", padx=5)
    #         self.bat_bowl_buttons.append(self.bat_button)

    #         self.bowl_button = tk.Button(self.bat_bowl_buttons_frame, text="Bowling", command=self.select_bowl)
    #         self.bowl_button.pack(side="left", padx=5)
    #         self.bat_bowl_buttons.append(self.bowl_button)
    #     else:
    #         self.bat_button = tk.Button(self.bat_bowl_buttons_frame, text="Batting", command=self.select_bat, state="disabled")
    #         self.bat_button.pack(side="left", padx=5)
    #         self.bat_bowl_buttons.append(self.bat_button)

    #         self.bowl_button = tk.Button(self.bat_bowl_buttons_frame, text="Bowling", command=self.select_bowl, state="disabled")
    #         self.bowl_button.pack(side="left", padx=5)
    #         self.bat_bowl_buttons.append(self.bowl_button)

    #     self.enable_runs_buttons()

    def select_bat(self):
        self.batting_enabled = True
        self.bowling_enabled = False
        #Button enable/disable called in AdvancedHandCricketGame Clas

    def select_bowl(self):
        self.batting_enabled = False
        self.bowling_enabled = True
        #Button enable/disable called in AdvancedHandCricketGame Class
        
    def choose_bat_bowl_option(self, option):
        self.disable_bat_bowl_buttons()

        if option == "Batting":
            self.select_bat()
        else:
            self.select_bowl()


    def first_innings(self):
        self.enable_runs_buttons()
        self.runs = 0
        self.wickets = 0
        self.bot_runs = 0
        self.bot_wickets = 0
        self.bot_guess = 0
        self.scorecard = []
        self.runs_label.config(text="Your Runs: 0")
        self.outs_label.config(text="Your Wickets: 0 / 3")
        self.bot_label.config(text="Bot's Guess: ")
        self.update_scorecard()
        self.update_actual_scorecard()
        messagebox.showinfo("First Innings", "Your batting innings begins!")

    def second_innings(self):
        self.enable_runs_buttons()
        self.runs = 0
        self.wickets = 0
        self.bot_runs = 0
        self.bot_wickets = 0
        self.bot_guess = 0
        self.scorecard = []
        self.runs_label.config(text="Bot's Runs: 0")
        self.outs_label.config(text="Bot's Wickets: 0 / 3")
        self.bot_label.config(text="Bot's Guess: ")
        self.update_scorecard()
        self.update_actual_scorecard()
        messagebox.showinfo("Second Innings", "Your bowling innings begins!")

    def between_innings(self):
        inning_scorecard = self.get_inning_scorecard()

        self.runs_label.config(text="Runs: " + str(self.runs))
        self.outs_label.config(text="Wickets: " + str(self.wickets) + " / 3")
        self.bot_label.config(text="Bot's Guess: ")

        if self.batting_enabled:
            messagebox.showinfo("Between Innings", "First innings is over!\n\n" + inning_scorecard)
        else:
            messagebox.showinfo("Between Innings", "Second innings is over!\n\n" + inning_scorecard)

        self.calculate_target_score()

        self.enable_bat_bowl_buttons()
        self.disable_runs_buttons()

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
        return f"Runs: {self.runs} - Overs: {self.overs}.{self.balls_bowled % 6} -  Wickets: {self.wickets}"

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


    def game_over(self):
        inning_scorecard = self.get_inning_scorecard()

        self.runs_label.config(text="Runs: " + str(self.runs))
        self.outs_label.config(text="Wickets: " + str(self.wickets) + " / 3")
        self.bot_label.config(text="Bot's Guess: ")

        player_total_runs = sum([int(score.split(": ")[1]) for score in self.scorecard if score.startswith("Player") and len(score.split(": ")) > 1])
        bot_total_runs = sum([int(score.split(": ")[1]) for score in self.scorecard if score.startswith("Bot") and len(score.split(": ")) > 1])

        if player_total_runs > bot_total_runs:
            winner_message = "You win!"
        elif player_total_runs < bot_total_runs:
            winner_message = "Bot wins!"
        else:
            winner_message = "It's a tie!"

        messagebox.showinfo("Game Over", f"{winner_message}\n\n{inning_scorecard}")

        self.disable_bat_bowl_buttons()


    def reset_game(self):
        self.runs = 0
        self.wickets = 0
        self.bot_runs = 0
        self.bot_wickets = 0
        self.balls_bowled = 0
        self.overs = 0
        self.bot_guess = 0
        self.scorecard = []
        self.target_score = 0

        self.batting_enabled = False
        self.bowling_enabled = False

        self.toss_result = ""
        self.user_won_toss = False

        self.runs_label.config(text="Runs: 0")
        self.outs_label.config(text="Wickets: 0 / 3")
        self.bot_label.config(text="Bot's Guess: ")
        self.toss_label.config(text="Toss Result: ")

        self.scorecard_text.delete(1.0, tk.END)

        # Enable/Disable Buttons on Reset Game
        self.enable_toss_buttons()
        self.disable_bat_bowl_buttons()
        self.disable_runs_buttons()


class AdvancedHandCricketGame(HandCricketGame):
    def __init__(self, window):
        super().__init__(window)
        
        # Additional GUI elements for batting shots
        self.batting_shots_label = tk.Label(window, text="Batting Shots:")
        self.batting_shots_label.pack(pady=10)
        
        self.batting_shots_frame = tk.Frame(window)
        self.batting_shots_frame.pack(pady=10)
        
        self.batting_shots = ["Defensive Shot", "Attacking Shot", "Lofted Shot"]
        self.batting_buttons = []
        for shot in self.batting_shots:
            button = tk.Button(self.batting_shots_frame, text=shot, command=lambda s=shot: self.user_bat_with_shot(s))
            button.pack(side="left", padx=5)
            self.batting_buttons.append(button)
        
        # Additional GUI elements for bowling variations
        self.bowling_variations_label = tk.Label(window, text="Bowling Variations:")
        self.bowling_variations_label.pack(pady=10)
        
        self.bowling_variations_frame = tk.Frame(window)
        self.bowling_variations_frame.pack(pady=10)
        
        self.bowling_variations = ["Fast Bowling", "Spin Bowling", "Swing Bowling"]
        self.bowling_buttons = []
        for variation in self.bowling_variations:
            button = tk.Button(self.bowling_variations_frame, text=variation, command=lambda v=variation: self.bot_bowl_with_variation(v))
            button.pack(side="left", padx=5)
            self.bowling_buttons.append(button)
        
        # Initially Enable/Disable Buttons
        self.disable_batting_buttons()
        self.disable_bowling_buttons()
    
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


    def reset_game(self):
        super().reset_game()
        self.disable_batting_buttons()
        self.disable_bowling_buttons()

    
# Create the main window
window = tk.Tk()

# Create the Advanced Hand Cricket game instance
game = AdvancedHandCricketGame(window)

# Run the GUI event loop
window.mainloop()