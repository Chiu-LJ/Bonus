i,j = 9,9 #先假設i,j的起始值，代表第一列第一行的值
while 3 <= i <= 9: #讓i在3-9之間跑，若超過則跳出
	while 1 <= j <= 9: #讓j在1-9之間跑，若超過，則i-3再繼續跑
		print(j ,"x", i ,"=",j*i,end="\t") #可以print出jxi=(j*i)並且不換行繼續print
		print(j ,"x", (i-1) ,"=",j*(i-1),end="\t") #可以print出jx(i-1)=(j*(i-1))並且不換行繼續print
		print(j ,"x", (i-2) ,"=",j*(i-2),end="\n") #可以print出jx(i-2)=(j*(i-2))並且結束
		j = j - 1 #讓j可以在i相同的情況下j-1一值跑，直到i>9
	print() #print一列空行
	i = i - 3 #每次讓i都-3，直到i=3
	j = 9 #reset j的數值，讓j每次都可以從9開始執行