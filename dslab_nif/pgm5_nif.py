import cmath
a = float(input("enter the value of a:"))
b = float(input("enter the value of b:"))
c = float(input("enter the value of c:"))
d = (b*b) - (4*a*c)
if(d>0):
    r1 = (-b  + cmath.sqrt(d)) / (2 * a)
    r2 = (-b - cmath.sqrt(d)) / (2 * a)
    print(" the roots are real and different ",r1,r2)
elif(d==0):
    r1=r2=-b/ (2 * a)
    print("the roots are real and same")
else:
    real = -b / (2 * a)
    img = cmath.sqrt(d) / (2 * a)
    print("complex roots", real, "+", img, "and", real, "-", img)