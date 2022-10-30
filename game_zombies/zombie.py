# class zombie
import random
class Zombie:
    
    def __init__(self):
        self.street = random.randint(10,20)
        self.direction = random.choice(['left', 'right'])
        self.velocity = random.randint(1,3)
        
    def moving(self):
        if self.direction == 'left':
            self.street -= self.velocity
        else:
            self.street += self.velocity
            
    def not_visible(self):
        if self.street < 0 or self.street > 40:
            return True
        else:
            return False

z= Zombie()


for i in range(5):
    print(z.street)
    z.moving()