temp_data = [
    [34,35,36,37,38,39,40], #week1
    [28,29,30,31,32,33,34], #week2
    [22,23,24,25,26,27,28], #week3
    [16,17,18,19,20,21,22], #week4
]

def week_averarge(temp_data, week_index):
    temp_average =  temp_data[week_index]
    return sum(temp_average) / len(temp_average)

def week_max(temp_data, week_index):
    temp_max = temp_data[week_index]
    return max(temp_max)

def week_min(temp_data, week_index):
    temp_min = temp_data[week_index]
    return min(temp_min)

week_index = 0  # 0-3 for week 1-4
print("Week Average:", week_averarge(temp_data, week_index))
print("Week Maximum:", week_max(temp_data, week_index))
print("Week Minimum:", week_min(temp_data, week_index))

