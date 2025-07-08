class Subagent:
    """A simple subagent that can interact with statements."""

    def __init__(self, name: str):
        self.name = name

    def interact(self, statement: str) -> str:
        """React to a statement in a minimal way."""
        return f"{self.name} hears '{statement}' and contemplates." 
