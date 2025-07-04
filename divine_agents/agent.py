"""Core building blocks for the ontological agent system."""


class Agent:
    """Agent capable of transitioning between ontological states.

    The agent moves from ``Ego`` to ``Jaz`` and from ``Jaz`` to ``Enotnost``
    when either its tension rises above ``0.7`` or its emotional intensity rises
    above ``0.5``. Each state reflects a different view on truth:

    * ``Ego``      -- truth is absolute and independent of others
    * ``Jaz``      -- truth is relative and shaped through relations
    * ``Enotnost`` -- all truths are unified and interconnected
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        """Create a new agent.

        Parameters
        ----------
        name:
            Agent identifier used in dialogues.
        state:
            Initial ontological state, defaults to ``Ego``.
        tension:
            Current level of tension within the agent.
        emotion:
            Current emotional intensity of the agent.
        """
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Set emotional level and increase tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly assign a tension level."""
        self.tension = value

    def transition(self) -> str:
        """Move to the next state if emotional or tension thresholds are met."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer according to the agent's state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
