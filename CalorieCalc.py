def get_bmi(height, weight):
    bmi = ((weight * 703.0) / (height ** 2.0))
    bmi = round(bmi, 1)
    return bmi


def get_bmr(height, weight, gender, age):
    if gender == "female":
        bmr = 655 + (4.35 * weight) + (4.7 * height) - (4.7 * age)
    if gender == "male":
        bmr = 66 + (6.23 * weight) + (12.7 * height) - (6.8 * age)
    return bmr


def get_calories(bmr, activity_level, goal, ppw):
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

    #if user wishes to lose weight, eat at ppw * 500 deficit
    if goal == "lose":
        calories -= 500.0 * ppw

    #if user wishes to gain wait, eat at ppw * 500 surplus
    elif goal == "gain":
        calories += 500.0 * ppw

    #if BMI in normal range, maintain weight

    calories = int(calories)
    return calories

#testing functions
BMI = get_bmi(71, 180)
print("BMI: " + str(BMI))
BMR = get_bmr(71, 180, "male", 22)
print("BMR: " + str(BMR))
cals = get_calories(BMR, "sedentary", "lose", 1)
print("Calories per day: " + str(cals))



