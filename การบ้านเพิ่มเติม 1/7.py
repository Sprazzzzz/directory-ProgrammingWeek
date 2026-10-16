#1)
numbers = list(map(float, input("Enter numbers: ").split()))

numbers.sort()

n = len(numbers)

if n % 2 == 1:
    median = numbers[n // 2]
else:
    median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2

print("Median =", median)

#2)
def find_median():
    numbers = list(map(float, input("Enter numbers: ").split()))

    numbers.sort()

    n = len(numbers)

    if n % 2 == 1:
        median = numbers[n // 2]
    else:
        median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2

    print("Median =", median)

find_median()

#3)
def find_median(numbers):
    numbers.sort()

    n = len(numbers)

    if n % 2 == 1:
        median = numbers[n // 2]
    else:
        median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2

    print("Median =", median)

numbers = list(map(float, input("Enter numbers: ").split()))

find_median(numbers)

#4)
def find_median(numbers):
    numbers.sort()

    n = len(numbers)

    if n % 2 == 1:
        return numbers[n // 2]
    else:
        return (numbers[n // 2 - 1] + numbers[n // 2]) / 2

numbers = list(map(float, input("Enter numbers: ").split()))

median = find_median(numbers)

print("Median =", median)