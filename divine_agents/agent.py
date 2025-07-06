class Agent:
    """An ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        The name of the agent.
    state:
        Initial ontological state (``Ego`` | ``Jaz`` | ``Enotnost``).
    tension:
        Initial tension value.
    emotion:
        Initial emotion intensity.
    emotion_label:
        Human readable description of the current emotion.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_label: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label
        self.history = [state]

    def update_emotion(self, value: float, label: str = "neutral") -> None:
        """Update emotion intensity, description and adjust tension."""
        self.emotion = value
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
        """Return a philosophical answer influenced by the current emotion."""
        prefix = ""
        if self.emotion_label != "neutral":
            prefix = f"Ob \u010dustvu {self.emotion_label}, "

        if self.state == "Ego":
            core = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            core = "Resnica je relativna, oblikovana z na\u0161imi odnosi."
        else:
            core = "Vse resnice so eno, medsebojno povezane."

        return prefix + core
