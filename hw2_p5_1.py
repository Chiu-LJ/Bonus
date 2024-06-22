inn = int(input("Input an integer number:"))
a = 0	
b = 1
if inn % 3!= 2:
	for i in range(1,inn//3+1):
		c = a + b #1
		a = b + c #2
		b = c + a #3
		if inn % 3 == 0 :
			while i ==inn//3:
				print("The",inn,"-th Fibonacci sequence number is ",a)
				quit()
		if inn % 3 == 1:
			while i ==inn//3:
				print("The",inn,"-th Fibonacci sequence number is ",b)
				quit()
else:
	for g in range(1,inn//3+2):
		c = a + b #1
		a = b + c #2
		b = c + a #3
		if inn % 3 == 2:
			while g == inn//3+1:
				print("The",inn,"-th Fibonacci sequence number is ",c)
				quit()
				
	
