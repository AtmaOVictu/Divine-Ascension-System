class Agent:
    """Represent an ontological agent capable of transitioning states.

    Each agent holds an ontological ``state`` and is influenced by
    ``emotion`` and ``tension``.  When either emotion or tension exceeds
    their threshold, the agent progresses to the next philosophical
    state (``Ego`` → ``Jaz`` → ``Enotnost``).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, emotion_name: str | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def set_emotion(self, name: str, intensity: float) -> None:
        """Set current emotion ``name`` and its ``intensity``.

        Setting an emotion automatically updates both the internal
        ``emotion`` value and increases ``tension`` which may trigger a
        state transition.
        """
        self.emotion_name = name
        self.update_emotion(intensity)

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
        """Return a philosophical answer depending on the current state."""
        prefix = {
            "fear": "S strahom, ",
            "joy": "Z veseljem, ",
            "anger": "Z jezo, ",
        }.get(self.emotion_name, "")

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return prefix + base
