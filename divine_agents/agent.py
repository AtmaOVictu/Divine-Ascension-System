"""Core logic for ontological agents and their state transitions."""


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")
    THRESHOLD_TENSION = 0.7
    THRESHOLD_EMOTION = 0.5

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        # higher emotion increases overall tension
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > self.THRESHOLD_TENSION or self.emotion > self.THRESHOLD_EMOTION:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the agent's state and emotion."""
        if self.emotion > 0.7:
            prefix = "Mo\u010dno \u010ditim, da "
        elif self.emotion > 0.4:
            prefix = "Menim, da "
        else:
            prefix = "Verjamem, da "

        if self.state == "Ego":
            msg = "resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            msg = "resnica je relativna, oblikovana z na\u0161imi odnosi."
        else:
            msg = "vse resnice so eno, medsebojno povezane."
        return prefix + msg
