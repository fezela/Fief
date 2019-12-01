import random
import rooms
from tile import DoorTile




class Floor(list):
    rooms_list = [
        rooms.SmallRoom, rooms.MediumRoom, rooms.LargeRoom, 
    ]
    def __init__(self):
        super().__init__()
        self.append(rooms.ElevatorRoom())
        self.door_coords = []
        #tramp(self)    

    def build_floor(self):


        def door_counter(room):
            counter = 0
            if isinstance(room, rooms.Room):
                for section in room: # this might be a function....but I think that would be too much.
                    for tile in section:
                        if tile == "DR":
                            counter = counter + 1
            return counter

    

        def tramp(room_list): # rename this to something useful
            for room_index, room in enumerate(room_list):
                num = door_counter(room)
                if num > 1:
                    self.door_coords.append(multiDoorTile_assigner(room_index, room))
                else:
                    self.door_coords.append(singleDoorTile_assigner(room_index, room))
        
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
                


x = Floor()

for index, room in enumerate(x):
    print("Room: ", index + 1)
    print("\n")
    print(room.__str__())

        