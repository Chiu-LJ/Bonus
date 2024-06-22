import random
import time


# (a)
def display(matrix):
    print("     a   b   c   d   e   f   g   h   i")
    for i, row in enumerate(matrix): #emumerate是輸出index和value(同時)
        print("   +---+---+---+---+---+---+---+---+---+")
        print(f"{i+1}  ", end="")
        for element in row:
            print(f"| {element} ", end="")
        print("|")
    print("   +---+---+---+---+---+---+---+---+---+")


# (b)
def generate_mines(matrix, mines_count, row, col):

    mines = []
    mine_map = [[" " for j in range(9)] for i in range(9)]#形成[[" "," "],[" "," "]......]的樣子，而第一個[]就是列，第二個是行

    # the row will be of the form 1-9
    # so we need to convert it to 0-8
    row = int(row) - 1
    # the col will be of the form a-i
    # so we need to convert it to 0-8
    col = ord(col) - ord("a")
    # if col == 'e':
    #     col = 4

    # generate mines
    print("Generating mines...")
    for i in range(mines_count):
        while True:
            row_gen = random.randint(0, 8)
            col_gen = random.randint(0, 8)

            # the generated cell should not be the selected cell
            if row_gen == row and col_gen == col:
                continue
            # the row_gen and col_gen should not be next to the selected cell
            if abs(row - row_gen) < 2 and abs(col - col_gen) < 2:#絕對值
                continue
            # the cell should not be a mine already
            if (row_gen, col_gen) in mines:
                continue
            else:
                mines.append((row_gen, col_gen))
                mine_map[row_gen][col_gen] = "X"
                break
    # display(mine_map)

    # determine the number of mines around each cell in mine_map
    for i in range(9):
        for j in range(9):
            if mine_map[i][j] == "X":
                continue
            count = 0
            # check the 8 cells around the current cell
            for r in range(i - 1, i + 2): #i-1檢查到i+1，讓他跑，只檢查特定位置周圍，因為是九宮格
                for c in range(j - 1, j + 2):
                    if r < 0 or r > 8 or c < 0 or c > 8:
                        continue
                    if mine_map[r][c] == "X":
                        count += 1
            # set the count to the cell #顯示值在空格中
            mine_map[i][j] = str(count)
    display(mine_map)

    # set the row, col as the first cell, set '0'
    matrix[row][col] = "0"

    # unfold the all of the connected '0' cells
    print("Unfolding cells that are connected to the selected cell...")
    queue = [(row, col)]    #隊列
    unfolded_pos = [] #已展開位置
    while queue: #使用 while 迴圈來處理隊列中的位置，直到隊列為空為止。
        r, c = queue.pop(0)
        for i in range(r - 1, r + 2):
            for j in range(c - 1, c + 2):
                if i < 0 or i > 8 or j < 0 or j > 8:
                    continue
                if mine_map[i][j] == "0" and matrix[i][j] == " ":
                    matrix[i][j] = "0"
                    queue.append((i, j))  #(i, j)是一組
                    unfolded_pos.append((i, j))
    # show the matrix
    display(matrix)

    # and unfold the connected cells that have been marked as '0'
    print("Unfolded cells:")
    while unfolded_pos: #直到=0
        r, c = unfolded_pos.pop(0)
        for i in range(r - 1, r + 2):
            for j in range(c - 1, c + 2):
                if i < 0 or i > 8 or j < 0 or j > 8:
                    continue
                if mine_map[i][j] != "0":
                    matrix[i][j] = mine_map[i][j]
    display(matrix)

    return mine_map


# (c)
def show_help():
    display(matrix)
    help_message = "Enter the column followed by the row (ex: a5). To add or remove a flag. add 'f' to the cell (ex: a5f). Type 'help' to show this message again. Type 'quit' to exit the game."
    print(help_message)


# (d) add or remove flag
def add_or_remove_flag(matrix, row, col, mines_count):
    if matrix[row][col] == " ":
        matrix[row][col] = "F"
        mines_count -= 1
    elif matrix[row][col] == "F":
        matrix[row][col] = " "
        mines_count += 1
    else:
        print("Cannot put a flag there.")

    return mines_count


def check_valid_position(matrix, col, row):
    row = int(row) - 1
    col = ord(col) - ord("a")

    if row < 0 or row > 8 or col < 0 or col > 8:
        return False

    return True


def transform_position(row, col):
    row = int(row) - 1
    col = ord(col) - ord("a")
    return row, col


def unfold(matrix, row, col, mine_map):
    gameover = False
    # check if the cell is flagged
    if matrix[row][col] == "F":
        print("There is a flag there.")
    elif matrix[row][col] != " ":
        print("That cell is already shown.")
    elif mine_map[row][col] == "X":
        print("Game over.")
        gameover = True
    else:
        matrix[row][col] = mine_map[row][col]
    return gameover


def check_win(matrix):
    # if matrix is full
    for row in matrix:
        if " " in row:
            return False
    return True


play_again = True
while play_again:
    start = time.time()
    matrix = []

    # create a  9x9 matrix with blank cells
    # row: 1 - 9
    # col: a - i
    for i in range(9):
        matrix.append([" "] * 9)

    display(matrix)

    mines_count = 10

    position = input(f"Enter the cell ({mines_count} mines left): ")
    col, row = position[0], position[1]

    # first input, so generate mines
    mine_map = generate_mines(matrix, mines_count, row, col)

    while True:
        position = input(f"Enter the cell ({mines_count} mines left): ")
        gameover = False
        if position == "help":
            show_help()
            continue

        if check_valid_position(matrix, position[0], position[1]) == False:
            print("Invalid position. Try again.")
            continue

        if len(position) == 3:
            col, row, flag = position[0], position[1], position[2]
            # row, col = transform_position(row, col)
            row = int(row) - 1
            col = ord(col) - ord("a")
            mines_count = add_or_remove_flag(matrix, row, col, mines_count)
        elif len(position) == 2:
            col, row = position[0], position[1]
            row, col = transform_position(row, col)
            gameover = unfold(matrix, row, col, mine_map)

        if gameover:
            display(mine_map)  #把所有揭曉
            break
        if check_win(matrix):
            end = time.time()
            print(f"You win. It took you {end-start:.2f} seconds.")
            break

        display(matrix)

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again == "no":
        play_again = False
    else:
        play_again = True
