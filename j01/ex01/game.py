class GotCharacter:
    def __init__(self, first_name, is_alive = True):
        self.first_name = first_name
        self.is_alive = is_alive

class Lannister(GotCharacter):
    """A class representing the Lannister family aka the most badass people of the Seven Kingdom"""
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Lannister"
        self.house_words = "A Lannister always pay his debts"

    def print_house_words(self):
        print(f"{self.house_words}")
    
    def die(self):
        self.is_alive = False

class Incestproduct(Lannister):
    """A class representing the children of Cersei and Jamie, the incest products"""
    def __init__(self, first_name, is_alive = True, hair_color = None):
        super().__init__(first_name=first_name, is_alive=is_alive)   #= def__init__ de classe parent donc family +hw sont definis par dflt dedans oklm
        self.hair_color = hair_color

# joffrey = Incestproduct("Joffrey", True, "blond")
# cersei = Lannister("Cersei")
# print(cersei.print_house_words())
# print(joffrey.print_house_words())
# print(joffrey.hair_color)
