from typing import Optional


class Agent:
    """Represent an ontological agent capable of transitioning states.

    Attributes
    ----------
    name: str
        Name of the agent.
    state: str
        Current ontological state (Ego, Jaz, Enotnost).
    tension: float
        Accumulated tension value influencing transitions.
    emotion: float
        Current emotion intensity.
    emotion_name: str
        Descriptive emotion label (e.g. "fear", "joy").
    history: list[str]
        Record of all states the agent has occupied.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_name: str = ""):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name
        self.history = [state]

    def update_emotion(self, value: float, name: Optional[str] = None) -> None:
        """Update emotion intensity and optionally set an emotion label.

        Parameters
        ----------
        value:
            Intensity of the emotion. Also increases tension by the same amount.
        name:
            Optional human readable label of the emotion.
        """
        self.emotion = value
        if name is not None:
            self.emotion_name = name
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set the tension level."""
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
        """Return a philosophical answer influenced by the current state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_name:
            base += f" Čutim {self.emotion_name}."
        return base
