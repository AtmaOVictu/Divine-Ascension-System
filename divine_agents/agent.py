from typing import Optional


class Agent:
    """Represent an ontological agent capable of transitioning states.

    Attributes
    ----------
    name : str
        Name of the agent.
    state : str
        Current ontological state (``Ego``, ``Jaz``, or ``Enotnost``).
    tension : float
        Numeric tension level in the range ``0`` to ``1``.
    emotion : float
        Intensity of the current emotion in the range ``0`` to ``1``.
    emotion_label : str
        Description of the current emotion (e.g. ``fear`` or ``joy``).
    history : list[str]
        Ordered list of visited states.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_label: str = "nevtralno"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label
        self.history = [state]

    def update_emotion(self, value: float, label: Optional[str] = None) -> None:
        """Update emotion intensity and optionally its descriptive label."""
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
        """Return a philosophical answer influenced by the current state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{base} Čutim {self.emotion_label}."
