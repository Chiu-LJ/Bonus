# circle_player = "O"
# cross_player = "X"
def draw_board(board):
    print("+---+---+---+---+---+---+---+")
    for i in range(6):
        print("|", end="")
        for j in range(7):
            print(f" {board[i][j]} ", end="|")
        print()
        print("+---+---+---+---+---+---+---+")


board = [
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
]
print(board)
end_game = False

# A player can only choose a column that is not full
while not end_game:
    # Cross player go first
    cross_index = int(input("Player X >> "))
    # Check if the column is full
    if board[0][cross_index] != " ":
        print("Column is full")
        continue
    # drop the piece
    for i in range(5, -1, -1):
        if board[i][cross_index] == " ":
            board[i][cross_index] = "X"
            break
    draw_board(board)

    # Check if the game is over
    # Check horizontal
    for i in range(6):
        for j in range(4):
            if board[i][j] == board[i][j + 1] == board[i][j + 2] == board[i][j + 3] != " ":
                print(f"Player {board[i][j]} wins")
                end_game = True
                break
            if end_game:
                break
    # Check vertical
    for i in range(3):
        for j in range(7):
            if board[i][j] == board[i + 1][j] == board[i + 2][j] == board[i + 3][j] != " ":
                print(f"Player {board[i][j]} wins")
                end_game = True
                break
            if end_game:
                break
    # Check diagonal
    for i in range(3):
        for j in range(4):
            if (
                board[i][j]
                == board[i + 1][j + 1]
                == board[i + 2][j + 2]
                == board[i + 3][j + 3]
                != " "
            ):
                print(f"Player {board[i][j]} wins")
                end_game = True
                break
            if end_game:
                break

    # Circle player go second
    circle_index = int(input("Player O >> "))
    # Check if the column is full
    if board[0][circle_index] != " ":
        print("Column is full")
        continue
    # drop the piece
    for i in range(5, -1, -1):
        if board[i][circle_index] == " ":
            board[i][circle_index] = "O"
            break

    draw_board(board)

    # Check horizontal
    for i in range(6):
        for j in range(4):
            if board[i][j] == board[i][j + 1] == board[i][j + 2] == board[i][j + 3] != " ":
                print(f"Player {board[i][j]} wins")
                end_game = True
                break
            if end_game:
                break
    # Check vertical
    for i in range(3):
        for j in range(7):
            if board[i][j] == board[i + 1][j] == board[i + 2][j] == board[i + 3][j] != " ":
                print(f"Player {board[i][j]} wins")
                end_game = True
                break
            if end_game:
                break
    # Check diagonal
    for i in range(3):
        for j in range(4):
            if (
                board[i][j]
                == board[i + 1][j + 1]
                == board[i + 2][j + 2]
                == board[i + 3][j + 3]
                != " "
            ):
                print(f"Player {board[i][j]} wins")
                end_game = True
                break
            if end_game:
                break
