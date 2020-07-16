from room import Room
from player import Player
from item import Item, LightSource

# Create some items

item = {
    'sword': Item("Sword", "A simple iron sword"),
    'rusty-sword': Item("Sword", "A rusty sword.", "Rusty"),
    'potion': Item("Potion", "A vial of strange liquid"),
    'lamp': LightSource("Lamp", "A portable lamp")
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [item['rusty-sword']]),

    'foyer':    Room("Foyer","""Dim light filters in from the south. Dusty
passages run north and east.""", [item['potion']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [item['sword']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [item['lamp']], False),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player1 = Player('Gary', room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
def room_is_light():
    if player1.location.is_light:
        return True
    else:
        for item in player1.inventory:
            if isinstance(item, LightSource):
                return True
        for item in player1.location.items:
            if isinstance(item, LightSource):
                return True
        return False

selection = ""
while selection != "q":
    print("\n")
    if room_is_light():
        print(player1.location.name)
        print(player1.location.description)
    else:
        print("It's pitch black!")

    selection = input('''\n[n] North [e] East [s] South [w] West
[get ITEM_NAME] Pickup Item [drop ITEM_NAME] Drop Item
[i/inventory] View Inventory [l/look] Search Room [q] Quit\n''')

    terms = selection.split(" ");

    if terms[0] == "q":
        print("See you later!")
    # movement
    elif terms[0] in 'nesw':
        player1.move(terms[0])
    # actions
    elif terms[0] == 'inventory' or terms[0] == 'i':
        print(f'You are carrying {[f"{item.adj} {item.name}" for item in player1.inventory]}')
    elif terms[0] == 'look' or terms[0] == 'l':
        if len(player1.location.items):
            print(f"Here you see a {player1.location.items[0].name}.")
        else:
            print("You don't find anything.")
    elif terms[0] == 'get' or terms[0] == 'take':
        if not room_is_light():
            print("Good luck finding that in the dark!")
        else:
            player1.get(terms)
    elif terms[0] == 'drop':
        player1.drop(terms)
    else:
        print("Please make a valid selection.")
