from .agent import Agent

class NasprotjeIskalec(Agent):
    """Agent that detects missing opposites and transitions accordingly."""

    def __init__(self, name: str, state: str = "Ego"):
        super().__init__(name, state)
        self.missing_opposites = []

    def find_missing_opposites(self, environment: str) -> str:
        """Look for contradiction gaps in the environment."""
        if "empty_space" in environment:
            self.missing_opposites.append("Nasprotje ni prisotno")
            return "Nasprotje ni prisotno, zaznana praznina"
        if "conflict" in environment:
            self.missing_opposites.append("Napetost brez nasprotja")
            return "Napetost je prisotna, a brez nasprotja"
        return "Okolje je uravnotezeno"

    def transition(self) -> str:
        """Override to incorporate missing opposites in the decision."""
        super().transition()
        if "Nasprotje ni prisotno" in self.missing_opposites:
            self.state = "Jaz"
        elif "Napetost brez nasprotja" in self.missing_opposites:
            self.state = "Ego"
        else:
            if self.state == "Jaz" and (self.tension > 0.7 or self.emotion > 0.5):
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        if self.state == "Ego":
            return f"{self.name}: Resnica je absolutna, brez nasprotij."
        if self.state == "Jaz":
            return f"{self.name}: Resnica je relativna, nasprotja so prisotna."
        return f"{self.name}: Vse resnice so zdruzene, ni vec nasprotij."

