"""Core ontology logic for philosophical agents."""


class Agent:
    """Represents an ontological agent capable of transitioning states.

    An agent holds an emotional state and tension level which determine when
    it moves through the ontological phases: ``Ego`` -> ``Jaz`` -> ``Enotnost``.
    State transitions occur only when the emotion or tension cross predefined
    thresholds.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        """Create a new agent.

        Parameters
        ----------
        name:
            Human readable identifier of the agent.
        state:
            Starting ontological phase.
        tension:
            Initial tension level. High tension may trigger a transition.
        emotion:
            Initial emotional intensity which also contributes to transitions.
        """
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update the emotional intensity of the agent.

        The emotion level directly contributes to internal tension which may
        trigger a state transition on the next call to :py:meth:`transition`.
        """
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set the tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform a state transition when thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the current state and emotion."""
        intense = self.emotion > 0.7

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
            return base if not intense else f"{base} Čutim močno potrebo po obrambi te resnice."

        if self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
            return base if not intense else f"{base} Naša čustva to še poudarjajo."

        base = "Vse resnice so eno, medsebojno povezane."
        return base if not intense else f"{base} To začutim v globini svojega bitja."
