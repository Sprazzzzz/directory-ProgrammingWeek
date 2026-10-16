#1)
import random
for i in range(10):
    x = random.randint(1, 100)
    y = random.randint(0, 5)

    result = 1

    for j in range(y):
        result = result * x

    print("p(", x, ",", y, ") =", result)

#2) 
import random
def power():
    for i in range(10):
        x = random.randint(1, 100)
        y = random.randint(0, 5)

        result = 1

        for j in range(y):
            result = result * x

        print("p(", x, ",", y, ") =", result)

power()

#3)
import random
def power(n):
    for i in range(n):
        x = random.randint(1, 100)
        y = random.randint(0, 5)

        result = 1

        for j in range(y):
            result = result * x

        print("p(", x, ",", y, ") =", result)

power(10)

#4)
import random
def power(x, y):
    result = 1

    for i in range(y):
        result = result * x

    return result

for i in range(10):
    x = random.randint(1, 100)
    y = random.randint(0, 5)

    result = power(x, y)

    print("p(", x, ",", y, ") =", result)

print(power(2, 3))