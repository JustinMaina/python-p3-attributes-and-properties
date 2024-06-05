#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:

    def __init__(self, name="", breed=""):
        self._name = None
        self._breed = None
        self.name = name  # This will trigger the name setter
        self.breed = breed  # This will trigger the breed setter
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value in APPROVED_BREEDS:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")


# Example usage:
d1 = Dog("Buddy")
print(d1.name)  # Output: Buddy

d2 = Dog("a very long name that exceeds twenty five characters")
# Output: Name must be string between 1 and 25 characters.
print(d2.name)  # Output: None

d3 = Dog(123)
# Output: Name must be string between 1 and 25 characters.
print(d3.name)  # Output: None