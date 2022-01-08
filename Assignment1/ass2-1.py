class Complex:
    def __init__(self,real,imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(a,b):
        return Complex(a.real+b.real,a.imaginary+b.imaginary)

    def __sub__(a,b):
        return Complex(a.real-b.real,a.imaginary-b.imaginary)

    def __mul__(a,b):                        
        mulReal = a.real*b.real - a.imaginary*b.imaginary
        mulImg = a.real*b.imaginary + a.imaginary*b.real
        return Complex(mulReal,mulImg)

    def __eq__(a,b):
        return (a.real==b.real and a.imaginary==b.imaginary)

    def __str__(self):    
        if self.imaginary<0:
            return f"{self.real} - {-self.imaginary}i"                                   
        return f"{self.real} + {self.imaginary}i"

c1 = Complex(-2,3)
c2 = Complex(-4,9)
c3= Complex(4,-2)


print(c1+c2)
print(c1-c2)
print(c1*c2)
print(c2==c3)
print(c1==c2)