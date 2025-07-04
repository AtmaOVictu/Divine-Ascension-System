class Agent:
    """Ontological agent capable of transitioning between states.

    The agent moves from ``Ego`` to ``Jaz`` and finally ``Enotnost`` when its
    tension or emotion exceed the defined thresholds.  Emotion also increases
    the agent's tension which in turn influences the next transition.
    """

    STATES = ("Ego", "Jaz", "Enotnost")
    TRANSITION_THRESHOLD_TENSION = 0.7
    TRANSITION_THRESHOLD_EMOTION = 0.5

    def __init__(self, name: str, state: str = "Ego", *, tension: float = 0.0, emotion: float = 0.0) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def emotion_descriptor(self) -> str:
        """Return a short descriptor representing current emotional state."""
        if self.emotion > 0.7:
            return "z veliko strastjo"
        if self.emotion > 0.3:
            return "umirjeno"
        return "mirno"

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if (
            self.tension > self.TRANSITION_THRESHOLD_TENSION
            or self.emotion > self.TRANSITION_THRESHOLD_EMOTION
        ):
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def speak(self, question: str) -> str:
        """Return the agent's statement with emotional context."""
        base = self.respond(question)
        return f"{self.emotion_descriptor()}: {base}"
