class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str = "neutral") -> None:
        """Update emotion intensity and adjust tension based on emotion type."""
        self.emotion = value
        self.emotion_type = emotion_type
        # Fear and anger induce stronger tension increase
        if emotion_type in {"fear", "anger"}:
            self.tension += value
        else:
            self.tension += value * 0.5

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
        """Return a philosophical answer depending on the current state."""
        mood = {
            "fear": "v strahu",
            "anger": "z jezo",
            "joy": "z veseljem",
        }.get(self.emotion_type, "mirno")

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        return f"{base} ({mood})"

    def speak(self, question: str) -> str:
        """Return a full dialogue line including the agent's name and state."""
        return f"{self.name} ({self.state}): {self.respond(question)}"

    def transition_line(self) -> str:
        """Perform transition and return an explanatory line."""
        new_state = self.transition()
        return f"{self.name} prehaja v stanje: {new_state}"
