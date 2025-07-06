class Agent:
    """Represents an ontological agent capable of transitioning states.

    The agent stores its current ontological ``state`` (``Ego``/``Jaz``/``Enotnost``),
    the level of ``tension`` it feels and the ``emotion`` intensity associated
    with an ``emotion_label``.  Tension and emotion intensity influence state
    transitions.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", *, tension: float = 0.0,
                 emotion: float = 0.0, emotion_label: str = "nevtralno") -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label
        # history stores snapshots of the agent across transitions
        self.history = [
            {
                "state": state,
                "tension": tension,
                "emotion": emotion,
                "emotion_label": emotion_label,
            }
        ]

    def set_emotion(self, label: str, intensity: float) -> None:
        """Set the current emotion label and intensity.

        Setting an emotion increases the agent's tension by the same amount,
        providing a simple coupling between how strongly an emotion is felt and
        the resulting mental strain.
        """
        self.emotion_label = label
        self.emotion = intensity
        self.tension += intensity

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity without changing the label."""
        self.emotion = value
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
        self.history.append(
            {
                "state": self.state,
                "tension": self.tension,
                "emotion": self.emotion,
                "emotion_label": self.emotion_label,
            }
        )
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the current emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{base} Čutim {self.emotion_label}."
