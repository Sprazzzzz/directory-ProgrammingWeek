def grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

score = float(input("Enter the score: "))
letter_grade = grade(score)
print(f"The letter grade for a score of {score} is: {letter_grade}")
