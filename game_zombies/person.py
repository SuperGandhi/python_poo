# class person

class Person:
    # initializador method
    # self -> convention
    def __init__(self, name_person):
        self.name = name_person
        self.address = 1
    
    
    def situation(self):
        return '{}, you are in the street{}'.format(self.name,self.street)
    
    # methods
    def moving(self, velocity):
        if velocity == '1':
            self.address += 1
        elif velocity == '2':
            self.address += 2
        else:
            self.address += 3

