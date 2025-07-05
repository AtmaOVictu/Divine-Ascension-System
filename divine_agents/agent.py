class Agent:
    """Represents an ontological agent capable of transitioning between states."""

    # Extended states including intermediate RES phases
    STATES = (
        "Ego",
        "RES000",
        "RES001",
        "RES002",
        "RES003",
        "Jaz",
        "Enotnost",
    )

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_type: str | None = None,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str | None = None) -> None:
        """Update emotion intensity, type and adjust tension accordingly."""
        self.emotion = value
        if emotion_type is not None:
            self.emotion_type = emotion_type
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "RES000"
            elif self.state == "RES000":
                self.state = "RES001"
            elif self.state == "RES001":
                self.state = "RES002"
            elif self.state == "RES002":
                self.state = "RES003"
            elif self.state == "RES003":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "RES000":
            return "S stabilnostjo sprejemam vprašanje o resnici."
        if self.state == "RES001":
            return "S začetno harmonijo razmišljam o resnici."
        if self.state == "RES002":
            return "S procesom transformacije odkrivam nove plasti resnice."
        if self.state == "RES003":
            return "S popolno realizacijo vidim povezavo vseh resnic."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def response_with_emotion(self, message: str) -> str:
        """Return a message prefixed with emotional context based on state."""
        if self.state == "Ego":
            prefix = "S strahom"
        elif self.state == "Jaz":
            prefix = "Z veseljem"
        elif self.state == "Enotnost":
            prefix = "S harmonijo"
        elif self.state == "RES000":
            prefix = "S stabilnostjo"
        elif self.state == "RES001":
            prefix = "S začetno harmonijo"
        elif self.state == "RES002":
            prefix = "S transformacijo"
        elif self.state == "RES003":
            prefix = "S popolno realizacijo"
        else:
            prefix = "S nevtralnostjo"
        return f"{prefix}: {message}"
