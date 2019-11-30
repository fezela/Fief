import random
import enemies

class MapTile:
    def __init__(self, y, x):
        self.y = y
        self.x = x
        
        
    def intro_text(self):
        raise NotImplementedError("Create a subclass instead")


class DoorTile(MapTile):
    def __init__(self, room_index, y, x):
        self.has_player = False
        self.exit_location = ' '
        self.room_index = room_index
        super().__init__(y, x)
        
    def move_player(self, player, location):
        pass
        #set player.location to self.exit_location
        #set self.has_player to False

    def intro_text(self):
        pass

class FloorTile(MapTile):
    def __init__(self, y, x):
        self.has_monster = False
        r0 = random.random()
        if r0 > 0.70:
            self.has_monster = True
            r1 = random.random()
            if r1 < 0.50:
                self.enemy = enemies.GiantSpider()
            
            elif r1 < 0.80:
                self.enemy = enemies.Scorpion()
            
            elif r1 < 0.95:
                self.enemy = enemies.LocustSwarm()
            
            else:
                self.enemy = enemies.Ifrit()
        super().__init__(y, x)
        
    
    def intro_text(self):
        if self.has_monster:
            return "a {} awaits!".format(self.enemy.name)
        
        else:
            return """
        You're on the right path.  It's just every
        step is dark and foreboding.
        """


class EnemyTile(MapTile):
    def __init__(self, x, y):
        r = random.random()
        
        if r < 0.50:
            self.enemy = enemies.GiantSpider()
            
        elif r < 0.80:
            self.enemy = enemies.Scorpion()
            
        elif r < 0.95:
            self.enemy = enemies.LocustSwarm()
            
        else:
            self.enemy = enemies.Ifrit()
            
        super().__init__(x, y)
        
    def intro_text(self):
        if self.enemy.is_alive() and self.enemy.name == "Ifrit":
            return "You've awoken an {}!".format(self.enemy.name)
        
        elif self.enemy.is_alive():
            return "A {} awaits!".format(self.enemy.name)
        
        else:
            return "You've defeated the {}!".format(self.enemy.name)
        

        
        
class BossTile(MapTile):
    def intro_text(self):
        return """
        There is a boss of the cave.
        """

class VictoryTile(MapTile):
    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!
        
        
        Victory is yours!
        """

"""I'm wondering if the below should be a method of the base class.  It
could be used to determine whether the player is @ the same location as the tile.
It could return true or false in order to trigger events.  I think for the code of
the original game it was used to determine index errors. There are some issues with this
concept though.  When would this code execute?  If it executes after every update there
will invariable be times when the players index will be the same, if there are multiple rooms.
It may need another variable to determine it's room location/index. Remember
EVERY ROOM has tiles, so you need to figure out a way to determine the tiles specific room
location."""

def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    
    try:
        return world_map[y][x]
    
    except IndexError:
        return None
             