
import numpy as np
x=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(x)
print(" Display the cube of each element of the matrix using different methods (use multiply(), *, power(),**)")
print(np.power(x,3))
print(np.multiply(x,(x*x)))
print(x*x*x)
print(x**3)
print("Display identity matrix of the given square matrix.")
b=np.identity(3,dtype=int)
print(b)
print("Display each element of the matrix to different powers.")
out=np.power(x,x)
print(out)
print ("Create a matrix Y with same dimension as X and perform the operation X 2 +2Y")
y = np.arange(11,20).reshape(3,3)
print("perform the operation X^2 +2Y: \n",np.add((np.power(x,2)),(np.multiply(y,2))))

