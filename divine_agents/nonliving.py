class NonLivingEntity:
    """Represents a non-living entity that is conceptually in the Jaz state."""

    def __init__(self, name: str, identity: str, state: str = "Jaz"):
        self.name = name
        self.identity = identity
        self.state = state

    def describe(self) -> str:
        """Return a textual description of the entity."""
        return f"{self.name} ({self.identity}) - state: {self.state}"

    @staticmethod
    def list_entities(entities: list) -> list:
        """Enumerate a list of entities by returning their descriptions."""
        return [entity.describe() for entity in entities]
