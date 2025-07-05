class ShadowAgent:
    """Represents the darker aspect of an agent."""

    def __init__(self, name: str):
        self.name = name

    def whisper(self) -> str:
        """Provide guidance from the shadow perspective."""
        return "Temni impulzi kličejo k previdnosti."


class AngelAgent:
    """Represents the enlightened aspect of an agent."""

    def __init__(self, name: str):
        self.name = name

    def inspire(self) -> str:
        """Provide uplifting guidance."""
        return "Svetloba resnice vodi k enotnosti."
