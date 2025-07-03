"""Core agent logic used across the simulation."""


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")
    EMOTIONS = ("neutral", "fear", "anger", "joy", "sorrow")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str = "neutral") -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def set_emotion(self, value: float, kind: str = "neutral") -> None:
        """Set emotion intensity and type while increasing tension."""
        if kind not in self.EMOTIONS:
            raise ValueError("Unknown emotion type")
        self.emotion = value
        self.emotion_type = kind
        self.tension += value

    # backward compatibility
    def update_emotion(self, value: float) -> None:
        self.set_emotion(value)

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
        """Return a philosophical answer depending on state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        prefix = ""
        if self.emotion_type == "anger":
            prefix = "Z jezo odgovarja: "
        elif self.emotion_type == "fear":
            prefix = "S strahom odgovarja: "
        elif self.emotion_type == "joy":
            prefix = "Z veseljem odgovarja: "
        elif self.emotion_type == "sorrow":
            prefix = "S potrtostjo odgovarja: "

        return f"{prefix}{base}"
