class Agent:
    """Ontological agent capable of transitioning through philosophical states."""

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
        emotion_type: str = "nevtralno",
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str) -> None:
        """Update emotional intensity and type, adjusting tension."""
        self.emotion = value
        self.emotion_type = emotion_type
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set the tension level."""
        self.tension = value

    def _next_state(self) -> str:
        """Return the next state in the sequence."""
        idx = self.STATES.index(self.state)
        if idx < len(self.STATES) - 1:
            return self.STATES[idx + 1]
        return self.state

    def transition(self) -> str:
        """Perform a state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            self.state = self._next_state()
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "RES000":
            return "Stabilno stanje pripravljenosti na spremembo."
        if self.state == "RES001":
            return "Začetna harmonija združevanja elementov sistema."
        if self.state == "RES002":
            return "Faza napetosti in transformacije."
        if self.state == "RES003":
            return "Faza popolne realizacije vseh delov."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def response_with_emotion(self, message: str) -> str:
        """Generate a response with an emotional prefix."""
        prefixes = {
            "Ego": "S strahom",
            "Jaz": "Z veseljem",
            "Enotnost": "S harmonijo",
            "RES000": "S stabilnostjo",
            "RES001": "S začetno harmonijo",
            "RES002": "S transformacijo",
            "RES003": "S popolno realizacijo",
        }
        prefix = prefixes.get(self.state, "S nevtralnostjo")
        return f"{prefix}: {message}"

    def __str__(self) -> str:  # pragma: no cover - debug convenience
        return f"Agent {self.name} je v stanju: {self.state}, zgodovina: {self.history}"
