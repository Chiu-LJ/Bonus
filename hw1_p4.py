h = float(input("Input the height of the 1st ball: "))
m1 = float(input("Input the mass of the 1st ball: "))
m2 = float(input("Input the mass of the 2nd ball: "))
v1 = (2*9.8*h)**0.5
print("The velocity of the 1st ball after slide: ", v1,"m/s")
v22 = m1*(v1**2)/m2
v2 = v22**0.5
print("The velocity of the 2nd ball after collision:", v2,"m/s")