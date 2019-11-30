import rooms
from tile import DoorTile

rl = [rooms.ElevatorRoom(), rooms.SmallRoom(), rooms.MediumRoom(), rooms.LargeRoom()]


def door_counter(room):
    counter = 0
    if isinstance(room, rooms.Room):
        for section in room: # this might be a function....but I think that would be too much.
            for tile in section:
                if tile == "DR":
                    counter = counter + 1
    return counter

    

def tramp(room_list): # rename this to something useful
    coord_list = []
    for room_index, room in enumerate(room_list):
        num = door_counter(room)
        if num > 1:
            coord_list.append(multiDoorTile_assigner(room_index, room))
        else:
            coord_list.append(singleDoorTile_assigner(room_index, room))
        
    print(coord_list)

def singleDoorTile_assigner(room_index, room):
    for y_index, section in enumerate(room):
        for x_index, tile in enumerate(section):
            if tile != "DR":
                continue
            else:
                door = (room_index, y_index, x_index)
                room[y_index][x_index] = DoorTile(room_index, y_index, x_index)
                
               
    return door 



def multiDoorTile_assigner(room_index, room):
    room_doors = []
    for y_index, section in enumerate(room):
        for x_index, tile in enumerate(section):
            if tile == 'DR':
                door = (room_index, y_index, x_index)
                room[y_index][x_index] = DoorTile(room_index, y_index, x_index)
                room_doors.append(door)
    return room_doors
                


tramp(rl)
for i in coord_list:
    if type(i) == list:
        print('look ma no hands')
    
    elif type(i) == tuple:
        print("tups!!!")
        
    else:
        print("Temae!!!")
        