# 1+2+3+....+n
n=int(input("Enter last number for first math = "))
sum=0
for x in range(1,n+1,1):
    sum=sum+x
print("Sum for first math is",sum)
print()

# 2+4+6+....+n
m=int(input("Enter last number for second math = "))
sum=0
for x in range(2,m+1,2):
    sum=sum+x
print("Sum for second math is",sum)
print()

# 1^1+2^2+3^3+....+n
y=int(input("Enter last number for third math = "))
sum=0
for x in range(1,y+1,1):
    sum=sum+x*x
print("Sum for third math is",sum)
print()