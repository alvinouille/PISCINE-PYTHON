from book import Book
from recipe import Recipe

dictionnaire = {"starter" :[], "lunch":[], "dessert":[]}
print("creation 2 objects Recipe")
tourte = Recipe("Tourte", 3, 120, ["Jambon", "Creme", "Oeufs"], None, "lunch")
saladenicoise = Recipe("Salade nicoise", 3, 45, ["Salade", "Blanc de dinde", "Cornichons"], "Tout melanger et deguster", "lunch")
print("creation 1 object Book")
mybook = Book("Hello", dictionnaire)
print(f"Creation = {mybook.creation_date}")
print(f"Last update = {mybook.last_update}")
lol = 2
mybook.add_recipe(tourte)
mybook.add_recipe(saladenicoise)
mybook.add_recipe(lol)
print(f"Recipes added, last update : {mybook.get_last_update()}")
print("Getting the recipe of 'Salade nicoise'")
mybook.get_recipe_by_name("Salade nicoise")
print("Getting recipes from type 'lunch'")
for i in mybook.get_recipes_by_types("lunch"):
    print(i)
print("Getting recipes from type 'starter'")
for a in mybook.get_recipes_by_types("starter"):
    print(a)
