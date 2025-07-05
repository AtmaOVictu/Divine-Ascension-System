class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, pathos: float = 0.0):
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

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def update_pathos(self, value: float) -> None:
        """Update pathos intensity."""
        self.pathos = value

    def is_legitimate_transition(self) -> bool:
        """Determine if conditions permit a legitimate state change."""
        if self.state == "Ego" and (self.tension > 0.7 or self.emotion > 0.5):
            return True
        if self.state == "Jaz" and (self.tension > 0.7 or self.emotion > 0.5):
            return True
        if self.state == "Enotnost" and self.pathos > 5:
            return True
        return False

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.is_legitimate_transition():
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        elif self.tension > 0.7 or self.emotion > 0.5:
            # Amateur transition triggered by high emotion or tension
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
            mood = " Močno čustvujem."
        elif self.emotion > 0.3:
            mood = " Čustva rahlo vplivajo na moj odgovor."
        else:
            mood = " Sem miren."
        return base + mood
