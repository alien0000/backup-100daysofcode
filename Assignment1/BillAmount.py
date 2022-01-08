a=int(input("Enter the consumed unit:"))

if a>=0 and a <=50:
    b=a*5.0
    print(f"The bill amount is:{b}Rs ")
elif a>=51 and a<=100:
    b=50*5.0+(a-50)*6.5
    print(f"The bill amount is:{b}Rs ")
elif a>=101 and a<=200: 
    b=50*5.0+50*6.5+(a-100)*8.0
    print(f"The bill amount is:{b}Rs ")
elif a>=201:
    b=50*5+50*6.5+100*8.0+(a-200)*10.0
    print(f"The bill amount is:{b}Rs ")
else:
    print("Invalid amount of unit")