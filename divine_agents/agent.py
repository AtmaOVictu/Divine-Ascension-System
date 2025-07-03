class Agent:
    """Represents an ontological agent capable of transitioning ontological
    states based on emotion and tension.

    Each agent tracks the intensity of its current ``emotion`` and
    ``tension``.  When either value exceeds the configured thresholds the
    agent will transition from ``Ego`` -> ``Jaz`` -> ``Enotnost``.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    # Numeric values associated with named emotions.  The values roughly map to
    # the amount of tension an emotion introduces into the system.
    EMOTION_MAP = {
        "fear": 0.6,
        "joy": 0.4,
        "anger": 0.7,
        "sorrow": 0.5,
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = ""
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension = min(1.0, self.tension + value)

    def set_emotion(self, label: str) -> None:
        """Set the current emotion by label and update tension."""
        self.emotion_label = label
        self.update_emotion(self.EMOTION_MAP.get(label, 0.0))

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

        The returned string also reflects the agent's current emotional
        descriptor if one is set.
        """
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_label:
            return f"{base} Čutim {self.emotion_label}."
        return base
