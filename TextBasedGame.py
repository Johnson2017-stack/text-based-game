# Andy Johnson
def instructions():
    print('Hello Bucky welcome to the Wizard Text Adventure Game')
    print('Collect all 6 items and defeat lord Farquaad to win the game, or get destroyed by Lord Farquaad')
    print('Move commands: north, south, west, east')
    print('to Add a item to inventory: type "grab [item name]" and it will be added')
    print('Enter "exit" to quit')
    print('----------------')

rooms = {
    'East Wing Lounge': {'north': 'Dungeon', 'west': 'Great Hall', 'Item': 'nothing'},
    'Dungeon': {'south': 'East Wing Lounge', 'Item': 'house elf'},
    'Great Hall': {'north': 'Library', 'east': 'East Wing Lounge', 'west': 'West Wing Lounge', 'south': 'Chapel', 'Item': 'gold'},
    'Library': {'south': 'Great Hall', 'east': 'North Chambers Tower', 'Item': 'owl'},
    'North Chambers Tower': {'west': 'Library', 'Item': 'wand'},
    'West Wing Lounge': {'east': 'Great Hall','Item': 'invisibility cloak'},
    'Chapel': {'north': 'Great Hall', 'east': 'South Power Tower', 'Item': 'broom stick'},
    'South Power Tower': {'east': 'Chapel', 'Item': 'lord Farquaad'},  # Villain
}

commands: set[str] = {'north', 'south', 'east', 'west'}
instructions()

def main():
    current_location = 'East Wing Lounge'
    inventory = []

    def show_status():
        print('')
        print(f'You are in the {current_location}')
        print('Inventory:', *inventory, sep='/ ')
        if rooms[current_location]['Item'] in inventory:
            print('This room is empty.')
        else:
            print(f'you see your ' + rooms[current_location] ['Item'])
    while True:
        show_status()
        possible_moves = rooms.get(current_location, {})
        current_item = rooms[current_location]['Item']
        command = input('\nEnter a direction or find the Item: \n').strip().lower()
        if command in commands:
            if command not in rooms[current_location]:
                print('Sorry try a different direction.')
            elif command in possible_moves:
                current_location = possible_moves.get(command, current_location)
                if current_location == 'South Power Tower':
                    if len(inventory) != 6:
                        print('You do not have all the Items to defeat lord Farquaad')
                        print('lord Farquaad sends a death spell. You have died')
                        break
                    else:
                        print('you have your wand and other Items to defeat lord Farquaad,')
                        print('you send a death spell towards lord Farquaad! Congrats you have defeated him')
                        break
        elif command == 'exit':
            print('I hope you enjoyed, Thank you for playing')
            break
        elif command == 'grab {}'.format(current_item):
            if current_item not in inventory:
                print('you grabbed your ' + current_item, 'and put it in your inventory.')
                inventory.append(current_item)
            elif current_item in inventory:
                print('you have that Item already in the inventory.')
            else:
                print('There are no items available here')
        else:
            print('Invalid input')
if __name__ == '__main__':
    main()

