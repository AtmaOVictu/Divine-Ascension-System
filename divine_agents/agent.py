class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Unique name of the agent.
    state:
        Current ontological state. One of ``"Ego"``, ``"Jaz"`` or ``"Enotnost"``.
    tension:
        Current tension level of the agent.
    emotion:
        Current emotional intensity.
    emotion_type:
        Description of the current emotional quality (e.g. ``"fear"`` or ``"joy"``).
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

    def update_emotion(self, intensity: float, emotion_type: str = "neutral") -> None:
        """Update emotion intensity and adjust tension and emotion type.

        Parameters
        ----------
        intensity:
            New emotional intensity.
        emotion_type:
            Qualitative description of the emotion (e.g. ``"fear"``).
        """
        self.emotion = intensity
        self.emotion_type = emotion_type
        self.tension += intensity

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

    def section_transition(self) -> str:
        """Perform a fine-grained transition based on current attributes.

        This method encapsulates the logic described in the user instructions
        where tension, emotion and environmental cues can nudge the agent into
        a specific state segment.
        """
        if self.tension < 0.3:
            self.state = "Ego"
        elif self.emotion > 0.5:
            self.state = "Jaz"
        else:
            self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state.

        The emotional context influences how the answer is presented.
        """
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{base} (\u010custvo: {self.emotion_type}, intenziteta: {self.emotion:.2f})"
