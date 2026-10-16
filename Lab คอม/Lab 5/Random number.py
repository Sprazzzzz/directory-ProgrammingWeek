import random

def random_number(x):
    num = []

    for i in range(x):
        num.append(random.randint(1, 100))
    return num

random_numbers = random_number(10)

print(random_numbers)