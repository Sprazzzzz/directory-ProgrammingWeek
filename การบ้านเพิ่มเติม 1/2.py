#1)
for n in range (2,101):
    for i in range(2,n):
        if n % i == 0:
            break
    else:
        print(n)

#2)
def prime_numbers():
    for n in range(2, 101):
        prime = True
        for i in range(2, n):
            if n % i == 0:
                prime = False
                break
        if prime:
            print(n)    

prime_numbers()

#3)
def prime_numbers(x):
    for n in range(2, x + 1):
        prime = True
        for i in range(2, n):
            if n % i == 0:
                prime = False
                break
        if prime:
            print(n)    

prime_numbers(100)

#4)
def find_prime(x):
    primes = []

    for n in range(2, x + 1):
        prime = True

        for i in range(2, n):
            if n % i == 0:
                prime = False
                break

        if prime:
            primes.append(n)

    return primes

result = find_prime(100)

print(result)