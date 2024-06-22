se = input("Enter a sequence of integers separated by whitespace:")
selist = list(se) #假設list
l1 = []
l2 = []

for i in range(len(selist)-2): 
    if selist[i+1] > selist[i]:  #中間有空格，所以跳開1
        l1 = l1 + [selist[i]]
    if selist[i] == selist[i-2]:
        l1 = [selist[i]]
    if selist[i+2] < selist[i]:
        l2 = l1   #如果後面小於前面的直
        l1 = []   #天一個變數，讓原本的歸零，跑
if selist[len(selist)-3] < selist[len(selist)-1]:
    l1 = l1 + [selist[len(selist)]-1]

if len(l1) > len(l2):
    print("Length:",len(l1))
    print("LICS:",l1)
else:
    print("Length:",len(l2))
    print("LICS:",l2)





#H24126052_quiz4.py