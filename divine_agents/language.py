class Language:
    """Generate responses based on an agent's ontological state."""

    def generate(self, state: str) -> str:
        """Return a philosophical statement for the given state."""
        if state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
