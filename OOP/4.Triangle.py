class Triangle:

    def __init__(self,base,height):
        self.base=base
        self.height=height

    def calculate_area(self):
        area=0.5*self.base*self.height
        print(f"Calculate area =",area)

t=Triangle(10,20)
t.calculate_area()
