y = int(input("Please input year:"))
m = int(input("Please input month:"))
a = "Sun Mon Tue Wed Thu Fri Sat\n 01  02  03  04  05  06  07 \n 08  09  10  11  12  13  14 \n 15  16  17  18  19  20  21 \n 22  23  24  25  26  27  28 \n 29  30  31"
b = "Sun Mon Tue Wed Thu Fri Sat\n     01  02  03  04  05  06 \n 07  08  09  10  11  12  13 \n 14  15  16  17  18  19  20 \n 21  22  23  24  25  26  27 \n 28  29  30  31"
c = "Sun Mon Tue Wed Thu Fri Sat\n         01  02  03  04  05 \n 06  07  08  09  10  11  12 \n 13  14  15  16  17  18  19 \n 20  21  22  23  24  25  26 \n 27  28  29  30  31"
D = "Sun Mon Tue Wed Thu Fri Sat\n             01  02  03  04 \n 05  06  07  08  09  10  11 \n 12  13  14  15  16  17  18 \n 19  20  21  22  23  24  25 \n 26  27  28  29  30  31"
e = "Sun Mon Tue Wed Thu Fri Sat\n                 01  02  03 \n 04  05  06  07  08  09  10 \n 11  12  13  14  15  16  17 \n 18  19  20  21  22  23  24 \n 25  26  27  28  29  30  31"
f = "Sun Mon Tue Wed Thu Fri Sat\n                     01  02 \n 03  04  05  06  07  08  09 \n 10  11  12  13  14  15  16 \n 17  18  19  20  21  22  23 \n 24  25  26  27  28  29  30 \n 31"
g = "Sun Mon Tue Wed Thu Fri Sat\n                         01 \n 02  03  04  05  06  07  08 \n 09  10  11  12  13  14  15 \n 16  17  18  19  20  21  22 \n 23  24  25  26  27  28  29 \n 30  31"


d = (7 + (2.6*m - 0.2)//1 - 2*int(str(y)[:2]) + int(str(y)[2:]) + (int(str(y)[:2])/4)//1) %7 

while m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
	if d ==0:
		print(a)
		quit()
	elif d == 1:
		print(b)
		quit()
	elif d == 2:
		print(c)
		quit()
	elif d == 3:
		print(D)
		quit()
	elif d == 4:
		print(e)
		quit()
	elif d == 5:
		print(f)
		quit()
	elif d == 6:
		print(g)
		quit()
while m == 4 or m == 6 or m == 9 or m == 11 :
	if d ==0:
		print(a[:153])
		quit()
	elif d == 1:			
		print(b[:157])
		quit()
	elif d == 2:
		print(c[:161])
		quit()
	elif d == 3:
		print(D[:165])
		quit()
	elif d == 4:
		print(e[:169])
		quit()
	elif d == 5:
		print(f[:173])
		quit()
	elif d == 6:
		print(g[:177])
		quit()

while m == 2: 
	if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):        #閏年2月( - 29)
		if d ==0:
			print(a[:149])
			quit()
		elif d == 1:			
			print(b[:153])
			quit()
		elif d == 2:
			print(c[:157])
			quit()
		elif d == 3:
			print(D[:161])
			quit()
		elif d == 4:
			print(e[:165])
			quit()
		elif d == 5:
			print(f[:169])
			quit()
		elif d == 6:
			print(g[:173])   
			quit()
	else:
		if d ==0:
			print(a[:145])
			quit()
		elif d == 1:			
			print(b[:149])
			quit()
		elif d == 2:
			print(c[:153])
			quit()
		elif d == 3:
			print(D[:157])
			quit()
		elif d == 4:
			print(e[:161])
			quit()
		elif d == 5:
			print(f[:165])
			quit()
		elif d == 6:
			print(g[:169])
			quit()