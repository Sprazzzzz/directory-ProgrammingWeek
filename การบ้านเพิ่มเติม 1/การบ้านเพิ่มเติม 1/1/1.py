#1)
import random
num = []
for i in range(20):
    num.append(random.randint(1, 100))
print(num)

#2)
def number():
    num = []
    for i in range(20):
        num.append(random.randint(1, 100))  
print(num)

number()

#3)
def number(x):
    num = []
    for i in range(x):
        num.append(random.randint(1, 100))  
print(num)

number(20)

#4)
def number(x):
    num = []
    for i in range(x):
        num.append(random.randint(1, 100))  
    return num

print(number(20))