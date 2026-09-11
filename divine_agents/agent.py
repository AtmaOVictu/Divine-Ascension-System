class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Agent identifier.
    state:
        One of :pydata:`STATES`.
    tension:
        Current tension level (0-1).
    emotion:
        Current emotion intensity (0-1).
    """

    STATES = ("Ego", "Jaz", "Enotnost")
    TENSION_THRESHOLD = 0.7
    EMOTION_THRESHOLD = 0.5

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly.

        The emotion value is clamped to the ``0-1`` range and directly
        increases tension. This mirrors how a strong emotional reaction
        builds up internal conflict within the agent.
        """
        self.emotion = max(0.0, min(1.0, value))
        self.tension = max(0.0, min(1.0, self.tension + value))

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = max(0.0, min(1.0, value))

    def transition(self) -> str:
        """Perform a state transition if thresholds are exceeded."""
        if self.tension > self.TENSION_THRESHOLD or self.emotion > self.EMOTION_THRESHOLD:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state.

        Emotion intensifies the agent's response. When emotion is high the
        answer becomes more emphatic, illustrating the influence of the
        internal state on philosophical outlook.
        """
        intense = self.emotion > self.EMOTION_THRESHOLD

        if self.state == "Ego":
            base = "Truth is absolute and independent of others."
            return base + (" I feel this deeply." if intense else "")

        if self.state == "Jaz":
            base = "Truth is relative, shaped by our relationships."
            return base + (" Močno čutim povezanost." if intense else "")

        base = "All truths are one, interconnected."
        return base + (" Jasno zaznavam to enost." if intense else "")
