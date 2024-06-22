def pascal_value(row, col):
    if col == 0 or col == row:
        return 1
    return pascal_value(row - 1, col - 1) + pascal_value(row - 1, col)

def generate_pascals_triangle(rows):
    triangle = []
    for row in range(rows):
        current_row = []
        for col in range(row + 1):
            current_row.append(pascal_value(row, col))
        triangle.append(current_row)
    return triangle

def print_pascals_triangle(triangle, direction):
    if direction == 'normal':
        max_length = len(' '.join(map(str, triangle[-1])))
        for row in triangle:
            row_str = ' '.join(map(str, row))
            print(row_str.center(max_length))
    
    elif direction == 'reversed':
        max_length = len(' '.join(map(str, triangle[-1])))
        for row in reversed(triangle):
            row_str = ' '.join(map(str, row))
            print(row_str.center(max_length))
    
    elif direction == 'left':
        max_length = len(' '.join(map(str, triangle[-1])))
        for row in triangle:
            row_str = ' '.join(map(str, row))
            print(row_str.rjust(max_length))
    
    elif direction == 'right':
        for row in triangle:
            row_str = ' '.join(map(str, row))
            print(row_str)


rows = int(input("Height of Pascal's triangle: "))
while rows <= 0:
    print("Invaild input. Please enter an integer greater than or equal to 1.")
    rows = int(input("Height of Pascal's triangle: "))

direction = input("Direction of triangle (\'normal\', \'reversed\', \'left\' or \'right\'):")

while direction != "normal" and direction != "reversed" and direction != "left" and direction != "right":
    print("Invaild input for direction. Please enter \'normal\', \'reversed\', \'left\'or \'right\'.")
    direction = input("Direction of triangle (\'normal\', \'reversed\', \'left\' or \'right\'):")

# 打印帕斯卡三角形
triangle = generate_pascals_triangle(rows)
print_pascals_triangle(triangle, direction)
