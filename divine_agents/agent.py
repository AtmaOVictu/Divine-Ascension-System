class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Identifier of the agent.
    state:
        Initial ontological state.
    tension:
        Accumulated tension influencing state transitions.
    emotion:
        Intensity of the current emotional response.
    emotion_type:
        Kind of emotion (``fear``, ``joy``, ``anger`` or ``neutral``) which
        modifies tension and responses.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_type: str = "neutral",
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str | None = None) -> None:
        """Update emotion intensity and adjust tension.

        Negative emotions (fear, anger) increase tension more drastically than
        positive ones (joy). If ``emotion_type`` is provided, the agent's current
        type is updated accordingly.
        """
        self.emotion = value
        if emotion_type is not None:
            self.emotion_type = emotion_type

        if self.emotion_type in {"fear", "anger"}:
            self.tension += value
        elif self.emotion_type == "joy":
            self.tension += value / 2
        else:
            self.tension += value * 0.1

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
        """Return a philosophical answer influenced by current emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_type == "fear":
            emotion_part = " Čutim strah, kar povečuje napetost."
        elif self.emotion_type == "anger":
            emotion_part = " Sem jezen in to usmerja moj odgovor."
        elif self.emotion_type == "joy":
            emotion_part = " Preveva me veselje, zato sem bolj odprt."
        else:
            emotion_part = ""

        return base + emotion_part
