import math
import cmath

a = eval(input("Enter coefficient of x square :"))
b = eval(input("Enter coefficient of x :"))
c = eval(input("Enter constant value in equation :"))
d = b**2 - 4*a*c
if (d >= 0):
	r1 = (-b + math.sqrt(d))/2*a
	r2 = (-b - math.sqrt(d))/2*a
	print("Roots of Quadratic Equation are =>", r1,",", r2)
elif (d <0):
	r1 = (-b + cmath.sqrt(d))/2*a
	r2 = (-b - cmath.sqrt(d))/2*a
	print("Roots of Quadratic Equation are =>", r1,",", r2)