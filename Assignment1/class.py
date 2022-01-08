class Complex:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary
    
    def __add__(self,a,b):
        return Complex(a.real+b.real ,a.imaginary+b.imaginary)
    
    def __sub__(self,a,b):
        return Complex(a.real-b.real,a.imaginary-b.imaginary)
    def __mul__(self,a,b):
        pass