#map
def square(x):
    return x*x
num=[2,4,6,8,10]

result=list(map(square,num))
print("Square of this function",result)

#filter
number=[1,2,3,4,5,6,7,8,9,]
result=list(filter(lambda x:x%2==0,number))
print("After filtering",result)