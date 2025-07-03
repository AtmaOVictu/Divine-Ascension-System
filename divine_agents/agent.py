class Agent:
    """Represent an ontological agent capable of transitioning states.

    Agents hold an emotion intensity and optional emotion name.  State
    transitions occur when either the emotion intensity exceeds ``0.5`` or the
    tension rises above ``0.7``.  Responses incorporate the current
    ontological state as well as the emotional context.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_name: str | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name or "neutral"
        self.history = [state]

    def update_emotion(self, value: float, name: str | None = None) -> None:
        """Update emotion intensity and optionally set emotion name.

        The tension is increased by the provided value to model how strong
        emotions raise inner pressure.
        """
        self.emotion = value
        if name is not None:
            self.emotion_name = name
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
        """Return a philosophical answer considering state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        emotion_part = "" if self.emotion_name == "neutral" else f"Ob\u010dutek {self.emotion_name}: "
        return f"{emotion_part}{base}"
