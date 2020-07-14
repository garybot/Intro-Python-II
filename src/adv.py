from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

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
options = ['n', 'e', 's', 'w', 'q', ]
selection = ""
while selection != "q":
    print("\n")
    print(player1.location.name)
    print(player1.location.description)

    selection = input('[n] North [e] East [s] South [w] West [get ITEM_NAME] Pickup Item [drop ITEM_NAME] Drop Item [q] Quit\n')

    if selection not in "neswq":
        print("Please make a valid selection.")
    elif selection == "q":
        print("See you later!")
    elif selection == "n" and hasattr(player1.location, 'n_to'):
        player1.location = player1.location.n_to
    elif selection == "e" and hasattr(player1.location, 'e_to'):
        player1.location = player1.location.e_to
    elif selection == "s" and hasattr(player1.location, 's_to'):
        player1.location = player1.location.s_to
    elif selection == "w" and hasattr(player1.location, 'w_to'):
        player1.location = player1.location.w_to
    else:
        print("That movement is not allowed.")
