def get_bmi(height, weight):
    bmi = ((weight * 703) / (height ** 2))
    return bmi


def get_bmr(height, weight, gender, age):
    if gender == "female":
        bmr = 655 + (4.35 * weight) + (4.7 * height) - (4.7 * age)
    if gender == "male":
        bmr = 66 + (6.23 * weight) + (12.7 * height) - (6.8 * age)
    return bmr


def get_calories(bmi, bmr, activity_level):
    calories = 0
    if activity_level == "sedentary":
        calories = bmr * 1.2
    elif activity_level == "lightly active":
        calories = bmr * 1.375
    elif activity_level == "moderately active":
        calories = bmr * 1.55
    elif activity_level == "very active":
        calories = bmr * 1.725
    elif activity_level == "extra active":
        calories = bmr * 1.9

    #if underweight, eat at 500 calorie surplus (1 pound per week)
    if bmi < 18.5:
        calories += 500

    #if overweight, eat at 500 calorie deficit
    elif bmi >= 25:
        calories -= 500

    #if BMI in normal range, maintain weight

    calories = int(calories)
    return calories

#testing functions
BMI = get_bmi(71, 180)
print(BMI)
BMR = get_bmr(71, 180, "male", 22)
cals = get_calories(BMI, BMR, "lightly active")
print(cals)



