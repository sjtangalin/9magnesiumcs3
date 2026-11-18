
# Parent Class
# Ito yung main class na foundation ng other animal classes.
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(self.name, "makes a sound.")

    def eat(self):
        print(self.name, "eats food.")


# Child Classes
# They inherit from Animal, pero they have their own behaviors.

class Lion(Animal):
    # Method overriding: sariling sound and food ng lion.
    def make_sound(self):
        print(self.name, "roars loudly!")

    def eat(self):
        print(self.name, "eats fresh meat.")


class Elephant(Animal):
    # Same methods, but different behavior naman.
    def make_sound(self):
        print(self.name, "trumpets!")

    def eat(self):
        print(self.name, "eats grass and fruits.")


class Monkey(Animal):
    # Kanya-kanyang behavior bawat animal.
    def make_sound(self):
        print(self.name, "chatters!")

    def eat(self):
        print(self.name, "eats bananas.")


# Creating Objects
# Simba, Dumbo, and George represent each animal.
animals = [
    Lion("Simba"),
    Elephant("Dumbo"),
    Monkey("George")
]


# For Loop
# So that automatic matawag yung methods without repeating code.
for animal in animals:
    animal.make_sound()
    animal.eat()
    print()
