
import re

class Input:
    def __init__(self, file):
        with open(file) as f:
            inputFoods = f.readlines()
            self.foods = []
            self.allIngredients = set()
            self.allergenMap = dict()
            for inputFood in inputFoods:
                foodParts = re.match('(.+) \(contains (.+)\)', inputFood)
                for allergen in foodParts[2].split(','):
                    if self.allergenMap.get(allergen) is None:
                        self.allergenMap[allergen] = set(foodParts[1].split())
                    else
                        self.allergenMap[allergen] |= set(foodParts[1].split())

input = Input('2020/input/day_21.txt')
for food in input.foods:
    print(food.allergens)
    print(food.ingredients)