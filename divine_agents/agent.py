class Agent:
    """Ontological agent capable of transitioning through philosophical states.

    Attributes
    ----------
    name : str
        Agent's identifier.
    state : str
        Current ontological state (``Ego``, ``Jaz`` or ``Enotnost``).
    tension : float
        Accumulated tension influencing transitions.
    emotion_level : float
        Intensity of the current emotion on a scale from 0 to 1.
    emotion : str
        Name of the current emotion.
    history : list[str]
        List of visited states in order.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion_level: float = 0.0, emotion: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion_level = emotion_level
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, emotion: str, intensity: float) -> None:
        """Update current emotion and adjust tension based on intensity."""
        self.emotion = emotion
        self.emotion_level = intensity
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Transition to the next state when thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_level > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def philosophical_principle(self) -> str:
        """Return the base philosophical principle for the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by state and emotion."""
        base = self.philosophical_principle()
        emotion_note = (
            f" Čutim {self.emotion} na ravni {self.emotion_level:.1f}."
            if self.emotion != "neutral" and self.emotion_level > 0
            else ""
        )
        return f"{base}{emotion_note}"
