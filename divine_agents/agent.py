from __future__ import annotations

class Agent:
    """Represents an ontological agent capable of transitioning states.

    The agent tracks its ontological ``state`` (``Ego`` / ``Jaz`` / ``Enotnost``),
    current ``tension`` level and ``emotion`` intensity as floating point values
    between ``0`` and ``1``.  In addition to the numeric emotion intensity the
    ``emotion_type`` attribute records the flavour of the emotion (e.g.
    ``"fear"``, ``"joy"`` or ``"anger"``).  Transitions between ontological
    states occur when the tension or emotion intensity exceed predefined
    thresholds.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_type: str = "neutral",
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, label: str | None = None) -> None:
        """Update emotion intensity and optionally change emotion type.

        The tension level is increased by the provided ``value``.  If ``label``
        is supplied, ``emotion_type`` is updated as well.
        """
        self.emotion = value
        if label is not None:
            self.emotion_type = label
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
        """Return a philosophical answer influenced by the current emotion."""
        emotion_prefix = {
            "fear": "Drhteče",
            "joy": "V radosti",
            "anger": "Z jezo",
        }.get(self.emotion_type, "")

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        return f"{emotion_prefix} {base}".strip()
