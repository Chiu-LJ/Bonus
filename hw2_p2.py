n = int(input("Inpu the range number:"))
now = 2 
while now <= n:
	summ = 0
	for i in range(1,now):
		if now % i == 0:
			summ = summ + i
	if summ == now:
		print("Perfect number ", now)
	now = now + 1


