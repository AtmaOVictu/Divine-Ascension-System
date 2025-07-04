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
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

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
        """Return a philosophical answer incorporating the question."""
        if self.state == "Ego":
            return (
                f"Na vprašanje '{question}' odgovarjam: "
                "Resnica je absolutna in neodvisna od drugih."
            )
        if self.state == "Jaz":
            return (
                f"V zvezi z '{question}' verjamem, "
                "da je resnica relativna, oblikovana z našimi odnosi."
            )
        return (
            f"Kar zadeva '{question}', "
            "vse resnice so eno, medsebojno povezane."
        )
