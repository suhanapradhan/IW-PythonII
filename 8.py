def is_prime(num):
    if num <2:
        return False
    if num == 2:
        return True
    else:
        for i in range(2,num):
           if num%i == 0 and num!=i:
                return "not a prime"
    return "is a prime"
n=int(input("enter a number"))
print(is_prime(n))