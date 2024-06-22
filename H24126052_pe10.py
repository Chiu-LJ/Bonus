import os
import random
import time
import threading
import sys

# 检查操作系统
is_windows = os.name == 'nt'
if is_windows:
    import msvcrt
else:
    import termios
    import tty
    import select

# 获取终端大小
def get_terminal_size():
    return os.get_terminal_size()

# 获取按键
def get_key():
    if is_windows:
        if msvcrt.kbhit():
            return msvcrt.getch().decode('utf-8')
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            if select.select([sys.stdin], [], [], 0.1)[0]:
                return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ''

# 游戏的全局变量
width, height = get_terminal_size()
width -= 1  # 调整宽度适应终端
height -= 1  # 调整高度适应终端
snake = [(height // 2, width // 2), (height // 2, width // 2 - 1), (height // 2, width // 2 - 2)]
direction = 'RIGHT'
normal_food = (0, 0)
special_food = (0, 0)
obstacles = []
game_over = False
paused = False
normal_food_eaten = 0
special_food_eaten = 0
move_interval = 0.1  # 初始移动间隔

# 初始化游戏
def initialize_game():
    global normal_food, special_food
    normal_food = generate_food()
    special_food = generate_food()
    generate_obstacles()

# 生成食物
def generate_food():
    while True:
        food = (random.randint(1, height - 2), random.randint(1, width - 2))
        if food not in snake and food not in obstacles:
            return food

# 生成障碍物
def generate_obstacles():
    global obstacles
    obstacles = []
    num_obstacles = int((width * height) * 0.05 // 5)
    for _ in range(num_obstacles):
        while True:
            vertical = random.choice([True, False])
            start_row = random.randint(1, height - 6)
            start_col = random.randint(1, width - 6)
            obstacle = [(start_row + i, start_col) if vertical else (start_row, start_col + i) for i in range(5)]
            if not any(cell in snake for cell in obstacle) and not any(cell in obstacles for cell in obstacle):
                obstacles.extend(obstacle)
                break

# 打印游戏屏幕
def print_game_screen():
    # 构建游戏屏幕的字符串
    screen = [[' ' for _ in range(width)] for _ in range(height)]
    for y, x in snake:
        screen[y][x] = 'O'
    screen[normal_food[0]][normal_food[1]] = 'π'
    screen[special_food[0]][special_food[1]] = 'X'
    for y, x in obstacles:
        screen[y][x] = '#'

    # 构建 ANSI 控制字符串
    output = ''
    for row_index, row in enumerate(screen):
        for col_index, char in enumerate(row):
            output += f"\033[{row_index + 1};{col_index + 1}H{char}"

    # 打印 ANSI 控制字符串
    sys.stdout.write(output)
    sys.stdout.flush()

# 移动蛇
def move_snake():
    global game_over, normal_food, special_food, normal_food_eaten, special_food_eaten, direction, move_interval, snake

    head_y, head_x = snake[0]

    if direction == 'UP':
        new_head = (head_y - 1, head_x)
    elif direction == 'DOWN':
        new_head = (head_y + 1, head_x)
    elif direction == 'LEFT':
        new_head = (head_y, head_x - 1)
    elif direction == 'RIGHT':
        new_head = (head_y, head_x + 1)

    # 环绕
    new_head = (new_head[0] % height, new_head[1] % width)

    if new_head in snake or new_head in obstacles:
        game_over = True
        return

    snake.insert(0, new_head)

    if new_head == normal_food:
        normal_food_eaten += 1
        normal_food = generate_food()
    elif new_head == special_food:
        special_food_eaten += 1
        special_food = generate_food()
        if len(snake) > 1:
            snake.pop()
            snake.pop()
    else:
        snake.pop()

# 键盘输入处理
def get_input():
    global direction, paused, move_interval
    while not game_over:
        key = get_key()
        if key == 'w' and direction != 'DOWN':
            direction = 'UP'
        elif key == 's' and direction != 'UP':
            direction = 'DOWN'
        elif key == 'a' and direction != 'RIGHT':
            direction = 'LEFT'
        elif key == 'd' and direction != 'LEFT':
            direction = 'RIGHT'
        elif key == ' ':
            paused = not paused

# 主循环
def main():
    global game_over
    initialize_game()
    threading.Thread(target=get_input, daemon=True).start()
    while not game_over:
        if not paused:
            move_snake()
            print_game_screen()
        time.sleep(0.1)

    if len(snake) == 1:
        reason = "Hit self"
    elif game_over:
        reason = "Hit obstacle"

    print(f" Game over because of {reason}")
    print(f"You ate {normal_food_eaten} normal food and {special_food_eaten} special food.")

if __name__ == "__main__":
    main()
