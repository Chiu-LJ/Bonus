import random
import time

def play_games():
    board = {}  # 存儲棋盤
    board_mutable = {}  # 存儲玩家可見的棋盤
    total_mines = 10

    def initialize_board():
        for x in range(9):
            for y in range(9):
                board[(x, y)] = None
                board_mutable[(x, y)] = None

    def print_board(board):
        print("    " + " ".join(["{}  ".format(chr(x)) for x in range(97, 106)]))
        print("  +" + "---+"*9)

        for y in range(9):
            print("{} |".format(y+1), end="")
            for x in range(9):
                cell = board[(x, y)]
                if cell is None:
                    print("   |", end="")
                else:
                    print(" {} |".format(cell), end="")
            print("\n  +" + "---+"*9)
    
    initialize_board()
    print_board(board)

    print("Enter the column followed by the row (e.g. a5).\nTo add or remove a flag, add \"f\" to the cell (e.g. a5f).\nType \"help\" to show this message again.")
    first_content = input("Enter the cell(10 mines left): ")

    x_first = ord(first_content[0]) - ord("a")
    y_first = int(first_content[1]) - 1
    board[(x_first, y_first)] = 0
    board_mutable[(x_first, y_first)] = 0
    print_board(board_mutable)
    
    mine_positions = []
    while len(mine_positions) < total_mines:
        x = random.randint(0, 8)
        y = random.randint(0, 8)
        if board[(x, y)] is None and abs(x - x_first) > 1 and abs(y - y_first) > 1:
            board[(x, y)] = "X"
            mine_positions.append((x, y))
    
    for x_answer in range(9):
        for y_answer in range(9):
            if board[(x_answer, y_answer)] is None:
                surrounding_mines_answer = 0
                for side_x_answer, side_y_answer in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    surrounding_x_answer = x_answer + side_x_answer
                    surrounding_y_answer = y_answer + side_y_answer
                    if 0 <= surrounding_x_answer < 9 and 0 <= surrounding_y_answer < 9:
                        if board[(surrounding_x_answer, surrounding_y_answer)] == "X":
                            surrounding_mines_answer += 1
                board[(x_answer, y_answer)] = surrounding_mines_answer

    start_time = time.time()
    while True:
        input_content = input("Enter the cell(%d mines left): " % total_mines)
        
        if input_content == "help":
            print("Enter the column followed by the row (e.g. a5).\nTo add or remove a flag, add \"f\" to the cell (e.g. a5f).\nType \"help\" to show this message again.")
            continue
        elif len(input_content) not in (2, 3) or input_content[0] not in "abcdefghi" or input_content[1] not in "123456789":
            print("Invalid input. Please try again.")
            continue
        elif len(input_content) == 3 and input_content[2] != "f":
            print("Invalid input. Please try again.")
            continue
        else:
            x_chose = ord(input_content[0]) - ord("a")
            y_chose = int(input_content[1]) - 1
            
            if len(input_content) == 2:
                if board_mutable[(x_chose, y_chose)] == "F":
                    print("There is a flag there.")
                    continue

                if board[(x_chose, y_chose)] == "X" and board_mutable[(x_chose, y_chose)] != "F":
                    print("Game over!")
                    print_board(board)
                    print()
                    break

                if board_mutable[(x_chose, y_chose)] is not None and board_mutable[(x_chose, y_chose)] != "F":
                    print("That cell is already shown")
                    continue

                surrounding_mines = 0
                for side_x, side_y in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    surrounding_x = x_chose + side_x
                    surrounding_y = y_chose + side_y
                    if 0 <= surrounding_x < 9 and 0 <= surrounding_y < 9:
                        if board[(surrounding_x, surrounding_y)] == "X":
                            surrounding_mines += 1
                if surrounding_mines == 0:
                    for side_x, side_y in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                        surrounding_x = x_chose + side_x
                        surrounding_y = y_chose + side_y
                        if 0 <= surrounding_x < 9 and 0 <= surrounding_y < 9:
                            board_mutable[(surrounding_x, surrounding_y)] = board[(surrounding_x, surrounding_y)]
                board_mutable[(x_chose, y_chose)] = str(surrounding_mines)
                print_board(board_mutable)

            elif len(input_content) == 3 and input_content[2] == "f":
                if board[(x_chose, y_chose)] == "X" and board_mutable[(x_chose, y_chose)] != "F":
                    board_mutable[(x_chose, y_chose)] = "F"
                    total_mines -= 1
                    print_board(board_mutable)
                    if total_mines == 0:
                        print("You win!", end="")
                        end_time = time.time()
                        pass_time = end_time - start_time
                        print("It took you %d minutes and %d seconds." % (pass_time // 60, pass_time % 60))
                        break
                elif board[(x_chose, y_chose)] == "X" and board_mutable[(x_chose, y_chose)] == "F":
                    board_mutable[(x_chose, y_chose)] = None
                    total_mines += 1
                    print_board(board_mutable)
                elif type(board[(x_chose, y_chose)]) is int:
                    if board_mutable[(x_chose, y_chose)] is None:
                        board_mutable[(x_chose, y_chose)] = "F"
                        print_board(board_mutable)
                    elif board_mutable[(x_chose, y_chose)] == "F":
                        board_mutable[(x_chose, y_chose)] = None
                        print_board(board_mutable)
                elif type(board_mutable[(x_chose, y_chose)]) is int:
                    print("Cannot put the flag there")
                    continue

play_games()

while True:
    wanna_play = input("Play again? (y/n): ")
    if wanna_play == "y":
        print()
        print()
        play_games()
    elif wanna_play == "n":
        break
