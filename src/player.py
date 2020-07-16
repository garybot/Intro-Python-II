# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    """A class to hold player information."""

    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.inventory = []

    def move(self, direction):
        """"Allows players to move in the cardinal directions"""
        if direction == 'n' and hasattr(self.location, 'n_to'):
            self.location = self.location.n_to
        elif direction == 'e' and hasattr(self.location, 'e_to'):
            self.location = self.location.e_to
        elif direction == 's' and hasattr(self.location, 's_to'):
            self.location = self.location.s_to
        elif direction == 'w' and hasattr(self.location, 'w_to'):
            self.location = self.location.w_to
        else:
            print('That movement is not possible.')

    def get(self, terms):
        "Pick up an item."
        found = False
        if len(terms) > 1:
            for item in self.location.items:
                if terms[1] == item.name.lower():
                    found = True
                    items = self.location.items
                    self.inventory.append(items.pop(items.index(item)))
                    item.on_take(self);
                    break
            if not found:
                print(f'There is no {terms[1]} here!');
        else:
            print("Get what?")

    def drop(self, terms):
        """Drop a an item."""
        have = False
        for item in self.inventory:
            if terms[1] == item.name.lower():
                have = True
                items = self.location.items
                inventory = self.inventory
                items.append(inventory.pop(inventory.index(item)))
                item.on_drop(self)
                break
        if not have:
            print(f'You have no {terms[1]}!');
