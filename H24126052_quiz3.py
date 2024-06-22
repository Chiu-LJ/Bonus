print("Welcome to the siple calculator program!")
done = False
while not done:
	fn = float(input("Enter the first number:"))
	sn = float(input("Enter the second number:"))
	ar = input("Select an arithemtic operation(+,-,*,/)=")
	if sn == 0 and ar =="/":
		print("Error : Division by zero!")
		continue
	if ar =="+":
		result = fn + sn
		print("Result:",result)
	elif ar =="-":
		result = fn - sn
		print("Result:",result)
	elif ar =="*":
		result = fn * sn
		print("Result:",result)
	elif ar =="/":
		result = fn / sn
		print("Result:",result)
	again = input("Do you want to perform another calculation(yes/no)=")
	done = (again != "yes")
print("Goodbye!")

