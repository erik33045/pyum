from yummly import Client

from CalorieCalc import CalorieCalc


class YummlyApiInfo:
    def __init__(self):
        pass

    # Erik's Key
    #Id = '1db8b5cc'
    #Key = 'd470fadf2ef7bdcaec50be759255006a'

    #Mark's Key
    #Id= '694cee2e'
    #Key = '392df3bc63518ea410eef68eb6da066e'

    #Greg's Key
    Id = 'c406a4d1'
    Key = '654c0671661c94a799e761615c36cdd5'


class RecipeQueryParameters:
    def __init__(self):
        pass

    # include measurements & user info
    ignore_user_preferences = False
    age = 0
    height = 0
    weight = 0
    gender = ""
    goal = ""
    activityLevel = ""
    mealsLeft = 3
    diabetic = False
    caloriesConsumed = 0

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
    minFatSat = 0
    maxFatSat = 0
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
    minTransFat = 0
    maxTransFat = 0


    def to_dictionary(self):
        return_dictionary = {"q": self.q}
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
            return_dictionary['nutrition.FAT.min'] = self.minFat
        if self.maxFat > 0.0:
            return_dictionary['nutrition.FAT.max'] = self.maxFat
        if self.minSodium > 0.0:
            return_dictionary['nutrition.NA.min'] = self.minSodium
        if self.maxSodium > 0.0:
            return_dictionary['nutrition.NA.max'] = self.maxSodium
        if self.minCholesterol > 0.0:
            return_dictionary['nutrition.CHOLE.min'] = self.minCholesterol
        if self.maxCholesterol > 0.0:
            return_dictionary['nutrition.CHOLE.max'] = self.maxCholesterol
        if self.minFatSat > 0.0:
            return_dictionary['nutrition.FATSAT.min'] = self.minFatSat
        if self.maxFatSat > 0.0:
            return_dictionary['nutrition.FATSAT.max'] = self.maxFatSat
        if self.minCarbs > 0.0:
            return_dictionary['nutrition.CHOCDF.min'] = self.minCarbs
        if self.minCarbs > 0.0:
            return_dictionary['nutrition.CHOCDF.max'] = self.maxCarbs
        if self.minFiber > 0.0:
            return_dictionary['nutrition.FIBTG.min'] = self.minFiber
        if self.maxFiber > 0.0:
            return_dictionary['nutrition.FIBTG.max'] = self.maxFiber
        if self.minProtein > 0.0:
            return_dictionary['nutrition.PROCNT.min'] = self.minProtein
        if self.maxProtein > 0.0:
            return_dictionary['nutrition.PROCNT.max'] = self.maxProtein
        if self.minVitaminC > 0.0:
            return_dictionary['nutrition.VITC.min'] = self.minVitaminC
        if self.maxVitaminC > 0.0:
            return_dictionary['nutrition.VITC.max'] = self.maxVitaminC
        if self.minCalcium > 0.0:
            return_dictionary['nutrition.CA.min'] = self.minCalcium
        if self.maxCalcium > 0.0:
            return_dictionary['nutrition.CA.max'] = self.maxCalcium
        if self.minIron > 0.0:
            return_dictionary['nutrition.FE.min'] = self.minIron
        if self.maxIron > 0.0:
            return_dictionary['nutrition.FE.max'] = self.maxIron
        if self.minSugar > 0.0:
            return_dictionary['nutrition.SUGAR.min'] = self.minSugar
        if self.maxSugar > 0.0:
            return_dictionary['nutrition.SUGAR.max'] = self.maxSugar
        if self.minCalories > 0.0:
            return_dictionary['nutrition.ENERC_KCAL.min'] = self.minCalories
        if self.maxCalories > 0.0:
            return_dictionary['nutrition.ENERC_KCAL.max'] = self.maxCalories
        if self.minVitaminA > 0.0:
            return_dictionary['nutrition.VITA_IU.min'] = self.minVitaminA
        if self.maxVitaminA > 0.0:
            return_dictionary['nutrition.VITA_IU.max'] = self.maxVitaminA
        if self.minTransFat > 0.0:
            return_dictionary['nutrition.FATRN.min'] = self.minTransFat
        if self.maxTransFat > 0.0:
            return_dictionary['nutrition.FATRN.max'] = self.maxTransFat

        return return_dictionary


def search_recipes(recipe_query_parameters):
    # passed in partial recipe parameters object
    if not recipe_query_parameters.ignore_user_preferences:
        #call calculator to figure out desired meals
        calc = CalorieCalc(recipe_query_parameters)

        #calculate max calories for meal
        recipe_query_parameters.maxCalories = calc.get_calories() - recipe_query_parameters.caloriesConsumed

        if recipe_query_parameters.mealsLeft > 0:
            recipe_query_parameters.maxCalories /= recipe_query_parameters.mealsLeft

        #diabetic info
        if recipe_query_parameters.diabetic == True:
            recipe_query_parameters.maxCarbs = 65
            recipe_query_parameters.minCarbs = 45
            recipe_query_parameters.maxSodium = 0.4

    #have yummly driver query data
    client = Client(api_id=YummlyApiInfo.Id, api_key=YummlyApiInfo.Key)
    return_dictionary = recipe_query_parameters.to_dictionary()
    return client.search(**return_dictionary)


# This is a test method to ensure proper functionality
def find():
    x = RecipeQueryParameters()
    x.activityLevel = "sedentary"
    x.age = 20
    x.caloriesConsumed = 2000
    x.gender = "Male"
    x.goal = "Lose 1"
    x.height = 72
    x.weight = 250
    x.mealsLeft = 1
    x.diabetic = True
    x.q = "bacon"
    results = search_recipes(x)
    print str(results)


find()