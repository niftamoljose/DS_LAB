def coprime(a, b):
    hcf = 1

    for i in range(1, a + 1):
        if a % i == 0 and b % i == 0:
            hcf = i

    return hcf == 1

fi = int(input("Enter first number:"))
se = int(input("Enter second number:"))

if coprime(fi, se):
    print("they are coprimes")
else:
    print("not coprimes")