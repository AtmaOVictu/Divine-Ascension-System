class Agent:
    """Represents an ontological agent capable of transitioning states.

    Attributes
    ----------
    name: str
        The display name of the agent.
    state: str
        Current ontological state (``Ego``, ``Jaz`` or ``Enotnost``).
    tension: float
        Level of inner tension. Values above ``0.7`` trigger transitions.
    emotion: float
        Intensity of the current emotion. Values above ``0.5`` may also
        trigger a transition.
    emotion_label: str
        Optional textual description of the current emotion (e.g. ``jeza``).
    history: list[str]
        Keeps a history of states for introspection.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0,
                 emotion_label: str | None = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label
        self.history = [state]

    def update_emotion(self, value: float, label: str | None = None) -> None:
        """Update emotion intensity, optionally setting an emotion label.

        Parameters
        ----------
        value:
            Intensity of the emotion. Also contributes to tension.
        label:
            Descriptive label of the emotion (e.g. ``jeza``).
        """
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
            response = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            response = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            response = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.5 and self.emotion_label:
            response += f" Čutim {self.emotion_label}."
        elif self.emotion > 0.5:
            response += " Čustveno se odzivam." 

        return response

