"""Ontological agents used for philosophical dialogues."""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    emotion_type: str = "neutral"
    history: List[str] = field(default_factory=lambda: ["Ego"])

    STATES = ("Ego", "Jaz", "Enotnost")

    def update_emotion(self, value: float, emotion_type: str = "neutral") -> None:
        """Update emotion intensity and adjust tension and type.

        Parameters
        ----------
        value: float
            Intensity of the emotion in range 0-1.
        emotion_type: str
            Kind of emotion (e.g. 'fear', 'joy', 'anger').
        """

        self.emotion = value
        self.emotion_type = emotion_type
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Transition to the next ontological state when thresholds are met.

        Transition occurs if ``tension`` exceeds ``0.7`` or ``emotion`` exceeds
        ``0.5``. The sequence of states is ``Ego -> Jaz -> Enotnost``.
        """
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state.

        The emotional type alters the tone of the response.
        """

        prefix_map = {
            "fear": "(prestraženo) ",
            "anger": "(jezno) ",
            "joy": "(veselo) ",
        }
        prefix = prefix_map.get(self.emotion_type, "")

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        return prefix + base
