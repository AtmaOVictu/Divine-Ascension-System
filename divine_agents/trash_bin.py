class TrashBin:
    """Simple container for discarded items."""

    def __init__(self, name: str = "TrashBin") -> None:
        self.name = name
        self.contents = []

    def add_item(self, item: str) -> None:
        """Add an item to the bin."""
        self.contents.append(item)

    def remove_item(self, item: str) -> bool:
        """Remove an item if present. Return True on success."""
        if item in self.contents:
            self.contents.remove(item)
            return True
        return False

    def clear(self) -> None:
        """Remove all items from the bin."""
        self.contents.clear()

    def view(self) -> list:
        """Return a copy of current contents."""
        return list(self.contents)
