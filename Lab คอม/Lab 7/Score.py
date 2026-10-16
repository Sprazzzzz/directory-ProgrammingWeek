score_data = [
    [80, 75, 90, 85], # first student scores
    [60, 70, 65, 80], # second student scores
    [95, 90, 85, 100] # third student scores
]

#Total score from a student
def Total_score(score_data, student_index):
    total = 0

    for score in score_data[student_index]:
        total += score

    return total

#Student average score
def Student_average(score_data, student_index):
    scores = score_data[student_index]

    return sum(scores) / len(scores)


#Output the total and average score for each student
for i in range(len(score_data)):
    print(f"Student number {i + 1}")
    print(f"Total score: {Total_score(score_data, i)}")
    print(f"Average score: {Student_average(score_data, i)}")
    print()






        
        