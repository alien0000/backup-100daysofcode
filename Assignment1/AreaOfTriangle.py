a=eval(input("Enter the first side of tringle: "))
b=eval(input("Enter the second side of tringle: "))
c=eval(input("Enter the thrid side of tringle: "))
if ((a+b>2) and (b+c>a) and (c+a>b)):
     s=(a+b+c)/2
     area=(s*(s-a)*(s-b)*(s-c))**0.5
    # print("area of the traiangle is %f" %area)
     print("area of the traiangle is ", area)
else:
    print("Invalid inputs!!!")