class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Human readable name of the agent.
    state:
        Ontological state of the agent (``"Ego"``, ``"Jaz"`` or ``"Enotnost"``).
    tension:
        Current tension level which may trigger a state change.
    emotion:
        Intensity of the current emotional response.
    emotion_label:
        Optional name of the current emotion (e.g. ``"jeza"`` or ``"strah"``).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_label: str | None = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label
        self.history = [state]

    def update_emotion(self, value: float, label: str | None = None) -> None:
        """Update emotional intensity and optionally set a label.

        Parameters
        ----------
        value:
            New emotional intensity.
        label:
            Optional description of the emotion (e.g. ``"strah"``).
        """
        self.emotion = value
        self.emotion_label = label or self.emotion_label
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
        """Return a philosophical answer influenced by the current state and emotion."""
        if self.state == "Ego":
            answer = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            answer = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            answer = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_label and self.emotion > 0.0:
            answer += f" Čutim {self.emotion_label} ({self.emotion:.1f})."

        return answer
