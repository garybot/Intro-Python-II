class Room:
    """A class to hold room information."""

    def __init__(self, name, description, items = []):
        self.name = name
        self.description = description
        self.items = items
