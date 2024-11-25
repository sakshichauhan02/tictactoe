import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def _init_(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

        # Create buttons for the grid
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = tk.Button(
                    root, text="", font=("Arial", 24), height=2, width=5,
                    command=lambda r=row, c=col: self.make_move(r, c)
                )
                self.buttons[row][col].grid(row=row, column=col)

    def make_move(self, row, col):
        # Check if the cell is empty
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            
            # Check for winner
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
                return

            # Check for draw
            if self.is_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
                return

            # Switch player
            self.current_player = "O" if self.current_player == "X" else "X"
        else:
            messagebox.showwarning("Invalid Move", "Cell already taken! Choose another.")

    def check_winner(self):
        # Check rows, columns, and diagonals
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != "":
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def is_draw(self):
        # Check if all cells are filled
        for row in self.board:
            if "" in row:
                return False
        return True

    def reset_game(self):
        # Reset the board for a new game
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="")


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()