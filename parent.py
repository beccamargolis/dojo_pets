class Pet:
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 50
        self.noise = noise

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        self.energy -= 10
        if self.energy <= 15:
            print(f"{self.name} is very tired! Energy level is {self.energy}")
        elif self.energy <= 25:
            print(f"{self.name} would like to sit down for a little bit.")
        else:
            print(f"{self.name} has plenty of energy left!")
        return self

    def noise(self):
        print(self.noise)

class LazyPet(Pet):
    def __init__(self, name, type, tricks, noise, bed):
        super().__init__(name, type, tricks, noise)
        self.bed = bed

    def play(self):
        self.health += 5
        self.energy -= 20
        print(f"{self.name} isn't a big fan of playing...")
        super().play()
        return self

    def sleep(self):
        print(f"{self.name} loves to sleep in {self.bed}!")
        super().sleep()
        return self