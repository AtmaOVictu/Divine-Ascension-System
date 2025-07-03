class Agent:
    """An ontological agent capable of emotional transitions.

    Parameters
    ----------
    name:
        Name of the agent.
    state:
        Initial ontological state (Ego, Jaz, Enotnost).
    tension:
        Initial tension level influencing transitions.
    emotion:
        Emotional intensity in range ``0.0`` to ``1.0``.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        # Keep a history of ontological states for introspection
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Set ``emotion`` to ``value`` and increase ``tension``.

        Parameters
        ----------
        value:
            Emotional intensity to apply.
        """
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set ``tension`` level."""
        self.tension = value

    def transition(self) -> str:
        """Transition between states when thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the emotional state."""

        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }

        emotion_desc = "mirno" if self.emotion <= 0.5 else "z močnimi čustvi"
        return f"{base.get(self.state, '')} Odgovarjam {emotion_desc}."
