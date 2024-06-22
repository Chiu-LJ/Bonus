R = float(input("Please input a Richter scale value:"))
print("Richter scale value: ", R)
JJ = (1.5 * R) + 4.8
J = 10**JJ                          #將
print("Equivalence in Joules: ", J)
CTNT = 4.184 * (10**9)
TNT = J/CTNT                       #將J/ 4.184 * (10**9),代表將TNT算出來
print("Equivalence in tons of TNT: ", TNT)
L = J/2930200
print("Equivalence in the number of nutritious lunches: ", L)