def primechecker(num):
    isprime=True
    for i in range(2, num):
        if num % i == 0:
            isprime=False
    if isprime:
        print(f"{num} is a prime number!!")
    else:
        print(f"{num} is not a prime number!!")

n=int(input("Enter the number for prime check: "))
primechecker(num=n)