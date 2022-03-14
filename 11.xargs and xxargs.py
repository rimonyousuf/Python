def add(*numbers):
    sum=0
    for num in numbers:
        sum=sum+num
    print("sum =",sum)

add(10,20)
add(10,20,30)
add(10,20.5,30)

def student(**details):
    print(details)

student(Id=101,Name="Rimon Yousuf")
student(Id=102,Name="Arafat Bati")