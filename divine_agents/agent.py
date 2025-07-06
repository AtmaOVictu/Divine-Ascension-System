class Agent:
    """Ontological agent capable of transitioning through philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_label: str = "neutral",
        loyalty: float = 0.0,
        experiences=None,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label
        self.loyalty = loyalty
        self.experiences = experiences or []
        self.history = [state]

    def update_emotion(self, value: float, label: str | None = None) -> None:
        """Update emotion intensity and optionally set the emotion label."""
        self.emotion = value
        self.tension += value
        if label is not None:
            self.emotion_label = label

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def add_experience(self, experience: str) -> None:
        """Store an experience that might influence future transitions."""
        self.experiences.append(experience)

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def multi_layer_transition(self) -> str:
        """Transition considering emotion, tension, loyalty and experiences."""
        experience_layer = self.experiences[-1] if self.experiences else "neutral"
        if self.state == "Ego" and (self.tension > 0.7 or self.emotion > 0.5):
            self.state = "Jaz"
        elif self.state == "Jaz" and (self.loyalty > 0.8 or "selfish" in experience_layer):
            self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            answer = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            answer = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            answer = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_label == "angry":
            answer += " Čutim jezo."
        elif self.emotion_label == "fearful":
            answer += " Čutim strah."
        elif self.emotion_label == "happy":
            answer += " Čutim veselje."
        return answer
