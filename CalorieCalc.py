class CalorieCalc:
    age = 0
    weight = 0
    height = 0
    gender = ""
    goal = ""
    activityLevel = ""

    def __init__(self, info):
        self.age = info['age']
        self.weight = info['weight']
        self.height = info['height']
        self.gender = info['gender']
        self.goal = info['goal']
        self.activityLevel = info['activityLevel']

    def get_bmi(self):
        bmi = ((self.weight * 703.0) / (self.height ** 2.0))
        bmi = round(bmi, 1)
        return bmi


    def get_bmr(self):
        if self.gender == "Female":
            bmr = 655 + (4.35 * self.weight) + (4.7 * self.height) - (4.7 * self.age)
        if self.gender == "Male":
            bmr = 66 + (6.23 * self.weight) + (12.7 * self.height) - (6.8 * self.age)
        return bmr


    def get_calories(self):
        calories = 0
        bmr = self.get_bmr()
        if self.activityLevel == "sedentary":
            calories = bmr * 1.2
        elif self.activityLevel == "lightly active":
            calories = bmr * 1.375
        elif self.activityLevel == "moderately active":
            calories = bmr * 1.55
        elif self.activityLevel == "very active":
            calories = bmr * 1.725
        elif self.activityLevel == "extra active":
            calories = bmr * 1.9

        #lose 2 pounds per week
        if self.goal == "Lose 2":
            calories -= 1000

        #lose 1 pound per week
        elif self.goal == "Lose 1":
            calories -= 500

        #lose 1/2 pound per week
        elif self.goal == "Lose 1/2":
            calories -= 250

        #gain 2 pounds per week
        elif self.goal == "Gain 2":
            calories += 1000

        #gain 1 pound per week
        elif self.goal == "Gain 1":
            calories += 500

        #gain 1/2 pound per week
        elif self.goal == "Gain 1/2":
            calories += 250

        #if BMI in normal range, maintain weight

        calories = int(calories)
        return calories

#testing functions
test_dictionary = {"height": 71, "weight": 180, "age": 22, "gender": "Male", "goal": "Lose 1",
                   "activityLevel": "lightly active"}
calc = CalorieCalc(test_dictionary)
cals = calc.get_calories()
print("Calories per day: " + str(cals))

