m = float(input("Enter the shopping amount:"))
l = str(input("Enter the membership level (Regular or Gold):"))
Regular = "Regular"
Gold = "Gold"
if l == Regular:
	if m < 1000 :
		m = m 
		print("Regular ＄",m)
	if 2000>=m > 1000:
		m = m * 0.9
		print("Regular ＄",m)
	if 3000>=m > 2000:
		m = m * 0.85
		print("Regular ＄",m)
	if m > 3000:
		m = m * 0.8
		print("Regular ＄",m)
if l == Gold:
	if m < 1000: 
		m = m 
		print("Gold ＄",m)
	if 2000>=m > 1000:
		m = m * 0.85
		print("Gold ＄",m)
	if 3000>=m > 2000:
		m = m * 0.8
		print("Gold ＄",m)
	if m > 3000:
		m = m * 0.75
		print("Gold ＄",m)
if l !=Regular and l !=Gold:
	print ("Invalid membership level. Please enter \'Regular\' or \'Gold \'")