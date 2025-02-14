a= float( input("length of side 1: "))
b = float( input("length of side 2: "))
c= float( input("length of side 3: "))

s = (a+b+c)/2

area = (s*(s-a)*(s-b)*(s-c))**0.5

print("area is", area)