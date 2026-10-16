numbers = list(map(float, input("Enter numbers: ").split()))

numbers.sort()

n = len(numbers)

if n % 2 == 1:
    median = numbers[n // 2]
else:
    median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2

print("Median =", median)