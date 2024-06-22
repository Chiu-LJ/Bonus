nl = int(input("Enter the number of layers (2 to 5 )="))    #3 4 3 
tl = int(input("Enter the side length of the top layer (2 to 6) ="))
gl = int(input("Enter the growth of each layer (1 to 5 ) ="))
tw = int(input("Enter the trunk width (odd number , 3 to 9) = "))
th = int(input("Enter the trunk height (4 to 10)="))

la = gl
for i in range(1,tl*2): #一個三角形的長相(7-13)
	if i == 1 :
		print(" "*(gl*nl+tl-1)+"#")
		for h in range(1,tl-1):
			print(" " * (gl*nl+tl-1-h)+ "#" + "@" * (h*2-1) + "#")
	if i == tl*2-1:
			print(" "*(gl*nl)+"#" * i)     

while la <=gl*nl-gl:
	for g in range(1,2):
		for i in range(1,tl*2+la): 
			if i == 1:
				for h in range(1,tl+la-1):
					print(" " *(gl*nl+tl-1-h)+ "#" + "@" * (2*h-1) + "#")
			if i == tl*2+la-1:
				print(" " *(gl*nl-la)+"#" * (i+la))
	la = la + gl
for i in range(1,th+1):
	print(" "*(((tl+gl+nl)*2-1)//2+gl-tw//2)+"|"*tw)
