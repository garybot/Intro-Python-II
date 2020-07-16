class Room:
    """A class to hold room information."""

    def __init__(self, name, description, items = [], is_light = True):
        self.name = name
        self.description = description
        self.items = items
        self.is_light = is_light
