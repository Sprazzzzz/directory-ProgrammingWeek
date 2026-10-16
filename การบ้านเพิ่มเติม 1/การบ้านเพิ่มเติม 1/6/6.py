
import random
def random_check():
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