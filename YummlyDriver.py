from yummly import Client


class YummlyApiInfo:
    def __init__(self):
        pass

    Id = '1db8b5cc'
    Key = 'd470fadf2ef7bdcaec50be759255006a'


class RecipeQueryParameters:
    def __init__(self):
        pass

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

        return return_dictionary


def search_recipes(recipe_query_parameters):
    client = Client(api_id=YummlyApiInfo.Id, api_key=YummlyApiInfo.Key)
    return_dictionary = recipe_query_parameters.to_dictionary()
    return client.search(**return_dictionary)