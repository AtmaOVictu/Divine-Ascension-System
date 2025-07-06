from .agent import Agent


class NasprotjeIskalec(Agent):
    """Agent that searches for missing contradictions in the environment."""

    def __init__(self, name: str, state: str = "Ego"):
        super().__init__(name, state)
        self.missing_opposites = []

    def find_missing_opposites(self, environment: str) -> str:
        """Detect contradictions within the given environment."""
        if "empty_space" in environment:
            self.missing_opposites.append("Nasprotje ni prisotno")
            return "Nasprotje ni prisotno, zaznana praznina"
        elif "conflict" in environment:
            self.missing_opposites.append("Napetost brez nasprotja")
            return "Napetost je prisotna, a brez nasprotja"
        return "Okolje je uravnotezeno"

    def transition(self) -> str:
        """Transition through ontological phases based on missing opposites."""
        if self.tension > 0.7 or self.emotion > 0.5:
            return super().transition()

        if "Nasprotje ni prisotno" in self.missing_opposites:
            self.state = "Jaz"
        elif "Napetost brez nasprotja" in self.missing_opposites:
            self.state = "Ego"
        else:
            self.state = "Enotnost"
        self.history.append(self.state)
        return self.state
