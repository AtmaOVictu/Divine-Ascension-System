"""Ontological agent implementations."""


class Agent:
    """Represents an agent that can transition between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")
    TENSION_THRESHOLD = 0.7
    EMOTION_THRESHOLD = 0.5

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.meditation_state = False

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > self.TENSION_THRESHOLD or self.emotion > self.EMOTION_THRESHOLD:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def meditate(self) -> str:
        """Reflect on current state and transition if thresholds are exceeded."""
        self.meditation_state = True
        message = "Meditacija zaključen: prehod ni potreben"
        if self.tension > self.TENSION_THRESHOLD or self.emotion > self.EMOTION_THRESHOLD:
            prev_state = self.state
            self.transition()
            message = f"Meditacija zaključen: prehod iz {prev_state} v {self.state}"
        self.meditation_state = False
        return message

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > self.EMOTION_THRESHOLD:
            return f"{base} (čustveno)"
        return base
