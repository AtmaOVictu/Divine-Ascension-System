class Agent:
    """Represents an ontological agent capable of transitioning states.

    The agent keeps track of its ontological ``state`` (``Ego`` -> ``Jaz`` ->
    ``Enotnost``), the current ``tension`` and ``emotion`` intensity and an
    optional ``emotion_label`` describing the feeling influencing its answers.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_label: str = "neutral") -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label
        self.history = [state]

    def update_emotion(self, value: float, label: str = "neutral") -> None:
        """Update emotional intensity and label and adjust tension.

        Parameters
        ----------
        value:
            Numerical representation of the emotional surge.
        label:
            Human readable tag describing the emotion (e.g. ``"anger"``).
        """
        self.emotion = value
        self.emotion_label = label
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
        """Return a philosophical answer influenced by ontological and emotional state."""

        emotion_prefix = {
            "anger": "Jezen odgovarjam: ",
            "fear": "V strahu pravim: ",
            "joy": "Z veseljem povem: ",
            "sorrow": "Žalosten menim: ",
            "neutral": "",
        }.get(self.emotion_label, "")

        if self.state == "Ego":
            message = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            message = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            message = "Vse resnice so eno, medsebojno povezane."

        return f"{emotion_prefix}{message}"
