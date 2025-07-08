"""Core logic for ontological agents.

Agents evolve through philosophical states (``Ego``, ``Jaz``, ``Enotnost``)
based on their emotional intensity and internal tension.  The transition
rules are simple: whenever ``tension`` exceeds ``0.7`` **or** ``emotion``
exceeds ``0.5`` the agent advances to the next state.  The philosophical
principles for each state are embedded in ``respond`` which produces a
statement coloured by the current emotional level.
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
        self.emotion = max(0.0, min(1.0, value))
        # Emotions feed into tension which in turn can trigger transitions
        self.tension = max(0.0, min(1.0, self.tension + self.emotion))

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = max(0.0, min(1.0, value))

    def perform_action(self, kind: str) -> None:
        """Simple behaviour simulation that alters emotion and tension."""
        if kind == "good":
            self.update_emotion(self.emotion - 0.1)
            self.update_tension(self.tension - 0.1)
        elif kind == "bad":
            self.update_emotion(self.emotion + 0.2)
            self.update_tension(self.tension + 0.2)
        self.transition()

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
        prefix = ""
        if self.emotion > 0.5:
            prefix = "Z veliko strastjo, "
        elif self.emotion < 0.2:
            prefix = "Mirno, "

        if self.state == "Ego":
            core = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            core = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            core = "Vse resnice so eno, medsebojno povezane."
        return prefix + core
