class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_label: str | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label or "neutral"
        self.history = [state]

    def update_emotion(self, value: float, label: str | None = None) -> None:
        """Update emotion intensity and optionally set an emotion label."""
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

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."


class AgentWithConflict(Agent):
    """Agent that handles moral or philosophical conflicts."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_label: str | None = None,
                 conflict: str | None = None):
        super().__init__(name, state, tension, emotion, emotion_label)
        self.conflict = conflict or "neznan"

    def choose_path(self) -> str:
        """Choose a path when faced with conflict and adjust state."""
        if self.conflict == "moralna dilema":
            self.update_emotion(self.emotion + 0.3, "fear")
            self.state = "Jaz"
        elif self.conflict == "filozofska dilema":
            self.update_emotion(self.emotion + 0.5, "anger")
            self.state = "Enotnost"
        else:
            self.update_emotion(self.emotion, self.emotion_label)
        self.history.append(self.state)
        return self.state
