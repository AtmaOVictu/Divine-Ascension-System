"""Core agent logic for the ontological framework.

Each ``Agent`` can reside in one of three states: ``Ego``, ``Jaz`` or
``Enotnost``.  Transitions between these states are triggered when either the
current ``tension`` exceeds ``0.7`` or ``emotion`` rises above ``0.5``.  The
agent also keeps a history of all states it has visited, which can be used for
further analysis or debugging.
"""


class Agent:
    """Represents an ontological agent capable of transitioning states."""

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

    def reflect(self) -> str:
        """Return a textual representation of the agent's state history."""
        return " -> ".join(self.history)

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
        """Return a philosophical answer depending on the current state.

        The response also reflects the agent's current emotional intensity.
        """
        emotion_note = self._emotion_note()
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{base}{emotion_note}"

    def _emotion_note(self) -> str:
        """Return a short textual note describing the current emotion level."""
        if self.emotion > 0.7:
            return " Čutim močna čustva, kar vpliva na moj odgovor." \
                if self.state != "Enotnost" else " Čutim globoko povezanost."
        if self.emotion > 0.3:
            return " Čutim določeno napetost."
        return ""
