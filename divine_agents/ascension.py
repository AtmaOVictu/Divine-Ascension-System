class BodyAgent:
    """Agent managing transitions through bodily states."""
    def __init__(self):
        self.state = "Material"

    def transition(self, symbol: str) -> str:
        """Move through body phases based on symbol."""
        if symbol == "Material":
            self.state = "Material"
        elif symbol == "Sensation":
            self.state = "Sensation"
        elif symbol == "Action":
            self.state = "Action"
        elif symbol in {"ADD", "DODAJ"}:
            self.state = "Expansion"
        return self.state

    def get_state(self) -> str:
        return self.state


class SoulAgent:
    """Agent managing transitions through soul states."""
    def __init__(self):
        self.state = "Awareness"

    def transition(self, symbol: str) -> str:
        if symbol == "Awareness":
            self.state = "Awareness"
        elif symbol == "Emotion":
            self.state = "Emotion"
        elif symbol == "Reflection":
            self.state = "Reflection"
        elif symbol == "Growth":
            self.state = "Growth"
        elif symbol in {"ADD", "DODAJ"}:
            self.state = "Enlightenment"
        return self.state

    def get_state(self) -> str:
        return self.state


class SpiritAgent:
    """Agent managing transitions through spirit states."""
    def __init__(self):
        self.state = "Divine"

    def transition(self, symbol: str) -> str:
        if symbol == "Divine":
            self.state = "Divine"
        elif symbol == "Unity":
            self.state = "Unity"
        elif symbol == "Eternal":
            self.state = "Eternal"
        elif symbol == "Enlightenment":
            self.state = "Enlightenment"
        elif symbol in {"ADD", "DODAJ"}:
            self.state = "Transcendence"
        return self.state

    def get_state(self) -> str:
        return self.state

