num1=float(input("Enter first number = "))
num2=float(input("Enter second number = "))
num3=float(input("Enter last number = "))

if num1>num2:
    if num1>num3:
        print(num1)
    else:
        print(num3)

else:
    if num2>num1:
        print(num2)
    else:
        print(num3)