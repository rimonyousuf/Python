#built in polymorphic function
print(len("Yasir Yousuf Rimon"))
print(len([10,20,30]))

#user defined polymorphic function
def add(x,y,z=0):
    return x+y+z

print(add(2,3))
print(add(2,3,6))