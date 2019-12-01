import random
from rooms import ElevatorRoom, SmallRoom


x = ElevatorRoom()
y = SmallRoom()
print(x.door_coords)
for i in x.door_coords:
    print(i[0])
    
print(y.door_coords)
for i in y.door_coords:
    print(i[0])