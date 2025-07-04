class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0,
                 emotion_label: str | None = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label
        self.synonyms: list["Agent"] = []
        self.history = [state]

    def update_emotion(self, value: float, label: str | None = None) -> None:
        """Update emotion intensity and label, adjusting tension accordingly."""
        self.emotion = value
        if label is not None:
            self.emotion_label = label
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

    def add_synonym_agent(self, other: "Agent") -> None:
        """Create a synonym link to another agent."""
        if other not in self.synonyms:
            self.synonyms.append(other)

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state and emotion."""
        base_reply = ""
        if self.state == "Ego":
            base_reply = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base_reply = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base_reply = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_label:
            return f"({self.emotion_label}) {base_reply}"
        return base_reply
