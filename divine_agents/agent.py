"""Core primitives for the divine agents.

This module defines the :class:`Agent` used throughout the system.  An agent
maintains an ontological state (``Ego``, ``Jaz`` or ``Enotnost``) and may
transition between these states when its emotional intensity or tension exceed
defined thresholds.  Each response that an agent gives is coloured by its
current emotional level.
"""


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    # Thresholds controlling the transition behaviour
    TENSION_THRESHOLD = 0.7
    EMOTION_THRESHOLD = 0.5

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        # Emotion feeds into tension which can trigger state changes
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > self.TENSION_THRESHOLD or self.emotion > self.EMOTION_THRESHOLD:
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

        if self.emotion > 0.7:
            prefix = "Strastno povem:"  # passionately
        elif self.emotion < 0.3:
            prefix = "Mirno odgovorim:"  # calmly
        else:
            prefix = "S čustvi razložim:"  # moderately emotional
        return f"{prefix} {base}"
