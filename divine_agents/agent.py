"""Ontology based agent implementation."""


class Agent:
    """Represents an ontological agent capable of transitioning states.

    The agent holds an emotional state and a tension level. When either the
    tension exceeds ``0.7`` or the emotion exceeds ``0.5`` the agent will
    transition from ``Ego`` -> ``Jaz`` or ``Jaz`` -> ``Enotnost``.  The history
    of states is kept for inspection and testing.
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

    def emotional_descriptor(self) -> str:
        """Return a textual representation of the current emotional intensity."""
        if self.emotion >= 0.7:
            return "z velikim čustvenim nabojem"
        if self.emotion >= 0.3:
            return "s srednjo mero čustev"
        return "mirno"

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
        """Return a philosophical answer influenced by emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        return f"{base} ({self.emotional_descriptor()})"
