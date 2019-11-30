from tile import FloorTile



class Room(list):
    def __init__(self, door_coords, wall_coords, 
    y_dim, x_dim, name='Room'):
        self.name = name
        if self.name == "Room":
            raise NotImplementedError(
        '''
        Create a subclass or set key 'name' to something other than "Room"
        ''')
        
        else:
            super().__init__()
            self.door_coords = door_coords
            self.wall_coords = wall_coords
            self.y_dim = y_dim
            self.x_dim = x_dim
            self.name = name
            self.build_room()


        

    def __str__(self):
        room_presentation = ""
        for section in self:
            for item in section:
                if isinstance(item, FloorTile):
                    room_presentation = room_presentation + "|FT"
                elif item == None:
                    room_presentation = room_presentation + "|  "
                elif item == "DR":
                    room_presentation = room_presentation + "|DR"
                else:
                    room_presentation = room_presentation + "|??"
            room_presentation = room_presentation + "|\n"

        return room_presentation

        
    def room_map(self):
        room = "Room name: {}".format(self.name)
        room = room + "\n\n"
        for section in self:
            for tile in section:
                if isinstance(tile, FloorTIle):
                    if tile.has_monster:
                        room = room + "|MT"
                    else:
                        room = room + "|FT"

                elif tile == None:
                    room = room + "|  "
                                
                else:
                    room = room + "|??"
            room = room + "|\n"
        return room
    
    
    def add_attribute(self, attribute, value):
        for i, j in enumerate(self):
            for a in attribute:
                for k in range(0, len(j)):
                    if i == a[0] and k == a[1]:
                        self[i][k] = value

    
    
    def build_room(self):        
        '''Crafts custom rooms.'''        
        def lay_foundation():
            for i, j in enumerate(range(0, self.y_dim)):
                i = []
                self.append(i)
                for k in range(0, self.x_dim):
                    i.append(FloorTile(j, k))

        
        lay_foundation()
        self.add_attribute(self.wall_coords, None)
        self.add_attribute(self.door_coords, "DR")
        
class ElevatorRoom(Room):
    walls = (
        (0,0), (0,1), (0,4), (0,7), (0,8),
        (1,0), (1,8), (3,0), (3,8), (4,0),
        (4,8), (5,0), (5,1), (5,2), (5,6),
        (5,7), (5,8), (6,0), (6,1), (6,2),
        (6,6), (6,7), (6,8), (7,0), (7,1),
        (7,7), (7,8), (8,0), (8,1), (8,2),
        (8,6), (8,7), (8,8), (9,0), (9,1),
        (9,2), (9,6), (9,7), (9,8), (10,0),
        (10,1), (10,2), (10,6), (10,7), (10,8),
        (11,0), (11,1), (11,2), (11,3), (11,5),
        (11,6), (11,7), (11,8),
    )

    doors = (
        (2,0), (2,8), (7,2), (7,6),
    )

    y = 12
    
    x = 9 
    def __init__(self, door_coords=doors, wall_coords=walls, y_dim=y, x_dim=x, name="Elevator Room"):
        super().__init__(door_coords, wall_coords, y_dim, x_dim, name)

class SmallRoom(Room):
    walls = (
        (0,4), (2,4)
    )
    
    doors = (
        (1,4),
    )

    y = 3
    
    x = 5
    def __init__(self, door_coords=doors, wall_coords=walls, y_dim=y, x_dim=x, name="Small Room"):
        super().__init__(door_coords, wall_coords, y_dim, x_dim, name)


class MediumRoom(Room):
    walls = (
        (0,8), (1,8), (2,8), (4,8), (5,8),
        (6,8),
    )

    doors = (
        (3,8),
    )
    
    y = 7

    x = 9
    def __init__(self, door_coords=doors, wall_coords=walls, y_dim=y, x_dim=x, name="Medium Room"):
        super().__init__(door_coords, wall_coords, y_dim, x_dim, name)

class LargeRoom(Room):
    """You need to create door and wall coords for this object"""
    walls = (
        (16,0), (16,1), (16,2), (16,3), (16,4), 
        (16,5), (16,6), (16,8), (16,9), (16,10),
        (16,11), (16,12), (16,13), (16,14), 
    )

    doors = (
        (16,7),
    )

    y = 17

    x = 15
    def __init__(self, door_coords=doors, wall_coords=walls, y_dim=y, x_dim=x, name="Large Room"):
        super().__init__(door_coords, wall_coords, y_dim, x_dim, name)                    


