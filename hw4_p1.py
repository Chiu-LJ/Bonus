import random
import time

def play_games():#創建9*9的棋盤
    board = [[None for x in range(9)] for y in range(9)]
    board_mutable = [[None for x in range(9)] for y in range(9)]
    total_mines = 10

    def print_board(board):
        print("    " + " ".join(["{}  ".format(chr(x)) for x in range(97, 106)]))
        print("  +" + "---+"*9)

        for i in range(len(board)):
            row = board[i]
            print("{} |".format(i+1), end="")
            for j in range(len(row)):
                cell = row[j]
                if cell is None: #cell未被揭示
                    print("   |", end="")
                else:
                    print(" {} |".format(cell), end="") #{}會被cell中的值替換
            print("\n  +" + "---+"*9)
    print_board(board)

    def print_board_mutable(board_mutable):
        print("    " + " ".join(["{}  ".format(chr(x)) for x in range(97, 106)]))
        print("  +" + "---+"*9)

        for i in range(len(board_mutable)):
            row = board_mutable[i]
            print("{} |".format(i+1), end="")
            for j in range(len(row)):
                cell = row[j]
                if cell is None:
                    print("   |", end="")
                else:
                    print(" {} |".format(cell), end="")
            print("\n  +" + "---+"*9)

    print("Enter the column followed by the row (e.g. a5).\nTo add or remove a flag, add \"f\" to the cell (e.g. a5f).\nType \"help\" to show this message again.")
    first_content = input("Enter the cell(10 mines left): ")

    x_first = ord(first_content[0]) - ord("a")
    y_first = int(first_content[1]) - 1
    board[y_first][x_first] = 0
    board_mutable[y_first][x_first] = 0
    print_board_mutable(board_mutable)
    
    mine_positions = []
    while len(mine_positions) < total_mines:
        x = random.randint(0, 8)
        y = random.randint(0, 8)
        if board[y][x] is None and abs(x - x_first) > 1 and abs(y - y_first) > 1:
            board[y][x] = "X"  # 在這裡將地雷顯示在 board 中
            mine_positions.append((y, x))
    
    for x_answer in range(9):
        for y_answer in range(9):
            if board[y_answer][x_answer] is None:
                surrounding_mines_answer = 0
                for side_x_answer, side_y_answer in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    surrounding_x_answer = x_answer + side_x_answer
                    surrounding_y_answer = y_answer + side_y_answer
                    if surrounding_x_answer < 0 or surrounding_x_answer > 8 or surrounding_y_answer < 0 or surrounding_y_answer > 8:
                        continue
                    if board[surrounding_y_answer][surrounding_x_answer] == "X":
                        surrounding_mines_answer += 1
                board[y_answer][x_answer] = surrounding_mines_answer

    start_time = time.time()
    while True:
        input_content = input("Enter the cell(%d mines left): "%(total_mines))
        
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
            if len(input_content) == 2:
                
                x_chose = ord(input_content[0]) - ord("a")
                y_chose = int(input_content[1]) - 1
                
                if board_mutable[y_chose][x_chose] == "F":
                    print("There is a flag there.")
                    continue

                if board[y_chose][x_chose] == "X" and board_mutable[y_chose][x_chose] != "F":
                    print("Game over!")
                    print_board(board)
                    print()
                    break

                if board_mutable[y_chose][x_chose] is not None and board_mutable[y_chose][x_chose] != "F":
                    print("That cell is already shown")
                    continue

                surrounding_mines = 0
                for side_x, side_y in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    surrounding_x = x_chose + side_x
                    surrounding_y = y_chose + side_y
                    if surrounding_x < 0 or surrounding_x > 8 or surrounding_y < 0 or surrounding_y > 8:
                        continue
                    if board[surrounding_y][surrounding_x] == "X":
                        surrounding_mines += 1
                if surrounding_mines == 0:
                    for side_x, side_y in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                        surrounding_x = x_chose + side_x
                        surrounding_y = y_chose + side_y
                        if surrounding_x < 0 or surrounding_x > 8 or surrounding_y < 0 or surrounding_y > 8:
                            continue
                        board_mutable[surrounding_y][surrounding_x] = board[surrounding_y][surrounding_x]
                board_mutable[y_chose][x_chose] = str(surrounding_mines)
                print_board_mutable(board_mutable)

            if len(input_content) == 3 and input_content[2] == "f":
                x_flag = ord(input_content[0]) - ord("a")
                y_flag = int(input_content[1]) - 1

                if board[y_flag][x_flag] == "X" and board_mutable[y_flag][x_flag] != "F":
                    board_mutable[y_flag][x_flag] = "F"
                    total_mines -= 1
                    print_board_mutable(board_mutable)
                    if total_mines == 0:
                        print("You wins!",end="")
                        end_time = time.time()
                        pass_time = end_time - start_time
                        print("It took you %d minutes and %d seconds." %(pass_time//60 , pass_time%60))
                        break
                elif board[y_flag][x_flag] == "X" and board_mutable[y_flag][x_flag] == "F":
                    board_mutable[y_flag][x_flag] = None
                    total_mines+=1
                    print_board_mutable(board_mutable)
                elif type(board[y_flag][x_flag]) is int:
                    if board_mutable[y_flag][x_flag] == None:
                        board_mutable[y_flag][x_flag] = "F"
                        print_board_mutable(board_mutable)
                    elif board_mutable[y_flag][x_flag] == "F":
                        board_mutable[y_flag][x_flag] = None
                        print_board_mutable(board_mutable)
                elif type(board_mutable[y_flag][x_flag]) is int:
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
