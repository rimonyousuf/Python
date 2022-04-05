class Student:
    roll=""
    gpa=""

    def set_value(self,roll,gpa):
        self.roll=roll
        self.gpa=gpa

    def display(self):
        print(f"Roll : {self.roll}, GPA : {self.gpa}")

Arafat=Student()
Arafat.set_value(101,4.78)
Arafat.display()

Monir=Student()
Monir.set_value(102,2.63)
Monir.display()