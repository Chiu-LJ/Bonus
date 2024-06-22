import random

# 初始化棋盤
def initialize_board(width, height, candy_types):
    return [[random.randint(1, candy_types) for _ in range(width)] for _ in range(height)]

# 打印棋盤
def print_board(board):
    for row in board:
        print(' '.join(map(str, row)))
    print()

# 用戶移動輸入
def get_user_move():
    move = input("Enter the coordinates of two adjacent candies to switch (e.g., '0 0 0 1' for (0,0) and (0,1)): ")
    return list(map(int, move.split()))

# 驗證移動是否有效
def is_valid_move(board, x1, y1, x2, y2):
    rows, cols = len(board), len(board[0])
    if 0 <= x1 < rows and 0 <= y1 < cols and 0 <= x2 < rows and 0 <= y2 < cols:
        return (abs(x1 - x2) == 1 and y1 == y2) or (abs(y1 - y2) == 1 and x1 == x2)
    return False

# 交換糖果位置
def switch_candies(board, x1, y1, x2, y2):
    board[x1][y1], board[x2][y2] = board[x2][y2], board[x1][y1]

# 糖果消除邏輯
def crush_candies(board):
    rows, cols = len(board), len(board[0])
    crush = set()
    
    for r in range(rows):
        for c in range(cols):
            if c > 1 and board[r][c] and board[r][c] == board[r][c-1] == board[r][c-2]:
                crush.update({(r, c), (r, c-1), (r, c-2)})
            if r > 1 and board[r][c] and board[r][c] == board[r-1][c] == board[r-2][c]:
                crush.update({(r, c), (r-1, c), (r-2, c)})
    
    if not crush:
        return False, 0

    score = len(crush)
    for r, c in crush:
        board[r][c] = 0

    return True, score

# 讓糖果下落
def drop_candies(board):
    rows, cols = len(board), len(board[0])
    for c in range(cols):
        idx = rows - 1
        for r in range(rows-1, -1, -1):
            if board[r][c] != 0:
                board[idx][c] = board[r][c]
                idx -= 1
        for r in range(idx, -1, -1):
            board[r][c] = 0

# 重新填充棋盤
def refill_board(board, candy_types):
    rows, cols = len(board), len(board[0])
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 0:
                board[r][c] = random.randint(1, candy_types)

# 主函數
def main():
    print("Welcome to Candy Crush!")
    width = int(input("Enter the width of the board: "))
    height = int(input("Enter the height of the board: "))
    candy_types = int(input("Enter the number of candy types: "))

    board = initialize_board(width, height, candy_types)
    print_board(board)

    score = 0
    moves = 0
    MAX_MOVES = 20

    while moves < MAX_MOVES:
        x1, y1, x2, y2 = get_user_move()
        if is_valid_move(board, x1, y1, x2, y2):
            switch_candies(board, x1, y1, x2, y2)
            moves += 1
            while True:
                crushed, points = crush_candies(board)
                if not crushed:
                    break
                score += points
                drop_candies(board)
                refill_board(board, candy_types)
                print_board(board)
                print(f"Score: {score}")
        else:
            print("Invalid move. Try again.")

    print("Game Over")
    print(f"Final Score: {score}")

if __name__ == "__main__":
    main()
