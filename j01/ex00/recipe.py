class Recipe:
    def __init__(self, p_name : str = "", p_cooking_lvl : int = 0, p_cooking_time : int = 0, p_ingredients : list = [], p_description : str = "", p_recipe_type : str = ""):
        
        assert p_name != ""
        assert 1 <= p_cooking_lvl <= 5
        assert p_cooking_time >= 0
        assert p_ingredients != []
        assert p_recipe_type.find("starter") == 0 or p_recipe_type.find("lunch") == 0 or p_recipe_type.find("dessert") == 0
        self.name = p_name
        self.cooking_lvl = p_cooking_lvl
        self.cooking_time = p_cooking_time
        self.ingredients = p_ingredients
        if p_description != "":
            self.description = p_description
        self.recipe_type = p_recipe_type

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = ""
        txt = txt + f"\tHow to cook a {self.name} :\n\n"
        txt = txt + f"Cooking level : {self.cooking_lvl}\nCooking time : {self.cooking_time} min\n"
        txt = txt + "Ingredients :\n"
        for ing in self.ingredients:
            txt = txt + f"\t- {ing}\n"
        txt = txt + f"({self.recipe_type})"
        return txt



