class Agent:
    """Ontological agent capable of transitioning between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost", "RES001")

    def __init__(self, name: str, state: str = "Ego", emotion: float = 0.0,
                 tension: float = 0.0, emotion_type: str = "nevtralno"):
        self.name = name
        self.state = state
        self.emotion = emotion
        self.tension = tension
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str) -> None:
        """Update emotion intensity, emotion type and adjust tension."""
        self.emotion = value
        self.emotion_type = emotion_type
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition when thresholds are exceeded."""
        if self.emotion > 0.5 or self.tension > 0.7:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
            elif self.state == "Enotnost":
                self.state = "RES001"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        if self.state == "Enotnost":
            return "Vse resnice so eno, medsebojno povezane."
        return "Prehajam v popolno enotnost vseh resnic."

    def response_with_emotion(self, message: str) -> str:
        """Generate a response with an emotional prefix."""
        if self.emotion_type == "strah":
            prefix = "S strahom"
        elif self.emotion_type == "veselje":
            prefix = "Z veseljem"
        elif self.emotion_type == "jeza":
            prefix = "S jezo"
        else:
            prefix = "S nevtralnostjo"
        return f"{prefix}: {message}"

    def __str__(self) -> str:
        return (f"Agent {self.name} je v stanju: {self.state}, "
                f"čustvo: {self.emotion_type}, zgodovina: {self.history}")
