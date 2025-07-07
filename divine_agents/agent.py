class Agent:
    """Represent an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Name of the agent.
    state:
        Starting ontological state. One of ``Ego``, ``Jaz`` or ``Enotnost``.
    tension:
        Initial tension level.
    emotion:
        Initial emotion intensity.
    emotion_name:
        Label of the current emotion (e.g. ``fear``, ``joy``).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", *, tension: float = 0.0, emotion: float = 0.0, emotion_name: str = "neutral") -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name
        self.history = [state]

    def update_emotion(self, value: float, name: str = "neutral") -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value:
            New emotion intensity.
        name:
            Descriptive label of the emotion (e.g. ``fear``, ``anger``).
        """
        self.emotion = value
        self.emotion_name = name
        # emotion contributes directly to tension
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform a state transition when thresholds are exceeded.

        The agent moves from ``Ego`` to ``Jaz`` or from ``Jaz`` to ``Enotnost``
        when either the current tension is greater than ``0.7`` or the emotion
        intensity exceeds ``0.5``.
        """
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on state and emotion."""
        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }[self.state]

        emotional_tone = {
            "fear": " v strahu.",
            "anger": " v jezi.",
            "joy": " z veseljem.",
            "neutral": "",
        }.get(self.emotion_name, "")

        return base + emotional_tone
