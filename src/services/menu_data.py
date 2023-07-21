import csv
from src.models.ingredient import Ingredient
from src.models.dish import Dish


# Req 3

class MenuData:
    def __init__(self, source_path: str) -> None:
        self.path = source_path
        self.dishes = set()
        my_dish = {}
        with open(source_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['dish'] not in my_dish:
                    my_dish[row['dish']] = Dish(
                        row['dish'], float(row['price'])
                        )
                    ingredient = Ingredient(row['ingredient'])
                    my_dish[row['dish']].add_ingredient_dependency(
                        ingredient,  int(row['recipe_amount']))
                else:
                    ingredient = Ingredient(row['ingredient'])
                    my_dish[row['dish']].add_ingredient_dependency(
                        ingredient,  int(row['recipe_amount'])
                        )
        self.dishes = set(my_dish.values())
