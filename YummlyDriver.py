from yummly import Client

from CalorieCalc import CalorieCalc


class YummlyApiInfo:
    def __init__(self):
        pass

    #Vi's Key
    #Id = '17f360b5'
    #Key = '214819cbde16a118c615fc0061e6dc8b'

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
    activity_level = ""
    meals_left = 3
    diabetic = False
    calories_consumed = 0

    q = ""
    start = 0
    maxResult = 25
    requirePictures = False
    allowed_ingredients = []
    excluded_ingredients = []
    facet_field = []
    allowed_diet = []
    allergies = []
    max_total_time_in_seconds = 0

    # Flavor stuff
    sweet_min_flavor = 0.0
    sweet_max_flavor = 0.0
    meaty_min_flavor = 0.0
    meaty_max_flavor = 0.0
    sourMinFlavor = 0.0
    sourMaxFlavor = 0.0
    bitterMinFlavor = 0.0
    bitterMaxFlavor = 0.0
    piquantMinFlavor = 0.0
    piquantMaxFlavor = 0.0

    # Nutrition stuff
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
        return_dictionary = {}
        if self.q != "":
            return_dictionary["q"] = self.q
        if self.start > 0:
            return_dictionary['start'] = self.start
        if self.maxResult != 40:
            return_dictionary['maxResult'] = self.maxResult
        if self.requirePictures:
            return_dictionary['requirePictures'] = True
        if len(self.allowed_ingredients) > 0:
            return_dictionary['allowedIngredient[]'] = self.allowed_ingredients
        if len(self.excluded_ingredients) > 0:
            return_dictionary['excludedIngredient[]'] = self.excluded_ingredients
        if len(self.facet_field) > 0:
            return_dictionary['facetField[]'] = self.facet_field
        if len(self.allowed_diet) > 0:
            return_dictionary['allowedDiet[]'] = self.allowed_diet
        if len(self.allergies) > 0:
            return_dictionary['allowedAlergy[]'] = self.allergies,
        if self.max_total_time_in_seconds > 0:
            return_dictionary['maxTotalTimeInSeconds'] = self.max_total_time_in_seconds
        if self.sweet_min_flavor > 0.0:
            return_dictionary['flavor.sweet.min'] = self.sweet_min_flavor
        if self.sweet_max_flavor > 0.0:
            return_dictionary['flavor.sweet.max'] = self.sweet_max_flavor
        if self.meaty_min_flavor > 0.0:
            return_dictionary['flavor.meaty.min'] = self.meaty_min_flavor
        if self.meaty_max_flavor > 0.0:
            return_dictionary['flavor.meaty.max'] = self.meaty_max_flavor
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


class UserPreferences:
    def __init__(self):
        pass

    age = 0
    height = 0
    weight = 0
    gender = ""
    goal = ""
    activity_level = ""
    meals_left = 3
    diabetic = False
    calories_consumed = 0
    allowed_diet = []
    allergies = []

def search_recipes(recipe_query_parameters):
    # passed in partial recipe parameters object
    if not recipe_query_parameters.ignore_user_preferences:
        # call calculator to figure out desired meals
        calc = CalorieCalc(recipe_query_parameters)

        # calculate max calories for meal
        recipe_query_parameters.max_calories = calc.get_calories() - recipe_query_parameters.caloriesConsumed

        if recipe_query_parameters.mealsLeft > 0:
            recipe_query_parameters.max_calories /= recipe_query_parameters.mealsLeft

        #diabetic info
        if recipe_query_parameters.diabetic:
            recipe_query_parameters.max_carbs = 65
            recipe_query_parameters.min_carbs = 45
            recipe_query_parameters.max_sodium = 0.4

    # have yummly driver query data
    client = Client(api_id=YummlyApiInfo.Id, api_key=YummlyApiInfo.Key)
    recipe_query_parameters.q = recipe_query_parameters.allowed_ingredients[0]
    return_dictionary = recipe_query_parameters.to_dictionary()
    return client.search(**return_dictionary)


def django_query_to_parameter_object(post_data_dictionary, user_preferences):
    parameter_object = RecipeQueryParameters()

    if len(post_data_dictionary['current_weight']):
        parameter_object.weight = int(post_data_dictionary['current_weight'])

    if len(post_data_dictionary['in_ingredients']):
        parameter_object.allowed_ingredients = post_data_dictionary['in_ingredients'].split(',')

    if len(post_data_dictionary['ex_ingredients']):
        parameter_object.excluded_ingredients = post_data_dictionary['ex_ingredients'].split(',')

    if len(post_data_dictionary['prep_time']):
        parameter_object.max_total_time_in_seconds = int(post_data_dictionary['prep_time'])

    if len(post_data_dictionary['amount-sweetness']):
        sweetness = post_data_dictionary['amount-sweetness'].split('-')
        parameter_object.sweet_min_flavor = float(sweetness[0]) / 10.00
        parameter_object.sweet_max_flavor = float(sweetness[1]) / 10.00

    if len(post_data_dictionary['amount-meatiness']):
        meatiness = post_data_dictionary['amount-meatiness'].split('-')
        parameter_object.meaty_min_flavor = float(meatiness[0]) / 10.00
        parameter_object.meaty_max_flavor = float(meatiness[1]) / 10.00

    if post_data_dictionary['ignore_user_preferences']:
        parameter_object.ignore_user_preferences = True
    else:
        parameter_object.age = user_preferences.age
        parameter_object.activity_level = user_preferences.activity_level
        parameter_object.allowed_diet = user_preferences.allowed_diet
        parameter_object.allergies = user_preferences.allergies
        parameter_object.diabetic = user_preferences.diabetic
        parameter_object.goal = user_preferences.goal
        parameter_object.meals_left = user_preferences.meals_left
        parameter_object.calories_consumed = user_preferences.calories_consumed
        parameter_object.height = user_preferences.height

    return parameter_object
