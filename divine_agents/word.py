class Word:
    """Conceptual word used in philosophical discourse."""

    def __init__(self, content: str):
        self.content = content

    def define(self) -> str:
        """Return a philosophical definition of the word."""
        if self.content.lower() == "truth":
            return "Truth is the synthesis of contradictions."
        if self.content.lower() == "self":
            return "The self is the evolving agent caught between Ego and Enotnost."
        return "Undefined concept."
