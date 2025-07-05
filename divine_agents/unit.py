class OntologicalUnit:
    """Represents a dynamic ontological unit."""

    def __init__(self, name: str, type: str, meaning: str) -> None:
        self.name = name
        self.type = type
        self.meaning = meaning

    def activate(self) -> None:
        """Activate the unit and print its meaning."""
        print(f"Enota '{self.name}' aktivirana. Pomen: {self.meaning}")

    def transition(self, new_meaning: str) -> None:
        """Transition to a new meaning."""
        print(
            f"Enota '{self.name}' prehaja iz '{self.meaning}' v '{new_meaning}'"
        )
        self.meaning = new_meaning

    def display(self) -> None:
        """Display the current state of the unit."""
        print(f"Enota: {self.name}, Tip: {self.type}, Pomen: {self.meaning}")
