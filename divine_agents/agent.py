"""Ontological agents that shift philosophical states based on emotion and tension.

The module defines a minimal framework for agents engaged in philosophical
dialogue. Each :class:`Agent` begins in one of three states:

``Ego``       - truth is absolute and individual.
``Jaz``       - truth is relative and shaped by relationships.
``Enotnost``  - all truths are unified and interconnected.

Agents transition between these states when either their ``tension`` exceeds
``0.7`` or their ``emotion`` rises above ``0.5``. Updating ``emotion`` directly
increases ``tension``, making transitions more likely.
"""


class Agent:
    """Represent an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        """Create a new agent.

        Parameters
        ----------
        name: str
            Identifier for the agent.
        state: str, optional
            Starting ontological state. Defaults to ``"Ego"``.
        tension: float, optional
            Initial tension level.
        emotion: float, optional
            Initial emotional intensity.
        """
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Set ``emotion`` and increase ``tension`` by the same amount.

        Parameters
        ----------
        value: float
            New emotional intensity.
        """
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set the agent's ``tension``.

        Parameters
        ----------
        value: float
            New tension level.
        """
        self.tension = value

    def transition(self) -> str:
        """Move the agent to the next state when thresholds are met.

        Returns
        -------
        str
            The new ontological state after transition.
        """
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Answer a question based on the current state.

        Parameters
        ----------
        question: str
            The prompt to respond to.

        Returns
        -------
        str
            Text reflecting the agent's philosophical stance.
        """
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
