def candyCrush(board):
    rows, cols = len(board), len(board[0])
    should_continue = False

    # Step 1: Mark candies to be crushed
    crush = set()
    for r in range(rows):
        for c in range(cols):
            if c > 1 and board[r][c] and board[r][c] == board[r][c-1] == board[r][c-2]:
                crush.update({(r, c), (r, c-1), (r, c-2)})
            if r > 1 and board[r][c] and board[r][c] == board[r-1][c] == board[r-2][c]:
                crush.update({(r, c), (r-1, c), (r-2, c)})
    
    # If there are no candies to crush, the board is stable
    if not crush:
        return board

    # Step 2: Crush candies
    for r, c in crush:
        board[r][c] = 0
    
    # Step 3: Drop candies
    for c in range(cols):
        idx = rows - 1
        for r in range(rows-1, -1, -1):
            if board[r][c] != 0:
                board[idx][c] = board[r][c]
                idx -= 1
        for r in range(idx, -1, -1):
            board[r][c] = 0

    return candyCrush(board)

# Example Input
board = [
    [110, 5, 112, 113, 114],
    [210, 211, 5, 213, 214],
    [310, 311, 3, 313, 314],
    [410, 411, 412, 5, 414],
    [5, 1, 512, 3, 3],
    [610, 4, 1, 613, 614],
    [710, 1, 2, 713, 714],
    [810, 1, 2, 1, 1],
    [1, 1, 2, 2, 2],
    [4, 1, 4, 4, 1014]
]

# Example Output
output = candyCrush(board)
for row in output:
    print(row)
