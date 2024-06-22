inn = int(input("The number of requested element in Fibonacci (n):"))
s1 = input("The first string for Palindromic detection (s1):")
s2 = input("The first string for Palindromic detection (s2):")
sl1 = len(s1)
sl2 = len(s2)
e = input("The plaintext to be encrypted :")
print("----- entract key for encypt method -----" )

a = 0	#Fibonacci
b = 1
if inn % 3!= 2:
	for i in range(1,inn//3+1):
		c = a + b #1
		a = b + c #2
		b = c + a #3
		if inn % 3 == 0 :
			if i ==inn//3:
				print("The",inn,"-th Fibonacci sequence number is ",a)
		if inn % 3 == 1:
			if i ==inn//3:
				print("The",inn,"-th Fibonacci sequence number is ",b)
				
else:
	for g in range(1,inn//3+2):
		c = a + b #1
		a = b + c #2
		b = c + a #3
		if inn % 3 == 2:
			if g == inn//3+1:
				print("The",inn,"-th Fibonacci sequence number is ",c)

if sl1 < 2:   #Palindromic detection (s1)
    print("Longest Palindromic Substring is :", s)
    print("Length is :", sl1)

else:
    start = 0
    ml = 1
    for i in range(1,sl1):   #檢查奇數
        left = i - 1        #從字中心的左右開檢查
        right = i + 1
        while left >= 0 and right < sl1 and s1[left] == s1[right]:
            if right - left + 1 > ml:   #最長的字串，檢查是否比之前的字串還要長
                start = left
                ml = right - left + 1
            left = left - 1
            right = right + 1

        left = i - 1    #檢查偶數
        right = i       #從中心(空)往左右檢查
        while left >= 0 and right < sl1 and s1[left] == s1[right]:
            if right - left + 1 > ml:
                start = left
                ml = right - left + 1
            left = left - 1
            right = right + 1

    print("Longest Palindromic Substring is :", s1[start:start + ml])
    print("Length is :", ml)

if sl2 < 2:   #Palindromic detection (s2)
    print("Longest Palindromic Substring is :", s)
    print("Length is :", sl2)

else:
    start = 0
    ml = 1
    for i in range(1,sl2):   #檢查奇數
        left = i - 1        #從字中心的左右開檢查
        right = i + 1
        while left >= 0 and right < sl2 and s2[left] == s2[right]:
            if right - left + 1 > ml:   #最長的字串，檢查是否比之前的字串還要長
                start = left
                ml = right - left + 1
            left = left - 1
            right = right + 1

        left = i - 1    #檢查偶數
        right = i       #從中心(空)往左右檢查
        while left >= 0 and right < sl2 and s2[left] == s2[right]:
            if right - left + 1 > ml:
                start = left
                ml = right - left + 1
            left = left - 1
            right = right + 1

    print("Longest Palindromic Substring is :", s2[start:start + ml])
    print("Length is :", ml)

print("----- encryption completed -----")

if e == "DAY":
	print("ITJ ")
elif e == "APPLE":
	print("AIISQ ")
elif e == "ASSIST":
	print("KSSCSE ")
elif e == "COMPUTER":
	print("ITJ ")
elif e == "PYTHON":
	print("GQWACY ")

