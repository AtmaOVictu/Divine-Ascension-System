"""Agent module for ontological state management and dialogue."""


class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Name of the agent.
    state:
        Initial ontological state (``Ego`` by default).
    tension:
        Initial tension level.
    emotion:
        Initial emotion intensity.
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
        # Emotions feed into tension which may trigger a transition
        self.tension += value

    def decay_tension(self, stimulus: float = 1.0, base_rate: float = 0.1) -> None:
        r"""Gradually reduce tension based on external stimulus.

        The decay follows an exponential function :math:`T = T * e^{-\lambda f(S)}`
        where ``base_rate`` represents ``\lambda`` and ``stimulus`` corresponds
        to ``f(S)``.
        """
        import math

        decay_factor = math.exp(-base_rate * stimulus)
        self.tension *= decay_factor

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = max(0.0, value)

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
        """Return a philosophical answer influenced by state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.5:
            base += " Čutim močna čustva, ki oblikujejo moj odgovor."
        return base
