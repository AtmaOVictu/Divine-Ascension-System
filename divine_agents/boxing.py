class Bit:
    """Represents a binary value."""

    def __init__(self, value: int):
        if value not in (0, 1):
            raise ValueError("Bit value must be 0 or 1.")
        self.value = value


class BoxingStation:
    """Create new boxes when entities interact."""

    def __init__(self):
        self.boxes = []

    def create_box(self, name: str) -> None:
        self.boxes.append(name)

    def interaction(self, entity1, entity2) -> str:
        """Handle interaction and return the created box name."""
        box_name = ""
        if hasattr(entity1, "state") and hasattr(entity2, "state"):
            if entity1.state == "Ego" and entity2.state == "Jaz":
                box_name = "Self-Other Reflection Box"
            elif entity1.state == "Jaz" and entity2.state == "Enotnost":
                box_name = "Unity Reflection Box"
        elif isinstance(entity1, Bit) and isinstance(entity2, Bit):
            if entity1.value == 0 and entity2.value == 1:
                box_name = "Bit Interaction Box"
        if box_name:
            self.create_box(box_name)
        return box_name
