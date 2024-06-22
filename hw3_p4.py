# P4: Replacing Number in a Matrix


def bfs(matrix, x, y, k):
    locations = []

    row, col = len(matrix), len(matrix[0])

    # Check if the pixel is of the color z
    z = matrix[x][y]

    # Create a queue for BFS
    queue = []
    queue.append((x, y))

    # Create a visited matrix to keep track of visited pixels
    visited = [[False for _ in range(col)] for _ in range(row)] #所有元素的初始值都是False，且不會在迴圈中使用這個迴圈索引"_"

    # Create a direction matrix for the 4 directions: left, right, up, down
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    while queue:
        x, y = queue.pop(0) #從隊列的前端彈出一個位置 (x, y)，以進行處理。
        locations.append((x, y))
        visited[x][y] = True

        for dx, dy in directions: #當前位置 (x, y) 向四個方向之一移動後的位置。移動4次
            nx, ny = x + dx, y + dy #新位置 (nx, ny)

            # Check if the pixel is within the matrix
            if nx < 0 or nx >= row or ny < 0 or ny >= col: #確認範圍
                continue

            # Check if the pixel is of the color z
            if matrix[nx][ny] == z and not visited[nx][ny]: #檢查新位置 (nx, ny) 的像素顏色是否等於目標顏色 z，且該位置並未訪問過。
                queue.append((nx, ny))

        print(queue)

    return locations


print("Enter index x, y, k (separated by space):")
x, y, k = input().split()

x = int(x)
y = int(y)
k = int(k)

print("Enter the matrix by multiple lines:")
matrix = []
line = ""
while line != "q":
    line = input()
    if line != "q":
        matrix.append(list(map(int, line.split()))) #將line.split()轉成int(用map)
                                                    #map:設定map函式第一個參數int ，第二個參數為要轉換的list意思就是將list裡面的每一個元素都轉型成整數(int
                                                    #例子:listA = ['1','2','3'] >>> print map(int,listA) >>> [1, 2, 3]
# print(matrix)

# Replace the element at index (x, y) with k

#print(matrix)

# replace the color 𝑧 of the given pixel 〈𝑥,𝑦〉 and all of its adjacent (excluding diagonally adjacent) same colored 𝑧 pixels with the given target color 𝑘.
# The adjacent pixels are the pixels to the left, right, up, and down of the pixel 〈𝑥,𝑦〉
# If the pixel 〈𝑥,𝑦〉 is already of the target color 𝑘, then do nothing.

locations = bfs(matrix, x, y, k)
for x, y in locations:
    matrix[x][y] = k

for row in matrix:
    for item in row:
        print(item, end=" ")
    print()
