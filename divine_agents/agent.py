"""Core agent logic for the ontological system."""

from dataclasses import dataclass, field


@dataclass
class Agent:
    """Ontological agent capable of emotional transitions.

    Parameters
    ----------
    name:
        Display name of the agent.
    state:
        Ontological state (Ego, Jaz or Enotnost).
    tension:
        Current level of tension. Values greater than ``0.7`` may trigger a
        transition.
    emotion:
        Current emotional intensity. Values greater than ``0.5`` may trigger a
        transition.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    history: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.history.append(self.state)

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension.

        Parameters
        ----------
        value:
            New emotional value in range ``0.0``-``1.0``.
        """
        self.emotion = value
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
        """Return a philosophical answer depending on the current state."""
        emotion_note = "" if self.emotion < 0.6 else " Moja čustva so intenzivna." 
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih." + emotion_note
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi." + emotion_note
        return "Vse resnice so eno, medsebojno povezane." + emotion_note
