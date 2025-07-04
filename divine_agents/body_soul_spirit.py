"""Agents representing the body, soul, and spirit stages.

Each agent allows transitions through symbolic phases that model an
ontological journey. These classes complement the :class:`Agent`
implementation which handles philosophical states (Ego, Jaz, Enotnost).
"""


class BodyAgent:
    """Agent handling the physical dimension."""

    def __init__(self):
        self.state = "Material"

    def transition(self, symbol: str) -> None:
        """Move the body agent through its phases."""
        if symbol == "Material":
            self.state = "Material"
        elif symbol == "Sensation":
            self.state = "Sensation"
        elif symbol == "Action":
            self.state = "Action"
        else:
            raise ValueError("Unknown body symbol")

    def get_state(self) -> str:
        return self.state


class SoulAgent:
    """Agent handling the internal soul dimension."""

    def __init__(self):
        self.state = "Awareness"

    def transition(self, symbol: str) -> None:
        """Move the soul agent through its phases."""
        if symbol == "Awareness":
            self.state = "Awareness"
        elif symbol == "Emotion":
            self.state = "Emotion"
        elif symbol == "Reflection":
            self.state = "Reflection"
        else:
            raise ValueError("Unknown soul symbol")

    def get_state(self) -> str:
        return self.state


class SpiritAgent:
    """Agent representing the spiritual dimension."""

    def __init__(self):
        self.state = "Divine"

    def transition(self, symbol: str) -> None:
        """Move the spirit agent through its phases."""
        if symbol == "Divine":
            self.state = "Divine"
        elif symbol == "Unity":
            self.state = "Unity"
        elif symbol == "Eternal":
            self.state = "Eternal"
        else:
            raise ValueError("Unknown spirit symbol")

    def get_state(self) -> str:
        return self.state
