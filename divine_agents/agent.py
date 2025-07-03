class Agent:
    """Ontological agent capable of emotional state transitions."""

    STATES = ("Ego", "Jaz", "Enotnost")

    EMOTION_THRESHOLD = 0.5
    TENSION_THRESHOLD = 0.7

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

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

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        mood = self._describe_emotion()
        return f"{base}{mood}"

    def _describe_emotion(self) -> str:
        """Return a short description of the agent's current emotional state."""
        if self.emotion > 0.5:
            return " Moja čustva so močna in vplivajo na razmišljanje."
        if self.emotion > 0.2:
            return " Čustveno sem nekoliko vznemirjen."
        return ""
