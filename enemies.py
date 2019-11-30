class Enemy:
    def __init__(self):
        raise NotImplementedError("Do not create raw enemy objects.")
        
    def __str__(self):
        return self.name
    
    def is_alive(self):
        return self.hp > 0
    
    def attack(self, target):
        target.hp = target.hp - self.damage
        print("{} attacks for {} damage".format(
            self.name, self.damage))

class GiantSpider(Enemy):
    def __init__(self):
        self.name = "Giant Spider"
        self.hp = 34
        self.damage = 11
        
    
        
class Scorpion(Enemy):
    def __init__(self):
        self.name = "Scorpion"
        self.hp = 30
        self.damage = 10
        self.special_attack = "Sting"
        self.special_damage = 30
        
    def attack(self, target):
        if self.hp > self.hp // 2:
            target.hp = target.hp - self.damage
            print("{} attacks for {} damage!".format(self.name,
                self.damage))
            
        else:
            print("Scorpion shakes tail!")
            target.hp = target.hp - self.special_damage
            print("{} uses {}!".format(self.name,
                self.special_attack))
            self.hp = self.hp - self.special_damage
            
        
class LocustSwarm(Enemy):
    def __init__(self):
        self.name = "Locust Swarm"
        self.hp = 100
        self.damage = 4
        
class Ifrit(Enemy):
    def __init__(self):
        self.name = "Ifrit"
        self.hp = 85
        self.damage = 15
        self.special_attack = "Wall of Fire"
        self.special_damage = 25
        
    def attack(self, target):
        if self.hp < 30:
            target.hp = target.hp - self.special_damage
            self.hp = self.hp + self.damage
            print("{} uses {}!".format(
                self.name, self.special_attack))
            print("The {} heals itself for {} HP!".format(
                self.name, self.damage))
            print("{} attacks for {} damage!".format(
                self.name, self.special_damage))
            
        else:
            target.hp = target.hp - self.damage
            print("{} attacks for {} damage!".format(
                self.name, self.damage))
            
                            