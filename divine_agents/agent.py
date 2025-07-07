from __future__ import annotations

from dataclasses import dataclass


class Agent:
    """Ontological agent capable of transitioning between states.

    Attributes
    ----------
    name:
        Unique identifier of the agent.
    state:
        Current ontological state (``"Ego"``, ``"Jaz"`` or ``"Enotnost"``).
    tension:
        Numeric representation of inner tension.
    emotion_level:
        Intensity of the current emotion in the ``[0, 1]`` range.
    emotion_type:
        Optional label of the emotion influencing the agent (e.g. ``"fear"``).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", *, tension: float = 0.0, emotion_level: float = 0.0,
                 emotion_type: str | None = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion_level = emotion_level
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, level: float, emotion_type: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        level:
            Intensity of the emotion in the ``[0, 1]`` range.
        emotion_type:
            Optional descriptive label of the emotion.  If provided the agent
            will incorporate this into its responses.
        """

        self.emotion_level = level
        self.emotion_type = emotion_type or self.emotion_type
        # Increasing emotion typically raises tension as well.
        self.tension = max(self.tension, level)

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
        base: str
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_type:
            return f"{base} (občutek {self.emotion_type})"
        return base
