#1)
number = [300, 800, 600, 400, 300, 900, 550, 650, 420, 601]

for x in number:
    if x > 500:
        print(x, "is greater than 500")

#2)
def check_greater_than_500():
    number = [300, 800, 600, 400, 300, 900, 550, 650, 420, 601]

    for x in number:
        if x > 500:
            print(x, "is greater than 500")

check_greater_than_500()

#3)
def check_greater_than_500(number):
    for x in number:
        if x > 500:
            print(x, "is greater than 500")

check_greater_than_500([300, 800, 600, 400, 300, 900, 550, 650, 420, 601])

#4)
def check_numbers(numbers, limit):
    result = []

    for x in numbers:
        if x > limit:
            result.append(x)

    return result

numbers = [300, 800, 600, 400, 300, 900, 550, 650, 420, 601]

result = check_numbers(numbers, 500)

print("ค่าที่มากกว่า 500:")
print(result)