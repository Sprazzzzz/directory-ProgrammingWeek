import random
sum = 0
x = 0

def Choice_mode(n):
    if n == 1:
        Input_mode()

    elif n == 2:
        Random_mode()

    else:
        print("Invalid input. Please choose 1 or 2.")

def Input_mode():
    global total_sum
    global x

    while x != -1:
        x = int(input("input any integer, input -1 to end : "))
        total_sum += x

    print ("Sum of this session is : ", total_sum)

def Random_mode():
    global total_sum
    global x

    while x != -1:
        x = random.randint(-10, 10)
        print("Random number generated:", x)
        total_sum += x


Choice_mode(n)