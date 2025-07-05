class ShadowAgent:
    """Represents the darker aspect of an agent."""

    def __init__(self, name: str):
        self.name = name

    def advise(self) -> str:
        return "Poglej v svojo senco in spoznaj svoje strahove."


class AngelAgent:
    """Represents the enlightened aspect of an agent."""

    def __init__(self, name: str):
        self.name = name

    def advise(self) -> str:
        return "Verjemi v visje nacelo in poisci enotnost."
