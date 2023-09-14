import tkinter as t
from tkinter import messagebox

# Create the board
board = [" " for _ in range(9)]

# Function to check if the board is full
def is_board_full():
    return " " not in board


# Function to check if there is a winner
def check_winner(player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == player:
            return True

    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True

    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True

    return False


# Function to handle button click
def handle_click(position):
    global current_player

    if board[position] != " ":
        return

    board[position] = current_player
    buttons[position].config(text=current_player)

    if check_winner(current_player):
        messagebox.showinfo("Winner", "Player " + current_player + " wins!")
        reset_game()
    elif is_board_full():
        messagebox.showinfo("Tie", "It's a tie!")
        reset_game()
    else:
        current_player = "O" if current_player == "X" else "X"


# Function to reset the game
def reset_game():
    global current_player
    board = [" " for _ in range(9)]
    current_player = "X"
    for button in buttons:
        button.config(text=" ", state=t.NORMAL)


# Create the main window
window = t.Tk()
window.title("Tic-Tac-Toe")

# Create buttons for the board
buttons = []
for i in range(9):
    button = t.Button(
        window, text=" ", width=10, height=5, command=lambda pos=i: handle_click(pos)
    )
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

# Initialize the current player
current_player = "X"

# Start the main loop
window.mainloop()
