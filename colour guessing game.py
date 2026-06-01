import tkinter as tk
from tkinter import messagebox
import random

class ColorGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎨 Color Guessing Game 🎨")
        self.root.geometry("600x700")
        self.root.configure(bg='#2c3e50')
        
        # Game variables
        self.colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange"]
        self.color_hex = {
            "Red": "#e74c3c",
            "Blue": "#3498db", 
            "Green": "#2ecc71",
            "Yellow": "#f1c40f",
            "Purple": "#9b59b6",
            "Orange": "#e67e22"
        }
        self.user_wins = 0
        self.computer_wins = 0
        self.current_color = None
        
        # Setup GUI
        self.setup_gui()
        
    def setup_gui(self):
        # Title Frame
        title_frame = tk.Frame(self.root, bg='#2c3e50')
        title_frame.pack(pady=20)
        
        title_label = tk.Label(title_frame, text="🎨 COLOR GUESSING GAME 🎨", 
                               font=('Arial', 24, 'bold'), 
                               fg='#ecf0f1', bg='#2c3e50')
        title_label.pack()
        
        subtitle_label = tk.Label(title_frame, text="Can you guess the computer's color?", 
                                  font=('Arial', 12), 
                                  fg='#bdc3c7', bg='#2c3e50')
        subtitle_label.pack()
        
        # Score Frame
        score_frame = tk.Frame(self.root, bg='#34495e', relief=tk.RAISED, bd=2)
        score_frame.pack(pady=20, padx=20, fill=tk.X)
        
        self.user_score_label = tk.Label(score_frame, text=f"YOU: {self.user_wins}", 
                                         font=('Arial', 18, 'bold'), 
                                         fg='#2ecc71', bg='#34495e')
        self.user_score_label.pack(side=tk.LEFT, padx=30, pady=10)
        
        vs_label = tk.Label(score_frame, text="VS", 
                           font=('Arial', 16, 'bold'), 
                           fg='#e74c3c', bg='#34495e')
        vs_label.pack(side=tk.LEFT, padx=20)
        
        self.computer_score_label = tk.Label(score_frame, text=f"COMPUTER: {self.computer_wins}", 
                                             font=('Arial', 18, 'bold'), 
                                             fg='#e74c3c', bg='#34495e')
        self.computer_score_label.pack(side=tk.LEFT, padx=30, pady=10)
        
        # Computer's Choice Display (Hidden initially)
        computer_frame = tk.Frame(self.root, bg='#34495e', relief=tk.RAISED, bd=2)
        computer_frame.pack(pady=10, padx=20, fill=tk.X)
        
        computer_label = tk.Label(computer_frame, text="🤔 Computer is thinking... 🤔", 
                                  font=('Arial', 14), 
                                  fg='#bdc3c7', bg='#34495e')
        computer_label.pack(pady=10)
        
        # Color Display Frame
        self.display_frame = tk.Frame(self.root, bg='#ecf0f1', relief=tk.RAISED, bd=3, height=150)
        self.display_frame.pack(pady=20, padx=40, fill=tk.BOTH)
        self.display_frame.pack_propagate(False)
        
        self.display_label = tk.Label(self.display_frame, text="?", 
                                      font=('Arial', 48, 'bold'), 
                                      fg='#7f8c8d', bg='#ecf0f1')
        self.display_label.pack(expand=True)
        
        # Guess Frame
        guess_frame = tk.Frame(self.root, bg='#2c3e50')
        guess_frame.pack(pady=20)
        
        guess_label = tk.Label(guess_frame, text="Choose a color:", 
                               font=('Arial', 14, 'bold'), 
                               fg='#ecf0f1', bg='#2c3e50')
        guess_label.pack()
        
        # Color Buttons Frame
        button_frame = tk.Frame(self.root, bg='#2c3e50')
        button_frame.pack(pady=10, padx=20)
        
        # Create color buttons in a grid
        for i, color in enumerate(self.colors):
            btn = tk.Button(button_frame, text=color, 
                           font=('Arial', 12, 'bold'),
                           bg=self.color_hex[color], 
                           fg='white',
                           activebackground=self.color_hex[color],
                           activeforeground='white',
                           width=12, height=2,
                           command=lambda c=color: self.make_guess(c))
            row = i // 3
            col = i % 3
            btn.grid(row=row, column=col, padx=10, pady=5)
        
        # Action Buttons Frame
        action_frame = tk.Frame(self.root, bg='#2c3e50')
        action_frame.pack(pady=20)
        
        self.new_game_btn = tk.Button(action_frame, text="🔄 New Game", 
                                      font=('Arial', 12, 'bold'),
                                      bg='#3498db', fg='white',
                                      activebackground='#2980b9',
                                      command=self.new_game)
        self.new_game_btn.pack(side=tk.LEFT, padx=10)
        
        quit_btn = tk.Button(action_frame, text="❌ Quit", 
                            font=('Arial', 12, 'bold'),
                            bg='#e74c3c', fg='white',
                            activebackground='#c0392b',
                            command=self.quit_game)
        quit_btn.pack(side=tk.LEFT, padx=10)
        
        # Message Frame
        self.message_frame = tk.Frame(self.root, bg='#2c3e50', relief=tk.SUNKEN, bd=2)
        self.message_frame.pack(pady=20, padx=20, fill=tk.X)
        
        self.message_label = tk.Label(self.message_frame, text="✨ Click on a color to start guessing! ✨", 
                                      font=('Arial', 12, 'italic'), 
                                      fg='#f39c12', bg='#2c3e50', wraplength=500)
        self.message_label.pack(pady=10)
        
        # Start the game
        self.new_round()
    
    def new_round(self):
        # Computer randomly selects a color
        self.current_color = random.choice(self.colors)
        
        # Reset display
        self.display_frame.configure(bg='#ecf0f1')
        self.display_label.configure(text="?", fg='#7f8c8d', bg='#ecf0f1')
        self.update_message("🤔 Computer has chosen a color... Can you guess it?", '#f39c12')
        
    def make_guess(self, guessed_color):
        if self.current_color is None:
            return
        
        # Show the computer's color with animation
        self.display_frame.configure(bg=self.color_hex[self.current_color])
        self.display_label.configure(text=self.current_color.upper(), 
                                     fg='white', 
                                     bg=self.color_hex[self.current_color])
        
        # Check if guess is correct
        if guessed_color == self.current_color:
            self.user_wins += 1
            self.update_score_display()
            self.update_message(f"🎉 CORRECT! {guessed_color} was the right color! +1 point for YOU! 🎉", '#2ecc71')
            self.animate_victory()
            
            # Check if user won the game
            if self.user_wins >= 5:
                self.game_over("player")
                return
        else:
            self.computer_wins += 1
            self.update_score_display()
            self.update_message(f"❌ WRONG! Computer chose {self.current_color}, you chose {guessed_color}. +1 point for COMPUTER! ❌", '#e74c3c')
            
            # Check if computer won the game
            if self.computer_wins >= 5:
                self.game_over("computer")
                return
        
        # Start new round after delay
        self.root.after(2000, self.new_round)
    
    def update_score_display(self):
        self.user_score_label.configure(text=f"YOU: {self.user_wins}")
        self.computer_score_label.configure(text=f"COMPUTER: {self.computer_wins}")
    
    def update_message(self, message, color):
        self.message_label.configure(text=message, fg=color)
    
    def animate_victory(self):
        # Flash the display for victory animation
        original_bg = self.display_frame.cget('bg')
        for _ in range(3):
            self.display_frame.configure(bg='gold')
            self.root.update()
            self.root.after(100)
            self.display_frame.configure(bg=original_bg)
            self.root.update()
            self.root.after(100)
    
    def game_over(self, winner):
        if winner == "player":
            message = f"🏆 YOU WIN THE GAME! Final Score: {self.user_wins} - {self.computer_wins} 🏆"
            title = "Victory!"
        else:
            message = f"💻 COMPUTER WINS! Final Score: {self.user_wins} - {self.computer_wins} 💻"
            title = "Game Over!"
        
        if messagebox.askyesno(title, f"{message}\n\nDo you want to play again?"):
            self.new_game()
        else:
            self.quit_game()
    
    def new_game(self):
        self.user_wins = 0
        self.computer_wins = 0
        self.update_score_display()
        self.new_round()
        self.update_message("🔄 New game started! Good luck! 🔄", '#f39c12')
    
    def quit_game(self):
        if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
            self.root.destroy()

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = ColorGuessingGame(root)
    root.mainloop()