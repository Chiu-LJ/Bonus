v = float(input("Input velocity: "))
c = 299792458
Per = v / c
print("Percentage of light speed = ", Per)
z = (c**2 - v**2)/c**2
q = z**0.5
ga = 1/q
Al = 4.3 / ga
print("Travel time to Alpha Centauri = ",Al)
Ba = 6.0/ga
print("Travel time to Barnard's Star =",Ba)
Be = 309/ga
print("Travel time to Betelgeuse (in the Milky Way)",Be)
An = 2000000/ga
print("Andromeda Galaxy (closest galaxy)=",An)