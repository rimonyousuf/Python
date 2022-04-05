class Student:
    roll=""
    gpa=""

    def __init__(self,roll,gpa):
        self.roll=roll
        self.gpa=gpa

    def display(self):
        print(f"Roll : {self.roll}, GPA : {self.gpa}")

Arafat=Student(101,4.78)
Arafat.display()

Monir=Student(102,2.63)
Monir.display()