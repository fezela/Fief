from player import Player
import world

north = ['n', 'North', 'north', 'N']
south = ['s', 'South', 'south', 'S']
east = ['e', 'East', 'east', 'E']
west = ['w', 'West', 'west', 'W']
attack = ['a', 'Attack', 'attack', 'A']
inv = ['i','Inventory', 'inventory', 'I',
       'inv', 'Inv']

def get_action():
    return input('Action: ')


def play():
    player = Player()
    print('Escape from the Cave of Terror!')
    while True:
        try:
            room = world.tile_at(player.x, player.y)
            print(room.intro_text())
            print("\n")
            print("current location: ", player.x, player.y)
            
        except AttributeError:
            print("This room doesn't exist")
            print("current location: ", player.x, player.y)
        action_input = get_action()
    
        if action_input in north:
            print('Going North')
            player.move_north()
        
        elif action_input in south:
            print('Going South')
            player.move_south()
                
        elif action_input in east:
            print('Going East')
            player.move_east()

        elif action_input in west:
            print('Going West')
            player.move_west()
            
        elif action_input in attack:
            player.attack()
        
        elif action_input in inv:
            print('Inventory:')
            player.print_inventory()
            
        elif action_input == 'exit':
            break
    
        else:
            print('That is not a valid action')
        
        
play()
            
