a = int(input("enter the length of side1:"))
b = int(input("enter the length of side2:"))
c = int(input("enter the length of side3:"))
if(a==b==c):
    print("the triangle is equilateral triangle")
elif(a==b or b==c or c==a):
    print("the triangle is isosceles triangle")
else:
    print("the triangle is scalene")