from parent import Pet, LazyPet

class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        print(f"It's dinner time for {self.pet.name}!")
        return self

    def bathe(self):
        self.pet.noise()
        return self

    def rest(self):
        self.pet.sleep()
        return self

dog_tricks = ["growl", "sit", "shake hands"]
cat_tricks = ["sleep", "claw furniture", "stretch"]

Digby = Pet("Digby", "English Bulldog", "sit", dog_tricks)
Leander = Pet("Leander", "cat", cat_tricks, ["meow", "purr"])
Ollie = LazyPet("Ollie", "Beagle", "shake hands", "bark", "couch")
Michael = Ninja("Michael", "Guy", "bones", "kibble", Digby)
Becca = Ninja("Becca", "Gal", "catnip", "tuna", Leander)
Caroline = Ninja("Caroline", "Gal", "bacon", "Purina", Ollie)

Michael.feed().walk().walk().walk().walk()
Becca.feed()
Caroline.walk().rest()