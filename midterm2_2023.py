#7
nums = input("Enter a sequence of numbers separated by whitespace:")
record = {}
# check the num from the last index to the first index
nums = nums.split(" ")  
for i in range(len (nums)):# str -> int
    nums[i] = int(nums[i])

for i in range(len(nums) - 1, -1, -1):
    element = nums[i]  # 當下的項目
    subsequence = [element]  # 18: [18]
    for j in range(i + 1, len(nums)):
        if nums[j] > element:
            if len([element] + record[nums[j]]) >= len(subsequence):
                subsequence = [element] + record[nums[j]]
    record[element] = subsequence

LIS = []
for key, value in record.items():
    if len(value) > len(LIS):
        LIS = value
print(LIS)


#8
r = int(input("Enter the number of rows:"))
c = int(input("Enter the number of columns:"))
rs = input("Enter the reserved seats:")
rss = rs.split("|")
li = list("A"*(r*c))
oor = ""

for i in range(1,int(len(rss)+1)):
    a = (int(rss[i-1][0])-1)*c + int(rss[i-1][2]) -1
    if int(rss[i-1][0]) > r or int(rss[i-1][2]) > c or int(rss[i-1][0]) == 0 or int(rss[i-1][2]) == 0 :
       oor = oor + rss[i-1] +"|"
    else:
        li = li[:a]+["R"]+li[a+1:]

if len(oor) >= 1 :
    loor = oor[:len(oor)-1]
    print("Out-of-range reserved seats:",loor)

grid = ""   
i = 0
while i < r*c:
    row = li[i:i+c]
    grid = grid + " ".join(row) + "\n"
    i = i + c
print("Seating Arrangement:")
print(grid)
