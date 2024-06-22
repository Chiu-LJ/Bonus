import random  #導入隨機變數
#al = input("Guess the lowercase alphabet:")
suit = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] #限定輸入者能輸入的值，只在這範圍內
correct_a = random.choice(suit) #隨機選取一字母
#將histogram拆開設變數，以便於在後面各自增加*，最後再印出來
ad = "a-d:"
eh = "e-h:"
il = "i-l:"
mp = "m-p:"
qt = "q-t:"
ux = "u-x:"
yz = "y-z:"
start = True 

while start: #迴圈，直到猜到英文字母才結束
	al = input("Guess the lowercase alphabet:")
	while al not in suit: #如果不是小寫英文字母，就輸出下列文字，並繼續執行
		print("Please enter a lowercase alphabet.")
		break
	while al < correct_a: #如果比較小
		print("The alphabet you are looking for is alphabetically higher.")
		if al in suit[:4]:
			ad = ad + "*"
		if al in suit[4:8]:
			eh = eh + "*"
		if al in suit[8:12]:
			il = il + "*"
		if al in suit[12:16]:
			mp = mp + "*"
		if al in suit[16:20]:
			qt = qt + "*"
		if al in suit[20:24]:
			ux = ux + "*"
		if al in suit[24:]:
			yz = yz + "*"
		break

	while al > correct_a: #如果比較大
		print("The alphabet you are looking for is alphabetically lower.")
		if al in suit[:4]:
			ad = ad + "*"
		if al in suit[4:8]:
			eh = eh + "*"
		if al in suit[8:12]:
			il = il + "*"
		if al in suit[12:16]:
			mp = mp + "*"
		if al in suit[16:20]:
			qt = qt + "*"
		if al in suit[20:24]:
			ux = ux + "*"
		if al in suit[24:]:
			yz = yz + "*"
		break

	if al == correct_a: #相等時
		if al in suit[:4]:
			ad = ad + "*"
		if al in suit[4:8]:
			eh = eh + "*"
		if al in suit[8:12]:
			il = il + "*"
		if al in suit[12:16]:
			mp = mp + "*"
		if al in suit[16:20]:
			qt = qt + "*"
		if al in suit[20:24]:
			ux = ux + "*"
		if al in suit[24:]:
			yz = yz + "*"
		#n為計算總共*個數，最後輸出
		n = int(len(ad[4:])) + int(len(eh[4:])) + int(len(il[4:])) + int(len(mp[4:])) + int(len(qt[4:])) + int(len(ux[4:])) + int(len(yz[4:])) 
		print("Congratulations! You guessd the alphabet",correct_a,"in",n,"tries.")
		start = False

print("Guess Histogram:")
print(ad)
print(eh)
print(il)
print(mp)
print(qt)
print(ux)
print(yz)




#correct
import random

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

answer = random.choice(alphabet)
print(f"Answer: {answer}")
# guess: c, answer: w
counter = 0
histogram = [0, 0, 0, 0, 0, 0, 0]  # a-d, e-h, ..., y-z
# 0-3, 4-7, 8-11
while True:
    counter = counter + 1
    guess = input("Guess the lowercase alphaet: ")

    diff = (ord(guess) - ord("a")) // 4  # -> corresponding pair index
    histogram[diff] += 1

    if guess == answer:
        print(f"Congratulations! You guessed the alphabet {answer} in {counter} tries")
        break
    elif guess < "a" or guess > "z":
        print("Please enter a lowercase alphabet.")
    elif guess < answer:
        print("The alphabet you are looking for is alphabetically higher.")
    elif guess > answer:
        print("The alphabet you are looking for is alphabetically lower.")

print("guess Histogram")
print(histogram)
print(f"a - d: {'*' * histogram[0]}")
print(f"e - h: {'*' * histogram[1]}")
print(f"i - l: {'*' * histogram[2]}")
print(f"m - p: {'*' * histogram[3]}")
print(f"q - t: {'*' * histogram[4]}")
print(f"u - x: {'*' * histogram[5]}")
print(f"y - z: {'*' * histogram[6]}")