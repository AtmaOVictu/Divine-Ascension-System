class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Name of the agent.
    state:
        Ontological state (Ego, Jaz, or Enotnost).
    tension:
        Current tension level.
    emotion:
        Intensity of the current emotion.
    mood:
        Qualitative description of the emotion (e.g. ``"fear"``).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    MOOD_PREFIX = {
        "fear": "Z občutkom strahu, ",
        "joy": "Z veseljem, ",
        "anger": "Z jezo, ",
        "neutral": "",
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, mood: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.mood = mood
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def set_mood(self, mood: str) -> None:
        """Set qualitative emotional state."""
        self.mood = mood

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
        """Return a philosophical answer depending on state and mood."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        prefix = self.MOOD_PREFIX.get(self.mood, "")
        return prefix + base
