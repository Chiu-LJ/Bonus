size = int(input("Enter the size of the grid:"))
b = ("_"*size )
a = ("_"*size ) + "\n"
print(a*size)    #先寫出grid
li = list(b*size) #寫成list

while True:
	co = input("Enter the cell coordinates to edit:")
	if co == "done":
		break        #如果是done，遊戲結束
	v = input("Enter the new value for the cell:")

	c = co.split(",")   #用","分開輸入的值
	f = int(c[0])*size + int(c[1])  #找出指定的位置
	li = li[:f]+[v] +li[f+1:]      #在指定的位置，將"_"替換成要求的值
	   
	grid = ""   #將list轉成字串並印出來
	i = 0
	while i < size*size:
		row = li[i:i+size]
		grid = grid + " ".join(row) + "\n"
		i = i + size
	print(grid)


#H24126052_quiz5.py

n = int(input("Enter the size of the grid: "))

matrix = [["_" for i in range(n)] for j in range(n)]


for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()

while True:
    cell_coordinates = input("Enter the cell coordinates to edit: ")  # row,col
    if cell_coordinates == "done":
        break
    row, col = cell_coordinates.split(",")   # str -> int
    row, col = int(row), int(col)
    new_value = input("Enter the new value for the cell: ")

    matrix[row][col] = new_value


    for i in range(n):
        print(" ".join(matrix[i]))
