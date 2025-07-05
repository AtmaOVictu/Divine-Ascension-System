class Philosopher:
    """Provide philosophical responses based on ontological state."""

    def __init__(self, state: str = "Ego") -> None:
        self.state = state

    def respond(self, question: str) -> str:  # pylint: disable=unused-argument
        """Return a philosophical answer based on current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
