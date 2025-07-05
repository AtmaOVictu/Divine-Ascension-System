"""Core primitives for philosophical agents."""


class Agent:
    """Ontological agent capable of transitioning between states.

    Parameters
    ----------
    name:
        Human readable identifier for the agent.
    state:
        Starting ontological state (``"Ego"``, ``"Jaz"`` or ``"Enotnost"``).
    tension:
        Initial tension level in range ``[0.0, 1.0]``.
    emotion:
        Initial emotion intensity in range ``[0.0, 1.0]``.
    emotion_type:
        Optional label describing the current dominant emotion.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, emotion_type: str | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type or "neutral"
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def feel(self, emotion_type: str, intensity: float) -> None:
        """Register an emotion and modify tension accordingly."""
        self.emotion_type = emotion_type
        self.emotion = intensity
        if emotion_type in {"fear", "anger"}:
            self.tension += intensity
        elif emotion_type == "joy":
            self.tension -= intensity / 2
        self.tension = max(0.0, min(1.0, self.tension))

    def update_tension(self, value: float) -> None:
        """Directly set the current tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if emotion or tension exceed thresholds."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the current state and emotion."""
        prefix = ""
        if self.emotion_type and self.emotion_type != "neutral":
            prefix = f"{self.emotion_type.capitalize()}: "

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return prefix + base
