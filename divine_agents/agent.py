"""Ontological agents capable of transitioning philosophical states."""


class Agent:
    """Represents an ontological agent.

    The agent holds an ontological ``state`` (``Ego``, ``Jaz`` or ``Enotnost``)
    and two floating point values ``tension`` and ``emotion`` that influence
    possible transitions between states.  When either ``tension`` is greater
    than ``0.7`` or ``emotion`` is greater than ``0.5`` the agent will attempt
    to transition to the next state.
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
        """Return a philosophical answer influenced by current emotion."""
        emotion_note = "" if self.emotion <= 0.5 else " Moja custva so intenzivna." 

        if self.state == "Ego":
            return (
                "Resnica je absolutna in neodvisna od drugih." + emotion_note
            )
        if self.state == "Jaz":
            return (
                "Resnica je relativna, oblikovana z nasimi odnosi." + emotion_note
            )
        return "Vse resnice so eno, medsebojno povezane." + emotion_note
