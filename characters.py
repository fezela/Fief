
class Character:
    def __init__(self):
        self.lvl = 1
        self.hp = 1
        self.inventory = []

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0

    def attack(self, target):
        target.hp = target.hp - self.damage
        print("{} attacks for {} damage".format(
            self.name, self.damage))

class Player(Character):
    def __init__(self):
        
        self.hp = 110
            