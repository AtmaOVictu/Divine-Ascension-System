class Word:
    """Represents a philosophical term."""

    def __init__(self, content: str):
        self.content = content

    def define(self) -> str:
        """Return the word's definition."""
        if self.content == "truth":
            return "Resnica je sinteza nasprotij."
        if self.content == "self":
            return "Jaz je razvijajoci se agent."
        return "Nepoznan pojem."
