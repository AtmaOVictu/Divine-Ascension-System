class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Agent identifier.
    state:
        Initial ontological state (``Ego``, ``Jaz`` or ``Enotnost``).
    tension:
        Initial level of tension.
    emotion:
        Initial emotional intensity. ``emotion_type`` describes the emotion
        affecting the agent.
    emotion_type:
        A human readable label of the emotion (e.g. ``fear`` or ``joy``).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, emotion_type: str, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        emotion_type:
            Label describing the emotion (``fear``, ``joy``, ``anger`` ...).
        value:
            Intensity of the emotion in range ``0.0`` to ``1.0``.
        """
        self.emotion_type = emotion_type
        self.emotion = value
        # Emotion intensity contributes to the overall tension
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform a state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state.

        The emotional state influences how the answer is phrased.
        """
        base = ""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        # Simple emotional modification of the reply
        if self.emotion_type == "joy":
            return f"[veselje] {base}"
        if self.emotion_type == "fear":
            return f"[strah] {base}"
        if self.emotion_type == "anger":
            return f"[jeza] {base}"
        return base
