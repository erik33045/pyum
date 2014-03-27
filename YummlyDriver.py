from yummly import Client
import CalorieCalc.py


class YummlyApiInfo:
    def __init__(self):
        pass

    Id = '1db8b5cc'
    Key = 'd470fadf2ef7bdcaec50be759255006a'


class RecipeQueryParameters:
    def __init__(self):
        pass

    # include measurements & user info
    age = 0
    height = 0
    weight = 0
    gender = ""
    goal = ""
    activityLevel = ""
    mealsLeft = 3

    q = ""
    start = 0
    maxResult = 25
    requirePictures = False
    allowedIngredients = []
    excludedIngredients = []
    facetField = []
    allowedDiet = []
    allowedAlergy = []
    maxTotalTimeInSeconds = 0

    # Flavor stuff
    sweetMinFlavor = 0.0
    sweetMaxFlavor = 0.0
    meatyMinFlavor = 0.0
    meatyMaxFlavor = 0.0
    sourMinFlavor = 0.0
    sourMaxFlavor = 0.0
    bitterMinFlavor = 0.0
    bitterMaxFlavor = 0.0
    piquantMinFlavor = 0.0
    piquantMaxFlavor = 0.0

    #Nutrition stuff
    minFat = 0
    maxFat = 0
    minSodium = 0
    maxSodium = 0
    minCholesterol = 0
    maxCholesterol = 0
    minFattyAcids = 0
    maxFattyAcids = 0
    minCarbs = 0
    maxCarbs = 0
    minFiber = 0
    maxFiber = 0
    minProtein = 0
    maxProtein = 0
    minVitaminC = 0
    maxVitaminC = 0
    minCalcium = 0
    maxCalcium = 0
    minIron = 0
    maxIron = 0
    minSugar = 0
    maxSugar = 0
    minCalories = 0
    maxCalories = 0
    minVitaminA = 0
    maxVitaminA = 0

    def to_dictionary(self):
        return_dictionary = {"q": self.q}
        if self.age > 0.0:
            return_dictionary['age'] = self.age
        if self.weight > 0.0:
            return_dictionary['weight'] = self.weight
        if self.height > 0.0:
            return_dictionary['height'] = self.height
        if len(self.gender) > 0:
            return_dictionary['gender'] = self.gender
        if len(self.goal) > 0:
            return_dictionary['goal'] = self.gender
        if len(self.activityLevel) > 0:
            return_dictionary['activityLevel'] = self.activityLevel
        if self.mealsLeft > 0:
            return_dictionary['mealsLeft'] = self.mealsLeft
        if self.start > 0:
            return_dictionary['start'] = self.start
        if self.maxResult != 40:
            return_dictionary['maxResult'] = self.maxResult
        if self.requirePictures:
            return_dictionary['requirePictures'] = True
        if len(self.allowedIngredients) > 0:
            return_dictionary['allowedIngredient[]'] = self.allowedIngredients
        if len(self.excludedIngredients) > 0:
            return_dictionary['excludedIngredient[]'] = self.allowedIngredients
        if len(self.facetField) > 0:
            return_dictionary['facetField[]'] = self.facetField
        if len(self.allowedDiet) > 0:
            return_dictionary['allowedDiet[]'] = self.allowedDiet
        if len(self.allowedAlergy) > 0:
            return_dictionary['allowedAlergy[]'] = self.allowedAlergy,
        if self.maxTotalTimeInSeconds > 0:
            return_dictionary['maxTotalTimeInSeconds'] = self.maxTotalTimeInSeconds
        if self.sweetMinFlavor > 0.0:
            return_dictionary['flavor.sweet.min'] = self.sweetMinFlavor
        if self.sweetMaxFlavor > 0.0:
            return_dictionary['flavor.sweet.max'] = self.sweetMaxFlavor
        if self.meatyMinFlavor > 0.0:
            return_dictionary['flavor.meaty.min'] = self.meatyMinFlavor
        if self.meatyMaxFlavor > 0.0:
            return_dictionary['flavor.meaty.max'] = self.meatyMaxFlavor
        if self.sourMinFlavor > 0.0:
            return_dictionary['flavor.sour.min'] = self.sourMinFlavor
        if self.sourMaxFlavor > 0.0:
            return_dictionary['flavor.sour.max'] = self.sourMaxFlavor
        if self.bitterMinFlavor > 0.0:
            return_dictionary['flavor.bitter.min'] = self.bitterMinFlavor
        if self.bitterMaxFlavor > 0.0:
            return_dictionary['flavor.bitter.max'] = self.bitterMaxFlavor
        if self.piquantMinFlavor > 0.0:
            return_dictionary['flavor.piquant.min'] = self.piquantMinFlavor
        if self.piquantMaxFlavor > 0.0:
            return_dictionary['flavor.piquant.max'] = self.piquantMaxFlavor
        if self.minFat > 0.0:
            return_dictionary['nutrition.fat.min'] = self.minFat
        if self.maxFat > 0.0:
            return_dictionary['nutrition.fat.max'] = self.maxFat
        if self.minSodium > 0.0:
            return_dictionary['nutrition.sodium.min'] = self.minSodium
        if self.maxSodium > 0.0:
            return_dictionary['nutrition.sodium.max'] = self.maxSodium
        if self.minCholesterol > 0.0:
            return_dictionary['nutrition.cholesterol.min'] = self.minCholesterol
        if self.maxCholesterol > 0.0:
            return_dictionary['nutrition.cholesterol.max'] = self.maxCholesterol
        if self.minFattyAcids > 0.0:
            return_dictionary['nutrition.fattyacids.min'] = self.minFattyAcids
        if self.maxFattyAcids > 0.0:
            return_dictionary['nutrition.fattyacides.max'] = self.maxFattyAcids
        if self.minCarbs > 0.0:
            return_dictionary['nutrition.carbs.min'] = self.minCarbs
        if self.minCarbs > 0.0:
            return_dictionary['nutrition.carbs.max'] = self.maxCarbs
        if self.minFiber > 0.0:
            return_dictionary['nutrition.fiber.min'] = self.minFiber
        if self.maxFiber > 0.0:
            return_dictionary['nutrition.fiber.max'] = self.maxFiber
        if self.minProtein > 0.0:
            return_dictionary['nutrition.protein.min'] = self.minProtein
        if self.maxProtein > 0.0:
            return_dictionary['nutrition.protein.max'] = self.maxProtein
        if self.minVitaminC > 0.0:
            return_dictionary['nutrition.vitaminc.min'] = self.minVitaminC
        if self.maxVitaminC > 0.0:
            return_dictionary['nutrition.vitaminc.max'] = self.maxVitaminC
        if self.minCalcium > 0.0:
            return_dictionary['nutrition.calcium.min'] = self.minCalcium
        if self.maxCalcium > 0.0:
            return_dictionary['nutrition.calcium.max'] = self.maxCalcium
        if self.minIron > 0.0:
            return_dictionary['nutrition.iron.min'] = self.minIron
        if self.maxIron > 0.0:
            return_dictionary['nutrition.iron.max'] = self.maxIron
        if self.minSugar > 0.0:
            return_dictionary['nutrition.sugar.min'] = self.minSugar
        if self.maxSugar > 0.0:
            return_dictionary['nutrition.sugar.max'] = self.maxSugar
        if self.minCalories > 0.0:
            return_dictionary['nutrition.calories.min'] = self.minCalories
        if self.maxCalories > 0.0:
            return_dictionary['nutrition.calories.max'] = self.maxCalories
        if self.minVitaminA > 0.0:
            return_dictionary['nutrition.vitamina.min'] = self.minVitaminA
        if self.maxVitaminA > 0.0:
            return_dictionary['nutrition.vitamina.max'] = self.maxVitaminA


        # Test submit
        return return_dictionary


def search_recipes(recipe_query_parameters):
    # passed in partial recipe parameters object

    #call calculator to figure out desired meals
    calc = CalorieCalc(recipe_query_parameters)
    recipe_query_parameters["maxCalories"] = calc.get_calories() / recipe_query_parameters["mealsLeft"]

    #have yummly driver query data
    client = Client(api_id=YummlyApiInfo.Id, api_key=YummlyApiInfo.Key)
    return_dictionary = recipe_query_parameters.to_dictionary()
    return client.search(**return_dictionary)