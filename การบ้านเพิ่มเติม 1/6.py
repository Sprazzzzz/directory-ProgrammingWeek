#1)
import random
for i in range(10):
    x = random.randint(100,1000)

    print(x)
    
    if x > 800:
        print(x, "is greater than 800")

#2)
import random
def check_greater_than_800():
    for i in range(10):
        x = random.randint(100,1000)

        print(x)
        
        if x > 800:
            print(x, "is greater than 800")

check_greater_than_800()

#3)
import random
def check_greater_than_800(x):
    for i in range(x):
        num = random.randint(100,1000)

        print(num)
        
        if num > 800:
            print(num, "is greater than 800")

check_greater_than_800(10)

#4)
import random
def random_check(n, limit):
    numbers = []

    for i in range(n):
        x = random.randint(100, 1000)
        numbers.append(x)

    return numbers

result = random_check(10, 800)

for x in result:
    print(x)

    if x > 800:
        print(x, "is greater than 800")