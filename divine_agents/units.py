class OntologicalUnit:
    """Represents a basic ontological unit such as a token, label or connotation."""

    def __init__(self, name: str, unit_type: str, meaning: str) -> None:
        self.name = name
        self.unit_type = unit_type
        self.meaning = meaning

    def activate(self) -> str:
        """Activate the unit returning its current meaning."""
        return f"Enota '{self.name}' aktivirana. Pomen: {self.meaning}"

    def transition(self, new_meaning: str) -> str:
        """Transition the unit to a new meaning."""
        old_meaning = self.meaning
        self.meaning = new_meaning
        return f"Enota '{self.name}' prehaja iz '{old_meaning}' v '{new_meaning}'"

    def display(self) -> str:
        """Return a string representation of the unit."""
        return f"Enota: {self.name}, Tip: {self.unit_type}, Pomen: {self.meaning}"
