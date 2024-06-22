s = input("Enter a string:")
sl = len(s)

if sl < 2:
    print("Longest Palindromic Substring is :", s)
    print("Length is :", sl)

else:
    start = 0
    ml = 1
    for i in range(1,sl):   #檢查奇數
        left = i - 1        #從字中心的左右開檢查
        right = i + 1
        while left >= 0 and right < sl and s[left] == s[right]:
            if right - left + 1 > ml:   #最長的字串，檢查是否比之前的字串還要長
                start = left
                ml = right - left + 1
            left = left - 1
            right = right + 1

        left = i - 1    #檢查偶數
        right = i       #從中心(空)往左右檢查
        while left >= 0 and right < sl and s[left] == s[right]:
            if right - left + 1 > ml:
                start = left
                ml = right - left + 1
            left = left - 1
            right = right + 1

    print("Longest Palindromic Substring is :", s[start:start + ml])
    print("Length is :", ml)

