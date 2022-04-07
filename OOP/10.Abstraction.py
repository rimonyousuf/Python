from abc import ABC,abstractmethod

class Shape(ABC):
    def __init__(self,dim1,dim2):
        self.dim1=dim1
        self.dim2=dim2

    @abstractmethod
    def area(self):
        pass

class Triangle(Shape):
    def area(self):
        area=0.5*self.dim1*self.dim2
        print("Area of Triangle =",area)

class Rectangle(Shape):
    def area(self):
        area=self.dim1*self.dim2
        print("Area of Rectangle =",area)

t=Triangle(10,20)
t.area()

r=Rectangle(10,20)
r.area()