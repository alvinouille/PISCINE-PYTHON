from datetime import datetime
from recipe import Recipe

class Book:
    def __init__(self, name_p : str = "", p_recipes_list : dict = {}):
        self.name = name_p
        self.recipes_list = p_recipes_list
        self.last_update = datetime.now()
        self.creation_date = datetime.now()

    def get_last_update(self):
        return (self.last_update)

    def set_last_update(self):
        self.last_update = datetime.now()

    def get_recipe_by_name(self, name):
        """Get a recipe with the name x and returns the instance"""
        liste1 = self.recipes_list["lunch"]
        liste2 = self.recipes_list["starter"]
        liste3 = self.recipes_list["dessert"]
        for i in liste1:
            if i.name == name:
                print(i)
                return i
        for i in liste2:
            if i.name == name:
                print(i)
                return i
        for i in liste3:
            if i.name == name:
                print(i)
                return i
    
    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type"""
        liste = []
        for i in self.recipes_list[recipe_type]:
            liste.append(i.name)
        return liste


    def add_recipe(self, recipe):
        if isinstance(recipe, Recipe):
            self.set_last_update()
            self.recipes_list[recipe.recipe_type].append(recipe)


# dictionnaire = {"starter" :[], "lunch":[], "dessert":[]}
# tourte = Recipe("Tourte", 3, 120, ["Jambon", "Creme", "Oeufs"], None, "lunch")
# saladenicoise = Recipe("Salade nicoise", 3, 45, ["Salade", "Blanc de dinde", "Cornichons"], "Tout melanger et deguster", "lunch")
# mybook = Book("Hello", dictionnaire)
# print(mybook.last_update)
# print(f"creation = {mybook.creation_date}")

# mybook.add_recipe(tourte)
# mybook.add_recipe(saladenicoise)
# print(f"Recipes added, update : {mybook.get_last_update()}")
# mybook.get_recipe_by_name("Tourte")
# for i in mybook.get_recipes_by_types("lunch"):
#     print(i)
