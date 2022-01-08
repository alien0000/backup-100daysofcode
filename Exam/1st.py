import math

val= float(input("Enter the value of x in order to find the series expansion of e^x: "))

result = math.exp(val)
print(f"The sum of the series is {round(result,2)}")