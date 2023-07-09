import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

class HandCricketGame:
    def __init__(self, window):
        self.window = window
        self.window.title("Virtual Cricket Game")

        # ---------GUI elements---------
        # Left Panel
        self.left_panel = tk.Frame(window)
        self.left_panel.pack(side="left", padx=10)

        # Right Panel
        self.right_panel = tk.Frame(window)
        self.right_panel.pack(side="left", padx=10)

        #-----right pannel elements-----
        # Match Mode
        self.match_mode_label = tk.Label(self.right_panel, text="Match Mode:", font=("Arial", 10, "bold"))
        self.match_mode_label.pack(pady=3)

        self.match_mode_frame = tk.Frame(self.right_panel)
        self.match_mode_frame.pack(pady=3)

        self.match_mode_buttons = []
        for mode in ["T20", "ODI", "Test", "Custom"]:
            button = tk.Button(self.match_mode_frame, text=mode, command=lambda m=mode: self.choose_match_mode(m),
                               font=("Arial", 10))
            button.pack(side="left", padx=5)
            self.match_mode_buttons.append(button)

        # Choose Wickets
        self.choose_wickets_label = tk.Label(self.right_panel, text="Choose Wickets:", font=("Arial", 10, "bold"))
        self.choose_wickets_label.pack(pady=3)

        self.choose_wickets_frame = tk.Frame(self.right_panel)
        self.choose_wickets_frame.pack(pady=3)

        self.choose_wickets_buttons = []
        for wicks in ["3", "5", "10", "Custom"]:
            button = tk.Button(self.choose_wickets_frame, text=wicks, command=lambda w=wicks: self.choose_wickets(w),
                               font=("Arial", 10))
            button.pack(side="left", padx=5)
            self.choose_wickets_buttons.append(button)

        # Toss Result
        self.toss_label = tk.Label(self.right_panel, text="Toss Result:", font=("Arial", 10, "bold"))
        self.toss_label.pack(pady=3)

        # Toss buttons
        self.toss_buttons_frame = tk.Frame(self.right_panel)
        self.toss_buttons_frame.pack(pady=3)

        self.toss_buttons = []
        for option in ["Heads", "Tails"]:
            button = tk.Button(self.toss_buttons_frame, text=option, command=lambda o=option: self.choose_toss_option(o),
                               font=("Arial", 10))
            button.pack(side="left", padx=3)
            self.toss_buttons.append(button)

        # Choose Batting-Bowling
        self.choose_batting_bowling_label = tk.Label(self.right_panel, text="Choose Batting / Bowling:",
                                                     font=("Arial", 10, "bold"))
        self.choose_batting_bowling_label.pack(pady=3)

        # Batting/Bowling Frame
        self.batting_bowling_button_frame = tk.Frame(self.right_panel)
        self.batting_bowling_button_frame.pack(pady=3)

        # Batting buttons
        self.choose_batting_buttons = []
        for option in ["Batting"]:
            button = tk.Button(self.batting_bowling_button_frame, text=option, command=lambda option=option:
                               self.select_bat(), font=("Arial", 10))
            button.pack(side="left", padx=5)
            self.choose_batting_buttons.append(button)
        # Bowling buttons
        self.choose_bowling_buttons = []
        for option in ["Bowling"]:
            button = tk.Button(self.batting_bowling_button_frame, text=option, command=lambda option=option:
                               self.select_bowl(), font=("Arial", 10))
            button.pack(side="left", padx=5)
            self.choose_bowling_buttons.append(button)

        # Your input to Batting or Bowling
        self.runs_buttons_label = tk.Label(self.right_panel, text="Your Input:", font=("Arial", 12, "bold"))
        self.runs_buttons_label.pack(pady=3)

        # Runs buttons
        self.runs_buttons_frame = tk.Frame(self.right_panel)
        self.runs_buttons_frame.pack(pady=3)

        self.run_buttons = []
        for i in range(7):
            button = tk.Button(self.runs_buttons_frame, text=str(i), command=lambda r=i: 
                               self.user_bat_bowl(r), font=("Arial", 10))
            button.pack(side="left", padx=5)
            self.run_buttons.append(button)

        # Additional GUI elements for batting shots
        self.batting_shots_label = tk.Label(self.right_panel, text="Batting Shots:", font=("Arial", 12, "bold"))
        self.batting_shots_label.pack(pady=3)

        self.batting_shots_frame = tk.Frame(self.right_panel)
        self.batting_shots_frame.pack(pady=3)

        self.batting_shots = ["Defensive Shot", "Attacking Shot", "Lofted Shot"]
        self.advanced_batting_buttons = []
        for shot in self.batting_shots:
            button = tk.Button(self.batting_shots_frame, text=shot, command=lambda s=shot: self.user_bat_with_shot(s),
                               font=("Arial", 10))
            button.pack(side="left", padx=5)
            self.advanced_batting_buttons.append(button)

        # Additional GUI elements for bowling variations
        self.bowling_variations_label = tk.Label(self.right_panel, text="Bowling Variations:",
                                                 font=("Arial", 12, "bold"))
        self.bowling_variations_label.pack(pady=3)

        self.bowling_variations_frame = tk.Frame(self.right_panel)
        self.bowling_variations_frame.pack(pady=3)

        self.bowling_variations = ["Fast Bowling", "Spin Bowling", "Swing Bowling"]
        self.advanced_bowling_buttons = []
        for variation in self.bowling_variations:
            button = tk.Button(self.bowling_variations_frame, text=variation,
                               command=lambda v=variation: self.bot_bowl_with_variation(v), font=("Arial", 10))
            button.pack(side="left", padx=5)
            self.advanced_bowling_buttons.append(button)

        # Reset Button
        self.reset_button = tk.Button(self.right_panel, text="Reset", command=self.reset_game, font=("Arial", 12))
        self.reset_button.pack(pady=10)

        #-----left pannel elements-----
        # Hand Gesture Displays
        self.gesture_frame = tk.Frame(self.left_panel)
        self.gesture_frame.pack(pady=3)

        # Player Gesture
        self.player_gesture_label = tk.Label(self.gesture_frame, text="Player's Input:",
                                             font=("Arial", 12, "bold"))
        self.player_gesture_label.grid(row=0, column=0)

        self.player_gesture_image = tk.Label(self.gesture_frame)
        self.player_gesture_image.grid(row=1, column=0, padx=15)

        # Bot Gesture
        self.bot_gesture_label = tk.Label(self.gesture_frame, text="Bot's Guess:",
                                          font=("Arial", 12, "bold"))
        self.bot_gesture_label.grid(row=0, column=1)

        self.bot_gesture_image = tk.Label(self.gesture_frame)
        self.bot_gesture_image.grid(row=1, column=1, padx=15)

        # Actual Scorecard
        self.scorecards_label = tk.Label(self.left_panel, text="Actual Scorecard:", font=("Arial", 12, "bold"))
        self.scorecards_label.pack(pady=3)

        self.scorecards_text = tk.Text(self.left_panel, width=50, height=3, font=("Arial", 10))
        self.scorecards_text.pack()

        # Commentry Box
        self.commentry_label = tk.Label(self.left_panel, text="Commentry Box:", font=("Arial", 12, "bold"))
        self.commentry_label.pack(pady=3)

        self.commentary_text = tk.Text(self.left_panel, width=50, height=4, font=("Arial", 10))
        self.commentary_text.pack(pady=3)

        # Scorecards Frame
        self.scorecards_frame = tk.Frame(self.left_panel)
        self.scorecards_frame.pack(pady=3)

        # Batsman Scorecard
        self.batsman_scorecard_label = tk.Label(self.scorecards_frame, text="Batsman Scorecard:",
                                                font=("Arial", 12, "bold"))
        self.batsman_scorecard_label.grid(row=0, column=0)

        self.batsman_scorecard_text = tk.Text(self.scorecards_frame, width=30, height=7, font=("Arial", 10))
        self.batsman_scorecard_text.grid(row=1, column=0, padx=10)

        # Bowler Scorecard
        self.bowler_scorecard_label = tk.Label(self.scorecards_frame, text="Bowler Scorecard:",
                                               font=("Arial", 12, "bold"))
        self.bowler_scorecard_label.grid(row=0, column=1)

        self.bowler_scorecard_text = tk.Text(self.scorecards_frame, width=30, height=7, font=("Arial", 10))
        self.bowler_scorecard_text.grid(row=1, column=1, padx=10)

        # Current Runs, Overs, and Wickets
        self.runs_wickets_frame = tk.Frame(self.left_panel)
        self.runs_wickets_frame.pack(pady=3)

        self.runs_label = tk.Label(self.runs_wickets_frame, text="Runs: 0", font=("Arial", 12))
        self.runs_label.pack(side="left", padx=3)

        self.wicks_label = tk.Label(self.runs_wickets_frame, text="Wickets: 0", font=("Arial", 12))
        self.wicks_label.pack(side="left", padx=3)

        self.overs_label = tk.Label(self.runs_wickets_frame, text="Overs: 0", font=("Arial", 12))
        self.overs_label.pack(side="left", padx=3)
        
        # Call Start Game method
        self.start_game()
        self.update_default_hand_gestures()
        
    def start_game(self):
        
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
        
        # Match mode variables
        self.match_mode = ""
        self.custom_overs = 0
        self.custom_wicks = 0

        # Player and Bot Names
        self.player_names = ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5",
                             "Player 6", "Player 7", "Player 8", "Player 9", "Player 10"]
        self.bot_names = ["Bot 1", "Bot 2", "Bot 3", "Bot 4", "Bot 5",
                          "Bot 6", "Bot 7", "Bot 8", "Bot 9", "Bot 10"]

        # Initially Enable/Disable Buttons
        self.enable_match_mode_buttons()
        self.disable_choose_wicks_buttons()
        self.disable_toss_buttons()
        self.disable_runs_buttons()
        self.disable_choose_batting_buttons()
        self.disable_choose_bowling_buttons()
        self.disable_advanced_batting_buttons()
        self.disable_advanced_bowling_buttons()

    def choose_match_mode(self, mode):
        if mode == "T20":
            self.match_mode = "T20"
            self.custom_overs = 20
            self.show_message("You choose T20 format, your custom over will " + str(self.custom_overs) + " overs")
        elif mode == "ODI":
            self.match_mode = "ODI"
            self.custom_overs = 50
            self.show_message("You choose ODI format, your custom over will " + str(self.custom_overs) + " overs")
        elif mode == "Test":
            self.match_mode = "Test"
            self.custom_overs = 999
            self.show_message("You choose Test format, your custom over will " + str(self.custom_overs) + " overs")
        elif mode == "Custom":
            self.match_mode = "Custom"
            # Display a dialog box to input the number of overs
            self.custom_overs = self.get_custom_overs()

        self.update_overs_label()
        self.update_match_mode_label()
        self.disable_match_mode_buttons()
        self.enable_choose_wicks_buttons()

    def get_custom_overs(self):
        # Create a dialog box or an entry field to get the number of overs for custom mode
        dialog_window = tk.Toplevel(self.window)
        dialog_window.title("Custom Overs")

        # Label and entry field for custom overs
        custom_overs_label = tk.Label(dialog_window, text="Enter the number of overs:")
        custom_overs_label.pack(pady=10)
        custom_overs_entry = tk.Entry(dialog_window)
        custom_overs_entry.pack()

        # Submit button
        submit_button = tk.Button(dialog_window, text="Submit", command=lambda: self.submit_custom_overs(dialog_window, custom_overs_entry))
        submit_button.pack(pady=10)

        # Focus the entry field
        custom_overs_entry.focus_set()

        # Run the dialog window event loop
        dialog_window.mainloop()

        return self.custom_overs
    
    def submit_custom_overs(self, dialog_window, custom_overs_entry):
        overs = custom_overs_entry.get()
        if overs.isdigit() and int(overs) > 0:
            self.custom_overs = int(overs)
            dialog_window.destroy()
            self.update_overs_label()  # Update the overs label with the custom overs value
            self.update_match_mode_label()
            self.enable_choose_wicks_buttons()  # Enable the choose wicks after custom overs submission
            self.disable_match_mode_buttons()  # Disable the match mode buttons after custom overs submission
        else:
            messagebox.showerror("Invalid Input", "Please enter a valid number of overs.")

    def update_overs_label(self):
        self.overs_label.config(text="Overs: 0 / " + str(self.custom_overs))

    def update_wicks_label(self):
        self.wicks_label.config(text="Wickets: 0 / " + str(self.custom_wicks))
        self.choose_wickets_label.config(text="Wickets: " + str(self.custom_wicks))
    
    def update_match_mode_label(self):
        if self.match_mode == "Custom":
            self.match_mode_label.config(text= "Match Mode: " + self.match_mode + " (" + str(self.custom_overs) + " overs)")
        else:
            self.match_mode_label.config(text= "Match Mode: " + self.match_mode)

    def choose_wickets(self, wicks):
        if wicks == "3":
            self.custom_wicks = 3
            self.show_message("You choose 3 wicket format")
        elif wicks == "5":
            self.custom_wicks = 5
            self.show_message("You choose 5 wicket format")
        elif wicks == "10":
            self.custom_wicks = 10
            self.show_message("You choose 10 wicket format")
        elif wicks == "Custom":
            # Display a dialog box to input the number of overs
            self.custom_wicks = self.get_custom_wicks()

        self.update_wicks_label()
        self.disable_choose_wicks_buttons()
        self.enable_toss_buttons()

    def get_custom_wicks(self):
        # Create a dialog box or an entry field to get the number of overs for custom mode
        dialog_window = tk.Toplevel(self.window)
        dialog_window.title("Custom Wickets")

        # Label and entry field for custom overs
        custom_wicks_label = tk.Label(dialog_window, text="Enter the number of wickets:")
        custom_wicks_label.pack(pady=10)
        custom_wicks_entry = tk.Entry(dialog_window)
        custom_wicks_entry.pack()

        # Submit button
        submit_button = tk.Button(dialog_window, text="Submit", command=lambda: self.submit_custom_wicks(dialog_window, custom_wicks_entry))
        submit_button.pack(pady=10)

        # Focus the entry field
        custom_wicks_entry.focus_set()

        # Run the dialog window event loop
        dialog_window.mainloop()

        return self.custom_wicks
    
    def submit_custom_wicks(self, dialog_window, custom_wicks_entry):
        wicks = custom_wicks_entry.get()
        if wicks.isdigit() and int(wicks) > 0:
            self.custom_wicks = int(wicks)
            dialog_window.destroy()
            self.update_wicks_label()
            self.disable_choose_wicks_buttons()
            self.enable_toss_buttons()
        else:
            messagebox.showerror("Invalid Input", "Please enter a valid number of wickets.")

    def choose_toss_option(self, option):
        toss_options = ["Heads", "Tails"]
        self.toss_result = random.choice(toss_options)
        self.toss_label.config(text="Toss Result: " + self.toss_result)

        if option == self.toss_result:
            self.user_won_toss = True
            # messagebox.showinfo("Toss Result", "You won the toss! Choose Batting or Bowling.")
            self.show_message("Toss Result: You won the toss! Choose Batting or Bowling.")
            self.enable_choose_batting_buttons()
            self.enable_choose_bowling_buttons()
        else:
            self.user_won_toss = False
            # messagebox.showinfo("Toss Result", "You lost the toss! Bot will choose Batting or Bowling.")
            self.show_message("Toss Result: You lost the toss! Bot will choose Batting or Bowling.")
            bot_choice = random.choice(["Bat", "Bowl"])
            if bot_choice == "Bat":
                self.disable_choose_batting_buttons()
                self.enable_choose_bowling_buttons()
                # messagebox.showinfo("Bot's Choice", "Bot has chosen to bat.")
                self.show_message("Bot's Choice: Bot has chosen to bat.")
            else:
                self.disable_choose_bowling_buttons()
                self.enable_choose_batting_buttons()
                # messagebox.showinfo("Bot's Choice", "Bot has chosen to bowl.")
                self.show_message("Bot's Choice: Bot has chosen to bowl.")

        self.disable_toss_buttons()
    
    def select_bat(self):
        self.batting_enabled = True
        self.bowling_enabled = False
        self.enable_runs_buttons()
        self.disable_choose_batting_buttons()
        self.disable_choose_bowling_buttons()
        self.enable_advanced_batting_buttons()
        self.disable_advanced_bowling_buttons()
        self.show_message("Your batting sessions starts")

    def select_bowl(self):
        self.batting_enabled = False
        self.bowling_enabled = True
        self.enable_runs_buttons()
        self.disable_choose_batting_buttons()
        self.disable_choose_bowling_buttons()
        self.disable_advanced_batting_buttons()
        self.enable_advanced_bowling_buttons()
        self.show_message("Your bowling sessions starts")
    
    def user_bat_bowl(self, runs):
        self.bot_guess = random.randint(0, 6)

        # Update gestures before performing any calculations
        self.update_hand_gestures(runs, self.bot_guess)
        self.player_gesture_label.config(text="Player's Input: "+ str(runs))
        self.bot_gesture_label.config(text="Bot's Guess: "+ str(self.bot_guess))

        if self.batting_enabled:

            if runs != self.bot_guess:
                self.runs += runs
                self.runs_label.config(text="Your Runs: " + str(self.runs))

            if runs == self.bot_guess:
                self.wickets += 1
                self.wicks_label.config(text="Your Wickets: " + str(self.wickets) + " / " + str(self.custom_wicks))
                self.scorecard.append("Out")
            else:
                self.scorecard.append("Player: " + str(runs))

            self.bot_balls_bowled += 1
            if self.bot_balls_bowled % 6 == 0:  # Check if the over is complete
                self.bot_overs += 1
                self.bot_balls_bowled = 0

            self.overs_label.config(text="Overs: " + f"{self.bot_overs}.{self.bot_balls_bowled % 6}" + " / " + str(self.custom_overs))

            self.update_batsman_scorecard()
            self.update_bowler_scorecard()
            self.update_actual_scorecard()

            # Check if overs limit reached or all wickets down
            if self.wickets == self.custom_wicks:  
                self.innings_count += 1
                self.between_innings()
                self.disable_choose_batting_buttons()
                if self.innings_count == 0:
                    self.show_message("Start New Game!")
                else:
                    # messagebox.showinfo("Innings Over", "All your's wickets are down. Innings is over!")
                    self.show_message("Innings Over, All your's wickets are down. Innings is over!")
            if self.bot_overs >= self.custom_overs:
                self.innings_count += 1
                self.between_innings()
                self.disable_choose_batting_buttons()
                if self.innings_count == 0:
                    self.show_message("Start New Game!")
                else:
                    # messagebox.showinfo("Innings Over", "Your custom overs reached. Innings is over!")
                    self.show_message("Innings Over, Your custom overs reached. Innings is over!")
                    
        elif self.bowling_enabled:

            if runs != self.bot_guess:
                self.bot_runs += self.bot_guess
                self.runs_label.config(text="Bot's Runs: " + str(self.bot_runs))

            if runs == self.bot_guess:
                self.bot_wickets += 1
                self.wicks_label.config(text="Bot's Wickets: " + str(self.bot_wickets) + " / " + str(self.custom_wicks))
                self.scorecard.append("Bot Out")
            else:
                self.scorecard.append("Bot: " + str(self.bot_guess))
            
            self.balls_bowled += 1
            if self.balls_bowled % 6 == 0:  # Check if the over is complete
                self.overs += 1
                self.balls_bowled = 0

            self.overs_label.config(text="Overs: " + f"{self.overs}.{self.balls_bowled % 6}" + " / " + str(self.custom_overs))

            self.update_batsman_scorecard()
            self.update_bowler_scorecard()
            self.update_actual_scorecard()

            # Check if overs limit reached or all wickets down
            if self.bot_wickets == self.custom_wicks:
                self.innings_count += 1
                self.between_innings()
                self.disable_choose_bowling_buttons()

                if self.innings_count == 0:
                    self.show_message("Start New Game!")
                else:
                    # messagebox.showinfo("Innings Over", "All bot's wickets are down. Innings is over!")
                    self.show_message("Innings Over, All bot's wickets are down. Innings is over!")
            if self.overs >= self.custom_overs:
                self.innings_count += 1
                self.between_innings()
                self.disable_choose_bowling_buttons()

                if self.innings_count == 0:
                    self.show_message("Start New Game!")
                else:
                    # messagebox.showinfo("Innings Over", "Bot's custom overs reached. Innings is over!")
                    self.show_message("Innings Over, Bot's custom overs reached. Innings is over!")
    
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
        self.wicks_label.config(text="Wickets: 0 /" + str(self.custom_wicks))
        self.overs_label.config(text="Overs: 0 / " + str(self.custom_overs))
        self.player_gesture_label.config(text="Player's Guess: ")
        self.bot_gesture_label.config(text="Bot's Guess: ")

        if self.innings_count == 1:
            messagebox.showinfo("Between Innings", "First innings is over!\n\n" + inning_scorecard)
            self.show_message("Between Innings, First innings is over!\n" + inning_scorecard)
            if self.batting_enabled:
                self.enable_choose_bowling_buttons()
            else:
                self.enable_choose_batting_buttons()
        else:
            messagebox.showinfo("Between Innings", "Second innings is over!\n\n" + inning_scorecard)
            self.show_message("Between Innings, Second innings is over!\n" + inning_scorecard)

        self.calculate_target_score()
        
        self.disable_runs_buttons()
        self.disable_advanced_batting_buttons()
        self.disable_advanced_bowling_buttons()

        self.check_game_over() #Checks if Game Over
        self.update_default_hand_gestures()

    def update_batsman_scorecard(self):
        self.batsman_scorecard_text.delete(1.0, tk.END)
        inning_scorecard = ""
        player_score = 0
        player_balls = 0
        bot_score = 0
        bot_balls = 0

        for score in self.scorecard:
            if score == "Out":
                inning_scorecard += "Player: " + str(player_score) + " (" + str(player_balls) + " balls)\n"
                player_score = 0
                player_balls = 0
            elif score == "Bot Out":
                inning_scorecard += "Bot: " + str(bot_score) + " (" + str(bot_balls) + " balls)\n"
                bot_score = 0
                bot_balls = 0
            elif score.startswith("Player"):
                player_score += int(score.split(": ")[1])
                player_balls += 1
            elif score.startswith("Bot"):
                bot_score += int(score.split(": ")[1])
                bot_balls += 1

        if self.batting_enabled:
            inning_scorecard += "Player: " + str(player_score) + " (" + str(player_balls) + " balls)\n"
        else:
            inning_scorecard += "Bot: " + str(bot_score) + " (" + str(bot_balls) + " balls)\n"

        self.batsman_scorecard_text.insert(tk.END, inning_scorecard)
    
    def update_bowler_scorecard(self):
        # to be implemented
        pass

    def get_inning_scorecard(self):
        inning_scorecard = ""
        player_score = 0
        player_balls = 0
        bot_score = 0
        bot_balls = 0

        for score in self.scorecard:
            if score.startswith("Player"):
                score_parts = score.split(": ")
                if len(score_parts) > 1:
                    player_score += int(score_parts[1])
                    player_balls += 1
            elif score.startswith("Bot"):
                score_parts = score.split(": ")
                if len(score_parts) > 1:
                    bot_score += int(score_parts[1])
                    bot_balls += 1

        inning_scorecard += "Player: " + str(player_score) + " (" + str(player_balls) + " balls)\n"
        inning_scorecard += "Bot: " + str(bot_score) + " (" + str(bot_balls) + " balls)\n"

        return inning_scorecard

    def calculate_target_score(self):
        self.target_score = self.runs + 1
    
    def get_actual_scorecard(self):
        return f"Your Score: Runs: {self.runs} - Overs: {self.bot_overs}.{self.bot_balls_bowled % 6} -  Wickets: {self.wickets}" + "\n" + f"Bot's Score: Runs: {self.bot_runs} - Overs: {self.overs}.{self.balls_bowled % 6} -  Wickets: {self.bot_wickets}"

    def update_actual_scorecard(self):
        self.scorecards_text.delete(1.0, tk.END)
        self.scorecards_text.insert(tk.END, self.get_actual_scorecard())

    def show_message(self, message):
        self.commentary_text.delete(1.0, tk.END)
        self.commentary_text.insert(tk.END, message)

    def update_hand_gestures(self, player_gesture, bot_gesture):
        # Update Player's Hand Gesture
        player_image_path = f"hand_gestures/run_{player_gesture}.png"
        player_image = Image.open(player_image_path)
        player_image = player_image.resize((100, 100))
        player_photo = ImageTk.PhotoImage(player_image)
        self.player_gesture_image.configure(image=player_photo)
        self.player_gesture_image.image = player_photo

        # Update Bot's Hand Gesture
        bot_image_path = f"hand_gestures/run_{bot_gesture}.png"
        bot_image = Image.open(bot_image_path)
        bot_image = bot_image.resize((100, 100))
        bot_photo = ImageTk.PhotoImage(bot_image)
        self.bot_gesture_image.configure(image=bot_photo)
        self.bot_gesture_image.image = bot_photo

    def update_default_hand_gestures(self):
        # Update Player's Hand Gesture to default
        player_image = Image.open("hand_gestures/run_default.png")
        player_image = player_image.resize((100, 100))
        player_photo = ImageTk.PhotoImage(player_image)
        self.player_gesture_image.configure(image=player_photo)
        self.player_gesture_image.image = player_photo

        # Update Bot's Hand Gesture to default
        bot_image = Image.open("hand_gestures/run_default.png")
        bot_image = bot_image.resize((100, 100))
        bot_photo = ImageTk.PhotoImage(bot_image)
        self.bot_gesture_image.configure(image=bot_photo)
        self.bot_gesture_image.image = bot_photo

    def enable_match_mode_buttons(self):
        for button in self.match_mode_buttons:
            button.config(state="normal")

    def disable_match_mode_buttons(self):
        for button in self.match_mode_buttons:
            button.config(state="disabled")

    def enable_choose_wicks_buttons(self):
        for button in self.choose_wickets_buttons:
            button.config(state="normal")

    def disable_choose_wicks_buttons(self):
        for button in self.choose_wickets_buttons:
            button.config(state="disabled")

    def enable_toss_buttons(self):
        for button in self.toss_buttons:
            button.config(state="normal")

    def disable_toss_buttons(self):
        for button in self.toss_buttons:
            button.config(state="disabled")

    def enable_runs_buttons(self):
        for button in self.run_buttons:
            button.config(state="normal")

    def disable_runs_buttons(self):
        for button in self.run_buttons:
            button.config(state="disabled")

    def enable_choose_batting_buttons(self):
        for button in self.choose_batting_buttons:
            button.config(state="normal")

    def disable_choose_batting_buttons(self):
        for button in self.choose_batting_buttons:
            button.config(state="disabled")

    def enable_choose_bowling_buttons(self):
        for button in self.choose_bowling_buttons:
            button.config(state="normal")

    def disable_choose_bowling_buttons(self):
        for button in self.choose_bowling_buttons:
            button.config(state="disabled")
    
    def enable_advanced_batting_buttons(self):
        for button in self.advanced_batting_buttons:
            button.config(state="normal")

    def disable_advanced_batting_buttons(self):
        for button in self.advanced_batting_buttons:
            button.config(state="disabled")

    def enable_advanced_bowling_buttons(self):
        for button in self.advanced_bowling_buttons:
            button.config(state="normal")

    def disable_advanced_bowling_buttons(self):
        for button in self.advanced_bowling_buttons:
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
            self.show_message("Game Over f{winner_message}\n\n{inning_scorecard}")
            
            # Reset Game
            self.reset_game() 

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

        #Configure text label as default on Reset Game
        self.match_mode_label.config(text= "Match Mode:")
        self.toss_label.config(text="Toss Result: ")
        self.runs_label.config(text="Runs: 0")
        self.wicks_label.config(text="Wickets: 0")
        self.overs_label.config(text="Overs: 0")
        self.player_gesture_label.config(text="Player's Input: ")
        self.bot_gesture_label.config(text="Bot's Guess: ")
        self.choose_wickets_label.config(text="Choose Wickets:")

        # Delete text fields text on Reset Game
        self.scorecards_text.delete(1.0, tk.END)
        self.commentary_text.delete(1.0, tk.END)
        self.batsman_scorecard_text.delete(1.0, tk.END)
        self.bowler_scorecard_text.delete(1.0, tk.END)

        # Enable/Disable Buttons on Reset Game
        self.enable_match_mode_buttons()
        self.disable_choose_wicks_buttons()
        self.disable_toss_buttons()
        self.disable_choose_batting_buttons()
        self.disable_choose_bowling_buttons()
        self.disable_runs_buttons()
        self.disable_advanced_batting_buttons()
        self.disable_advanced_bowling_buttons()

        self.update_default_hand_gestures()

    
# Create the main window
window = tk.Tk()

# Create the Hand Cricket game instance
game = HandCricketGame(window)

# Run the GUI event loop
window.mainloop()