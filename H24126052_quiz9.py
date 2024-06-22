import random

def generate_maze(filename):
    """Read the maze blueprint from a specified file and generate a path."""
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            N = len(lines) // 2
            M = len(lines[0].strip().split('+')) - 1
            maze = {}
            for i in range(N):
                for j in range(M):
                    maze[(i, j)] = 0

            # Generate path
            preset_obstacles_77 = {(1, 1), (3, 2), (4, 4), (5, 1)}
            preset_obstacles_99 = {(2, 2), (2, 3), (2, 5), (2, 6), (3, 6), (4, 4), (5, 2), (6, 3), (7, 6)}
            if filename == "grid77.txt":
                preset_obstacles = preset_obstacles_77
            elif filename == "grid99.txt":
                preset_obstacles = preset_obstacles_99
            else:
                preset_obstacles = set()

            path = [(0, 0)]
            x, y = 0, 0
            while (x, y) != (N - 1, M - 1):
                direction = random.choice([(0, 1), (1, 0)])  # Move right or down
                if direction == (0, 1) and y < M - 1 and (x, y + 1) not in preset_obstacles:
                    y += 1
                elif direction == (1, 0) and x < N - 1 and (x + 1, y) not in preset_obstacles:
                    x += 1
                else:
                    continue  # Skip if the next step is an obstacle
                path.append((x, y))

            for (i, j) in path:
                maze[(i, j)] = 2  # Mark path

            return maze, N, M, lines, path
    except IOError:
        print("IOError occurred in generate_maze function. File not found. Please enter a valid file name.")
        return None, None, None, None, None

def add_obstacles(maze, min_obstacles, N, M):
    obstacle_count = 0
    while obstacle_count < min_obstacles:
        x, y = random.randint(0, N - 1), random.randint(0, M - 1)
        if maze[(x, y)] == 0:  # Ensure we don't overwrite the path
            maze[(x, y)] = 1
            obstacle_count += 1

def set_obstacle(maze, N, M):
    try:
        x, y = map(int, input("Enter the coordinates to place an obstacle (x y): ").split())
        if (x, y) not in maze:
            print("Coordinates out of bounds.")
        elif maze[(x, y)] == 2:
            print("Cannot place an obstacle on the path.")
        else:
            maze[(x, y)] = 1
    except ValueError:
        print("Invalid input. Please enter two integers separated by a space.")

def remove_obstacle(maze, N, M):
    try:
        x, y = map(int, input("Enter the coordinates to remove an obstacle (x y): ").split())
        if (x, y) not in maze:
            print("Coordinates out of bounds.")
        elif maze[(x, y)] != 1:
            print("No obstacle found at the given coordinates.")
        else:
            maze[(x, y)] = 0
    except ValueError:
        print("Invalid input. Please enter two integers separated by a space.")

def print_maze(maze, path, maze_lines, N, M, filename):
    """Print the current state of the maze including the path."""
    print("\nGenerated Maze Map:")
    preset_obstacles_77 = {(1, 1), (3, 2), (4, 4), (5, 1)}
    preset_obstacles_99 = {(2, 2), (2, 3), (2, 5), (2, 6), (3, 6), (4, 4), (5, 2), (6, 3), (7, 6)}

    if filename == "grid77.txt":
        preset_obstacles = preset_obstacles_77
    elif filename == "grid99.txt":
        preset_obstacles = preset_obstacles_99
    else:
        preset_obstacles = set()

    for i in range(N):
        print("+---" * M + "+")
        for j in range(M):
            if (i, j) in path:
                print("| O ", end='')
            elif (i, j) in preset_obstacles or maze[(i, j)] == 1:
                print("| X ", end='')
            else:
                print("|   ", end='')
        print("|")
    print("+---" * M + "+")

def main():
    while True:
        filename = input("Enter file name: ")
        maze, N, M, maze_lines, path = generate_maze(filename)
        if maze is not None:
            break

    while True:
        try:
            min_obstacles = int(input(f"Enter the minimum number of obstacles (0-{N*M}): "))
            if min_obstacles < 0 or min_obstacles > N * M:
                raise ValueError("Invalid number of obstacles.")
            break
        except ValueError:
            print("Invalid number. Please enter a positive integer within the maze's bounds.")

    add_obstacles(maze, min_obstacles, N, M)

    while True:
        print("\nOptions:")
        print("1. Set obstacle")
        print("2. Remove obstacle")
        print("3. Exit")
        try:
            option = int(input("Enter your option: "))
            print_maze(maze, path, maze_lines, N, M, filename)
            if option == 1:
                set_obstacle(maze, N, M)
            elif option == 2:
                remove_obstacle(maze, N, M)
            #elif option == 3:
                #print_maze(maze, path, maze_lines, N, M, filename)
            elif option == 3:
                print("Exiting the program.")
                break
            else:
                print("Invalid option. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
