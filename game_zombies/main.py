# flow program
from person import Person
from zombie import Zombie 
import os

os.system('cls')
print()
print(' The city crowded zombies')
print(' You are on 1th street can arrive')
print(' On the 40th street you can save yourself')
print(' The zombies advance 1, 2 or 3 streets ')
print(' You can move along 1,2 or 3 streets ')
print()

name = input(' ¿You are ready? What is your name: ').capitalize()


player = Person(name)

horda = []

for i in range(50):
    z=Zombie()
    horda.append(z)
    
while True:
    os.system('cls')
    
    
    print(player.situation())
    # print ('{}, you are in the street{}'.format(player.name,player.street))
    
    streets = []
    for zombie in horda:
        streets.append(zombie.street)
    streets.sort()
    print('There are zombies in the streets: ')
    for element in streets:
        print(element, end=' ')
    print()
    print()
    
    if player.street > 40:
        print(' Dont see any zombie')
        print(' You have luck')
        print()
        break
    
    ate = False
    
    for zombie in horda:
        if zombie.street == player.street:
            ate = True
    if ate:
        print(' A zombie see you')
        print(' He eat you . Game over')
        print()
        break

    velocity = ""
    while velocity not in ('1','2','3'):
        velocity = input(' You want runnig (1/2/3): ')
    player.moving(velocity)


    for z in horda:
        z.moving()