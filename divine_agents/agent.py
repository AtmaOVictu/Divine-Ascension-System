class Agent:
    """Represents an ontological agent capable of transitioning states.

    Attributes
    ----------
    name : str
        Name of the agent.
    state : str
        Current ontological state (Ego, Jaz or Enotnost).
    tension : float
        Current tension level in range 0-1.
    emotion : float
        Emotion intensity in range 0-1.
    emotion_type : str
        Type of the current emotion (e.g. ``joy`` or ``fear``).
    history : list[str]
        History of states for debugging and analysis.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type or "neutral"
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str | None = None) -> None:
        """Update emotion intensity and optionally its type.

        Updating emotion increases tension by the same value, representing
        how strong feelings create additional strain on the agent.
        """
        self.emotion = value
        if emotion_type:
            self.emotion_type = emotion_type
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
        """Return a philosophical answer depending on the current state.

        The response also reflects the agent's current emotional tone.
        """
        emotion_note = f" Trenutno čutim {self.emotion_type}." if self.emotion_type else ""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih." + emotion_note
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi." + emotion_note
        return "Vse resnice so eno, medsebojno povezane." + emotion_note
