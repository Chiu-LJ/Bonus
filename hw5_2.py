import random

def initialize_board(length, penalty_probability):
    """初始化棋盤，設置安全和懲罰格子。"""
    return ['P' if random.random() < penalty_probability else '_' for _ in range(length)]

def roll_dice():
    """模擬擲骰子。"""
    return random.randint(1, 6)

def move_player(player_position, board):
    """根據擲骰子結果移動玩家並處理懲罰。"""
    dice_roll = roll_dice()
    new_position = player_position + dice_roll
    if new_position >= len(board):
        return len(board) - 1, dice_roll, False

    if board[new_position] == 'P':
        return new_position, dice_roll, True
    return new_position, dice_roll, False

def print_board(board, player_a_position, player_b_position, penalties, move_a, move_b):
    """打印當前棋盤，顯示玩家位置和懲罰。"""
    display_board = ['_' for _ in range(len(board))]
    for i in range(len(board)):
        if player_a_position == i and player_b_position == i:
            display_board[i] = 'X' if not penalties['A'] and not penalties['B'] else 'x'
        elif player_a_position == i:
            display_board[i] = 'A' if not penalties['A'] else 'a'
        elif player_b_position == i:
            display_board[i] = 'B' if not penalties['B'] else 'b'
    
    print(''.join(display_board) + f" (A: {move_a}, B: {move_b})")

def print_hidden_board(board):
    """打印隱藏懲罰格子的棋盤。"""
    print(' '.join(['P' if square == 'P' else '_' for square in board]))

def main():
    board_length = 30
    penalty_probability = 0.3

    board = initialize_board(board_length, penalty_probability)

    player_positions = {'A': 0, 'B': 0}
    penalties = {'A': False, 'B': False}
    
    game_over = False

    while not game_over:
        move_a = 0
        move_b = 0
        for player in ['A', 'B']:
            if penalties[player]:
                penalties[player] = False
                continue

            player_positions[player], move, penalties[player] = move_player(player_positions[player], board)

            if player == 'A':
                move_a = move
            else:
                move_b = move

            print_board(board, player_positions['A'], player_positions['B'], penalties, move_a, move_b)

            if player_positions[player] == board_length - 1:
                game_over = True
                print(f"\nPlayer {player} wins!\n")
                break
        if game_over:
            break

    print_hidden_board(board)

if __name__ == "__main__":
    main()
