class Agent:
    """Ontological agent capable of state transitions based on emotion and tension."""

    STATES = ("Ego", "Jaz", "Enotnost", "Invertni Jaz")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self._previous_state = state

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def toggle_invertni_jaz(self) -> str:
        """Toggle the 'Invertni Jaz' state as a reflection of the current state."""
        if self.state != "Invertni Jaz":
            self._previous_state = self.state
            self.state = "Invertni Jaz"
        else:
            self.state = self._previous_state
        self.history.append(self.state)
        return self.state

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer based on state and emotion."""
        prefix = ""
        if self.emotion > 0.6:
            prefix = "Z navdihom: "
        elif self.emotion < -0.6:
            prefix = "S strahom: "

        if self.state == "Ego":
            answer = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            answer = "Resnica je relativna, oblikovana z našimi odnosi."
        elif self.state == "Invertni Jaz":
            answer = "Resnica je moj odsev v nasprotju."
        else:
            answer = "Vse resnice so eno, medsebojno povezane."
        return f"{prefix}{answer}"
