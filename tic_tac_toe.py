from tkinter import *
from tkinter import ttk
import tkinter.messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.create_widgets()
        self.reset_game()

    def create_widgets(self):
        self.buttons = [ttk.Button(self.root, text=' ', command=lambda i=i: self.button_click(i)) for i in range(9)]
        for i, btn in enumerate(self.buttons):
            btn.grid(row=i//3, column=i%3, sticky='snew', ipadx=40, ipady=40)

        self.player_turn_label = ttk.Label(self.root, text="   Player 1's turn!   ")
        self.player_turn_label.grid(row=3, column=0, sticky='snew', ipadx=40, ipady=40)

        self.player_details_label = ttk.Label(self.root, text="    Player 1 is X\n\n    Player 2 is O")
        self.player_details_label.grid(row=3, column=2, sticky='snew', ipadx=40, ipady=40)

        self.restart_button = ttk.Button(self.root, text='Restart', command=self.reset_game)
        self.restart_button.grid(row=3, column=1, sticky='snew', ipadx=40, ipady=40)

    def reset_game(self):
        self.current_player = "X"
        self.moves = [" " for _ in range(9)]
        self.game_active = True
        self.player_turn_label['text'] = "   Player 1's turn!   "
        for btn in self.buttons:
            btn['text'] = ' '
            btn.state(['!disabled'])

    def button_click(self, index):
        if self.game_active and self.moves[index] == " ":
            self.moves[index] = self.current_player
            self.buttons[index]['text'] = self.current_player
            if self.check_winner():
                tkinter.messagebox.showinfo("Tic Tac Toe", f"Winner is Player {'1' if self.current_player == 'X' else '2'}!")
                self.end_game()
            elif " " not in self.moves:
                tkinter.messagebox.showinfo("Tic Tac Toe", "Match is a Draw.")
                self.end_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.player_turn_label['text'] = f"   Player {'1' if self.current_player == 'X' else '2'}'s turn!   "

    def end_game(self):
        self.game_active = False
        for btn in self.buttons:
            btn.state(['disabled'])

    def check_winner(self):
        win_patterns = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)              # Diagonals
        ]
        for p1, p2, p3 in win_patterns:
            if self.moves[p1] == self.moves[p2] == self.moves[p3] and self.moves[p1] != " ":
                return True
        return False

if __name__ == "__main__":
    root = Tk()
    app = TicTacToe(root)
    root.mainloop()
