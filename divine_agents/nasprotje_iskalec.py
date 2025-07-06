"""NasprotjeIskalec agent for detecting missing contradictions."""
from .agent import Agent


class NasprotjeIskalec(Agent):
    """Agent that searches for contradictions and manages ontological transitions."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        super().__init__(name, state, tension, emotion)
        self.missing_opposites = []

    def find_missing_opposites(self, environment: str) -> str:
        """Look for missing contradictions in the environment."""
        if "empty_space" in environment:
            self.missing_opposites.append("Nasprotje ni prisotno")
            return "Nasprotje ni prisotno, zaznana praznina"
        if "conflict" in environment:
            self.missing_opposites.append("Napetost brez nasprotja")
            return "Napetost je prisotna, a brez nasprotja"
        return "Okolje je uravnotezeno"

    def transition(self) -> str:
        """Transition according to tension, emotion or missing opposites."""
        if self.tension > 0.7 or self.emotion > 0.5 or self.missing_opposites:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Philosophical response influenced by current state."""
        if self.state == "Ego":
            return f"{self.name}: Resnica je absolutna, brez nasprotij."
        if self.state == "Jaz":
            return f"{self.name}: Resnica je relativna, nasprotja so prisotna."
        return f"{self.name}: Vse resnice so zdruzene, ni vec nasprotij."
