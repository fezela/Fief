import random
from rooms import ElevatorRoom, SmallRoom, MediumRoom, LargeRoom
from tile import DoorTile
####################
#DUNGEON BUILDER   #
####################

"""
    The whole point of DUNGEON BUILDER is to allow the user
    to easily build dungeons.  The end goal is to be able to
    quickly craft randomized dungons but it would also be cool
    to be able to allow someone to utiles a designated software
    language (DSL) to create their own hand made dungeon.
"""
def dungeon_generator(num_of_flrs): 
    num_of_flrs = num_of_flrs
    floors = {}
    dungeon = {}
    for i in range(num_of_flrs):
        x = 'FL' + str(i + 1)
        y = i
        z = (x, y)
        #assigning the dictionary it's key and value pairs
        floors.__setitem__(x, y)
        '''building the dictionary keys with a default value
            of an empty list'''
        dungeon.setdefault(x, [])
    return dungeon

def dungeon_rm_generator(num_of_rms):
    room_choices = [SmallRoom(), MediumRoom(), LargeRoom(),]
    room_list = [ElevatorRoom()]
    coord_list = []
    num_of_rms = num_of_rms

    while num_of_rms > 0:
        x = random.randint(0, len(room_choices))
        room_list.append(room_choices[x - 1])
        num_of_rms = num_of_rms - 1
    return room_list

def doorTile_assigner(room_list):
    coord_list = []
    for room_index, room in enumerate(room_list):
        coord = []
        coord.append(room_index)
        for y_index, section in enumerate(room):
            for x_index, tile in enumerate(section):
                if tile != "DR":
                    continue
                else:
                    coord.append(y_index)
                    coord.append(x_index)
                    room[room_index][y_index][x_index] = DoorTile(room_index, y_index, x_index)
        coord_list.append(coord)
        del coord
    print(coord_list)




print(dungeon_rm_generator(5))
#print(dungeon_generator(12))