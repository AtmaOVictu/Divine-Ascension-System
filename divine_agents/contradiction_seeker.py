from .agent import Agent


class NasprotjeIskalec(Agent):
    """Agent that searches for missing contradictions in the environment."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        super().__init__(name, state, tension, emotion)
        self.missing_opposites = []

    def find_missing_opposites(self, environment: str) -> str:
        """Detect absence of opposites in the environment and raise emotion."""
        if "empty_space" in environment:
            self.missing_opposites.append("Nasprotje ni prisotno")
            self.update_emotion(0.6)
            return "Nasprotje ni prisotno, zaznana praznina"
        if "conflict" in environment:
            self.missing_opposites.append("Napetost brez nasprotja")
            self.update_emotion(0.6)
            return "Napetost je prisotna, a brez nasprotja"
        return "Okolje je uravnoteženo"
