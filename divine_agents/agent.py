class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Display name of the agent.
    state:
        Ontological state of the agent. One of :data:`STATES`.
    tension:
        Current tension level which can trigger a state transition.
    emotion:
        Current emotion intensity in the range ``0.0`` - ``1.0``.
    emotion_name:
        Descriptive emotion label such as ``fear`` or ``joy``.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0,
                 emotion_name: str | None = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def set_emotion(self, name: str, value: float) -> None:
        """Assign an emotion label with an intensity and adjust tension.

        Parameters
        ----------
        name:
            Descriptive emotion label, e.g. ``fear`` or ``joy``.
        value:
            Emotion intensity between ``0`` and ``1``.
        """
        self.emotion_name = name
        self.update_emotion(value)

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

    def __repr__(self) -> str:  # pragma: no cover - debugging helper
        return (
            f"Agent(name={self.name!r}, state={self.state!r}, "
            f"tension={self.tension:.2f}, emotion={self.emotion:.2f})"
        )

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        prefix = f"[{self.emotion_name}] " if self.emotion_name else ""
        if self.state == "Ego":
            return prefix + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return prefix + "Resnica je relativna, oblikovana z našimi odnosi."
        return prefix + "Vse resnice so eno, medsebojno povezane."
