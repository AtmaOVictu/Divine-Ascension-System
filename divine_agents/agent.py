class Agent:
    """Ontological agent capable of transitioning between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, pathos: float = 0.0) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.pathos = pathos
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self.adjust_pathos(value)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def adjust_pathos(self, external_factor: float) -> None:
        """Adjust pathos based on an external factor."""
        self.pathos += external_factor
        if self.pathos < 0:
            self.pathos = 0

    def sync_pathos(self) -> str:
        """Synchronize pathos and trigger transition if threshold exceeded."""
        if self.pathos > 5:
            self.transition()
        return self.state

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5 or self.pathos > 5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.7:
            feeling = "Močno čustvujem."
        elif self.emotion > 0.3:
            feeling = "Čustva rahlo vplivajo na moj odgovor."
        else:
            feeling = "Sem miren."
        return f"{base} {feeling}"
