a = int(input("Enter any number: "))
sum = 0
for i in range(1, a):
    if(a % i == 0):
        sum = sum + i
if (sum == a):
    print("The number is a Perfect number")
else:
    print("The number is not a Perfect number")