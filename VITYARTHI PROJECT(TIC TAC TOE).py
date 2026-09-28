
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]



def display_board():
    print("\n")
    print(board[0][0], "|", board[0][1], "|", board[0][2])
    print("--+---+--")
    print(board[1][0], "|", board[1][1], "|", board[1][2])
    print("--+---+--")
    print(board[2][0], "|", board[2][1], "|", board[2][2])
    print("\n")



def check_winner(player):


    for row in board:
        if row[0] == player and row[1] == player and row[2] == player:
            return True

    
    for col in range(3):
        if (board[0][col] == player and
            board[1][col] == player and
            board[2][col] == player):
            return True

    
    if (board[0][0] == player and
        board[1][1] == player and
        board[2][2] == player):
        return True

    
    if (board[0][2] == player and
        board[1][1] == player and
        board[2][0] == player):
        return True

    return False



def board_full():
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True



player = "X"

print("Welcome to Tic-Tac-Toe!")
print("Player 1 = X")
print("Player 2 = O")

for turn in range(9):

    display_board()

    print("Player", player, "turn")

    
    row = int(input("Enter row (1-3): ")) - 1
    col = int(input("Enter column (1-3): ")) - 1

    
    if board[row][col] != " ":
        print("This position is already occupied!")
        continue

    
    board[row][col] = player

    
    if check_winner(player):
        display_board()
        print("Player", player, "wins!")
        break


    if board_full():
        display_board()
        print("It's a draw!")
        break

    
    if player == "X":
        player = "O"
    else:
        player = "X"
        