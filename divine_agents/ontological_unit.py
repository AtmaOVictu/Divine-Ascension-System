class OntologicalUnit:
    """Represents a symbolic unit that can transition between meanings."""

    def __init__(self, name: str, unit_type: str, meaning: str):
        self.name = name
        self.type = unit_type
        self.meaning = meaning

    def activate(self) -> None:
        """Activate the unit and display its current meaning."""
        print(f"Enota '{self.name}' aktivirana. Pomen: {self.meaning}")

    def transition(self, new_meaning: str) -> None:
        """Transition the unit to a new meaning."""
        print(f"Enota '{self.name}' prehaja iz '{self.meaning}' v '{new_meaning}'")
        self.meaning = new_meaning

    def display(self) -> None:
        """Display the unit's current state."""
        print(f"Enota: {self.name}, Tip: {self.type}, Pomen: {self.meaning}")
