class Item:
    """A base class for Items"""
    def __init__(self, name, description, adj = "Basic"):
        self.name = name
        self.description = description
        self.adj = adj

    def __str__(self):
        return f"{self.adj} {self.name}: {self.description}"

    def on_take(self, player):
        '''Is invoked when a player picks up this item.'''
        print(f'You pick up the {self.adj} {self.name}')

    def on_drop(self, player):
        '''Is invoked when a player drops this item.'''
        print(f'You drop the {self.adj} {self.name}')

class LightSource(Item):
    """docstring for LightSource."""

    def __init__(self, name, description):
        super().__init__(name, description)

    def on_drop(self, player):
        '''Is invoked when a player drops this item.'''
        print(f"It's not wise to drop your source of light!")
