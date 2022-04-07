class A:
    def display(self):
        print("I am inside A class")

class B:
    def display(self):
        print("I am inside B class")

class C(B,A):
    pass

ob=C()
ob.display()