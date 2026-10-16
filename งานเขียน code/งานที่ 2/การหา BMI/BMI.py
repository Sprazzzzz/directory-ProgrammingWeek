def calculate_bmi():
    weight = 70 #Information about weight
    height =  1.75 #Information about height

    # Calculate BMI
    bmi = weight / (height ** 2) 

    # Determine BMI category
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obesity"

    # Display the results
    print(f"Weight = {weight} kg")
    print(f"Height = {height} m")
    print(f"BMI = {bmi}")
    print(f"Category = {category}")

calculate_bmi()


