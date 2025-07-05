class Agent:
    """Represents an ontological agent capable of transitioning states.

    The class embodies the ontological movement from **DA** (potencial) to
    **JA** (aktivacija). Each agent begins in one of the philosophical phases
    ``Ego``, ``Jaz`` or ``Enotnost`` and can move forward when tension or
    emotional intensity surpass specified thresholds.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def set_emotion(self, emotion_type: str, intensity: float) -> None:
        """Set the current emotion type and intensity."""
        self.emotion_type = emotion_type
        self.update_emotion(intensity)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded.

        A transition symbolises prehod iz "DA" v "JA". If ``tension`` exceeds
        ``0.7`` or ``emotion`` surpasses ``0.5``, the agent advances to the next
        philosophical phase.
        """
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state.

        The response embodies the agent's current understanding of resnica
        (truth) as shaped by its ontological phase and emotional colouring.
        """
        if self.state == "Ego":
            reply = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            reply = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            reply = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_type:
            reply += f" (čutim {self.emotion_type})"
        return reply
