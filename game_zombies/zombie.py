# class zombie
import random
class Zombie:
    
    def __init__(self):
        self.street = random.randint(10,20)
        self.direction = random.choice(['left', 'right'])
        
    def moving(self):
        if self.direction == 'left':
            self.street -= random.randint(1,3)
        else:
            self.street += random.randint(1,3)
            
    def not_visible(self):
        if self.street < 0 or self.street > 40:
            return True
        else:
            return False

z= Zombie()
print(z.street)
print(z.direction)
z.moving()
print(z.street)
print(z.not_visible())