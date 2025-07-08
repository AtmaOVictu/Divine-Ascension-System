class BoxingStation:
    """Manage creation of boxes when entities interact."""

    def __init__(self):
        self.boxes = []  # type: list[str]

    def create_box(self, box_name: str) -> None:
        """Store a new interaction box."""
        self.boxes.append(box_name)

    def interaction(self, entity1, entity2) -> None:
        """Create boxes based on interaction between two entities."""
        from .agent import Agent
        if isinstance(entity1, Agent) and isinstance(entity2, Agent):
            if entity1.state == "Ego" and entity2.state == "Jaz":
                self.create_box("Self-Other Reflection Box")
            elif entity1.state == "Jaz" and entity2.state == "Enotnost":
                self.create_box("Unity Reflection Box")
        elif isinstance(entity1, Bit) and isinstance(entity2, Bit):
            if entity1.value == 0 and entity2.value == 1:
                self.create_box("Bit Interaction Box")


class Bit:
    """Simple binary unit for data-driven interactions."""

    def __init__(self, value: int):
        self.value = value
