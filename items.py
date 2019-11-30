
class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")
    
    def __str__(self):
        return self.name

class Rock(Weapon):
    def __init__(self):
        self.name = 'Rock'
        self.description = 'A fist-sized rock.'
        self.damage = 5
        
class Dagger(Weapon):
    def __init__(self):
        self.name = 'Dagger'
        self.description = 'A small dagger with some rust.'
        self.damage = 10
        
class RustySword(Weapon):
    def __init__(self):
        self.name = "Rusty Sword"
        self.description = 'A sword that\'s showing it\'s age'
        self.damage = 20


        
