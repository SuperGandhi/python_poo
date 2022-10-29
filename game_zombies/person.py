# class person

class Person:
    # initializador method
    # self -> convention
    def __init__(self, name_person):
        self.name = name_person
        self.address = 1
    
    # métodos 
    def moving(self, velocity):
        if velocity == "1":
            self.address += 1
        elif velocity == "2":
            self.address += 2
        else:
            self.address += 3

jose = Person("Jose")


print(jose.address)
jose.moving("2")
print(jose.address)
jose.moving("3")
print(jose.address)

