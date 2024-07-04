#write a code in python to calculate area of a triangle using Heron's formula

a = float(input("Enter the first side of triangle"))
b = float(input("Enter the second side of triangle"))
c = float(input("Enter the third side of triangle"))
print(a,b,c)
S=(a+b+c/2)
area = (S*(S-a)*(S-b)*(S-c))**0.5
print("Area of triangle = :"+str(area))
