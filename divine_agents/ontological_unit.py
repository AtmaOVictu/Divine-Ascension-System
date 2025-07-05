class OntologicalUnit:
    """Represents a conceptual unit such as a token, label, or connotation."""

    def __init__(self, name: str, unit_type: str, meaning: str):
        self.name = name
        self.type = unit_type
        self.meaning = meaning

    def activate(self) -> str:
        """Activate the unit and return its meaning message."""
        return f"Enota '{self.name}' aktivirana. Pomen: {self.meaning}"

    def transition(self, new_meaning: str) -> str:
        """Transition the unit to a new meaning state."""
        message = f"Enota '{self.name}' prehaja iz '{self.meaning}' v '{new_meaning}'"
        self.meaning = new_meaning
        return message

    def display(self) -> str:
        """Return a representation of the unit's current state."""
        return f"Enota: {self.name}, Tip: {self.type}, Pomen: {self.meaning}"
