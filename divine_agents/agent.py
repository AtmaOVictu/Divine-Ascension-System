class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion_level: float = 0.0, emotion: str = "neutral") -> None:
        """Create a new agent.

        Parameters
        ----------
        name:
            Agent name.
        state:
            Ontological state of the agent.
        tension:
            Current tension level.
        emotion_level:
            Intensity of the current emotion.
        emotion:
            Name of the current emotion (e.g. 'fear', 'joy').
        """
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion_level = emotion_level
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, intensity: float, emotion: str = None) -> None:
        """Update the current emotion and adjust tension.

        Parameters
        ----------
        intensity:
            Numerical intensity of the emotion.
        emotion:
            Optional name of the emotion.
        """
        self.emotion_level = intensity
        if emotion is not None:
            self.emotion = emotion
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_level > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion != "neutral":
            base += f" Čutim {self.emotion}."
        return base
