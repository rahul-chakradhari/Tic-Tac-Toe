import tkinter as tk
from tkinter import messagebox
import random

# Initialize the main Tkinter window
root = tk.Tk()
root.title("Tic Tac Toe")

# Initialize variables
PLAYER = "X"
AI = "O"
EMPTY = " "
board = [EMPTY] * 9

# Function to check for winner
def check_winner(board):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] != EMPTY:
            return board[i]
    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != EMPTY:
            return board[i]
    # Check diagonals
    if board[0] == board[4] == board[8] != EMPTY or board[2] == board[4] == board[6] != EMPTY:
        return board[4]
    return EMPTY

# Function to check if the board is full
def is_board_full(board):
    return EMPTY not in board

# Function to handle player's move
def player_move(index):
    global PLAYER
    if board[index] == EMPTY:
        board[index] = PLAYER
        buttons[index].config(text=PLAYER)
        if check_winner(board) == PLAYER:
            messagebox.showinfo("Winner", "Congratulations! You won!")
            root.quit()
        elif is_board_full(board):
            messagebox.showinfo("Draw", "It's a draw!")
            root.quit()
        else:
            ai_move()

# Minimax algorithm for AI
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == AI:
        return 10 - depth
    elif winner == PLAYER:
        return depth - 10
    elif is_board_full(board):
        return 0

    if is_maximizing:
        max_eval = float("-inf")
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI
                eval = minimax(board, depth + 1, False)
                board[i] = EMPTY
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = PLAYER
                eval = minimax(board, depth + 1, True)
                board[i] = EMPTY
                min_eval = min(min_eval, eval)
        return min_eval

# AI move
def ai_move():
    best_move = None
    best_eval = float("-inf")
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI
            eval = minimax(board, 0, False)
            board[i] = EMPTY
            if eval > best_eval:
                best_eval = eval
                best_move = i
    board[best_move] = AI
    buttons[best_move].config(text=AI)
    if check_winner(board) == AI:
        messagebox.showinfo("Winner", "AI wins!")
        root.quit()
    elif is_board_full(board):
        messagebox.showinfo("Draw", "It's a draw!")
        root.quit()

# Function to close the Tkinter window
def close_window():
    root.destroy()

# Create buttons for the Tic Tac Toe grid
buttons = []
for i in range(3):
    for j in range(3):
        button = tk.Button(root, text=EMPTY, font=('Helvetica', 20), width=6, height=3,
                           command=lambda index=i * 3 + j: player_move(index))
        button.grid(row=i, column=j, padx=5, pady=5)
        buttons.append(button)

# Bind closing event to the window
root.protocol("WM_DELETE_WINDOW", close_window)

# Start the main loop
root.mainloop()
