class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", *, tension: float = 0.0, emotion: float = 0.0, emotion_type: str = "nevtralno"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str) -> None:
        """Update emotion intensity, type, and adjust tension accordingly."""
        self.emotion = value
        self.emotion_type = emotion_type
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

    def __str__(self) -> str:
        return (
            f"Agent {self.name} je v stanju: {self.state}, "
            f"čustvo: {self.emotion_type}, zgodovina: {self.history}"
        )

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            answer = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            answer = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            answer = "Vse resnice so eno, medsebojno povezane."
        return self.response_with_emotion(answer)

    def response_with_emotion(self, message: str) -> str:
        """Return message prefixed with emotional context."""
        prefixes = {
            "strah": "S strahom",
            "veselje": "Z veseljem",
            "jeza": "S jezo",
        }
        prefix = prefixes.get(self.emotion_type, "S nevtralnostjo")
        return f"{prefix}: {message}"
