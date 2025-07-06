class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        loyalty: float = 0.5,
        experiences=None,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.loyalty = loyalty
        self.experiences = experiences or []
        self.emotional_state = "neutral"
        self.history = [state]

    def update_emotion(self, value: float, label: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        if label:
            self.emotional_state = label
        self.adjust_tension_based_on_emotions()

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def adjust_tension_based_on_emotions(self) -> None:
        """Modify tension using the emotional state label."""
        if self.emotional_state == "angry":
            self.tension += 0.3
        elif self.emotional_state == "happy":
            self.tension -= 0.2
        else:
            self.tension += 0.1

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
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{base} (Čustvo: {self.emotional_state})"

    def add_experience(self, exp: str) -> None:
        """Add a textual experience to the agent."""
        self.experiences.append(exp)

    def learn_from_past_decisions(self, situation: str) -> str:
        """Return a decision hint based on past experiences."""
        if situation == "danger":
            if "helped" in self.experiences:
                return "Act selflessly"
            return "Self-preservation"
        return "Neutral decision"

    def auto_refactor(self) -> str:
        """Adjust the current state based on history keywords."""
        if "hesitation" in self.history:
            self.state = "Jaz"
        elif "self-preservation" in self.history:
            self.state = "Ego"
        return self.state
