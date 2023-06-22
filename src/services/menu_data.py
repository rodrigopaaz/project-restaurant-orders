import csv
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str):
        self.dishes = self.load_menu_data(source_path)

    def get_ingredients(self):
        return list(self.dishes)

    def load_menu_data(self, source_path):
        recipes = []
        with open(source_path, newline='') as file:
            csv_file = csv.reader(file)
            next(csv_file)
            for items in csv_file:
                name, dish_price, ingredient_name, ingredient_quantity = items
                ingredient_quantity = int(ingredient_quantity)

                dish = next((recipe for recipe in recipes if
                             recipe.name == name), None)
                if dish is None:
                    dish = Dish(name, float(dish_price))
                    recipes.append(dish)

                ingredient = Ingredient(ingredient_name)
                dish.add_ingredient_dependency(ingredient, ingredient_quantity)

        return recipes
