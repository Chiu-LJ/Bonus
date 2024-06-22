#midterm_2019.py (題目有誤)

l = input("Input list:")
li = l.split(" ")
li = [int(x) for x in li]
low = int(input("Input low:"))
high = int(input("Input high:"))
listt = []

# Find missing numbers
i = low
while i <= high:
    if i not in li:
        start = i
        while i + 1 <= high and i + 1 not in li:
            i = i + 1
        end = i
        if start == end:
            listt.append(str(start))
        else:
            listt.append(f"{start}->{end}")
    i = i + 1

print(listt)
