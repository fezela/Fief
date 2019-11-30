import random
import enemies

class MapTile:
    def __init__(self, y, x):
        self.y = y
        self.x = x
        
        
    def intro_text(self):
        raise NotImplementedError("Create a subclass instead")
    
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

world_map = [
    [FloorTile(0,0), FloorTile(1,0), FloorTile(2,0)],
    [FloorTile(0,1), FloorTile(1, 1), FloorTile(2,1)],
    [FloorTile(0, 2), FloorTile(1, 2), FloorTile(2, 2)],
    [FloorTile(0, 3), FloorTile(1, 3), FloorTile(2, 3)]
    ]

def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    
    try:
        return world_map[y][x]
    
    except IndexError:
        return None
             