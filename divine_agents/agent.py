class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Emotion and tension are clamped to the range 0.0 - 1.0 to
        avoid unrealistic values.
        """
        self.emotion = max(0.0, min(1.0, value))
        self.tension = max(0.0, min(1.0, self.tension + self.emotion))

    def update_tension(self, value: float) -> None:
        """Directly set tension level.

        Tension is clamped between 0.0 and 1.0.
        """
        self.tension = max(0.0, min(1.0, value))

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
        """Return a philosophical answer depending on the current state.

        The provided question influences the response when it concerns truth.
        """
        prompt = question.lower()
        if "resnica" in prompt or "truth" in prompt:
            if self.state == "Ego":
                return (
                    f"{self.name} (Ego): Resnica je absolutna in neodvisna od drugih."
                )
            if self.state == "Jaz":
                return (
                    f"{self.name} (Jaz): Resnica je relativna, oblikovana z našimi odnosi."
                )
            return (
                f"{self.name} (Enotnost): Vse resnice so eno, medsebojno povezane."
            )
        # Non-truth questions yield a generic response
        return f"{self.name}: Nimam odgovora na to."
