class Agent:
    """Represent an ontological agent with emotional state and tension.

    Agents can transition between three philosophical states ``Ego``, ``Jaz``
    and ``Enotnost``. A transition occurs when either the internal ``tension``
    exceeds ``0.7`` or the ``emotion`` value rises above ``0.5``.  Each state
    provides a different perspective on truth.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def emotion_label(self) -> str:
        """Return a human readable label for the current emotional intensity."""
        if self.emotion >= 0.7:
            return "intenzivno"
        if self.emotion >= 0.3:
            return "umirjeno"
        return "mirno"

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
        """Return a philosophical answer reflecting current state and emotion."""
        prefix = f"{self.emotion_label()} izjavi: "
        if self.state == "Ego":
            core = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            core = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            core = "Vse resnice so eno, medsebojno povezane."
        return prefix + core
