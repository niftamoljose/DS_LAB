n = int(input("enter the value:"))
a = 0
b = 1
sum = 0
print("the fibonacci seris is:",end ="")
while(sum <= n):
    print(sum, end=" ")
    a = b
    b = sum
    sum = a + b

