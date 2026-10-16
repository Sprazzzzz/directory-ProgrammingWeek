#Multiply
def multiply():
    a=int(input("Enter first number: "))

    for i in range(1,13):
        sum = a * i
        print(f"{a} x {i} = {sum}")

multiply()
