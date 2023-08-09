import time
from random import randint
import os


class log:
    import sys
    import timeit
    def __init__(self, start_machine, boil_water=None, make_coffee=None, add_water=None):
        self.start_machine = start_machine
        self.boil_water = boil_water
        self.make_coffee = make_coffee
        self.add_water = add_water
    
    def __call__(self, *args):
        fd = open("machine.txt", "w")
        fd.write("this is test")
        if args:
            return self.start_machine(self, *args)
        else:
            return self.sta(self)


class CoffeeMachine():
    water_level = 100
    
    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."
    
    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")

if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)