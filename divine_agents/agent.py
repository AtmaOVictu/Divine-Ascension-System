"""Core logic for ontological agents.

Agents exist in one of three philosophical states: ``Ego``,
``Jaz`` or ``Enotnost``.  Each state reflects a different view on truth:

``Ego``
    Truth is absolute and independent of others.

``Jaz``
    Truth is relative and shaped through relationships.

``Enotnost``
    All truths are one and interconnected.

Agents carry ``emotion`` and ``tension`` values influencing state
transitions. A transition from ``Ego`` to ``Jaz`` or ``Jaz`` to
``Enotnost`` occurs when ``tension`` exceeds ``0.7`` or ``emotion``
exceeds ``0.5``.
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

    def interact(self, other: "Agent", intensity: float) -> str:
        """Interact with another agent.

        Parameters
        ----------
        other:
            The agent being interacted with.
        intensity:
            Strength of the interaction which increases this agent's
            emotional level and therefore tension.

        Returns
        -------
        str
            A response string reflecting the agent's current state after
            the interaction.
        """

        self.update_emotion(self.emotion + intensity)
        new_state = self.transition()
        return self.respond("Kaj je resnica?")

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
        if self.state == "Ego":
            msg = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            msg = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            msg = "Vse resnice so eno, medsebojno povezane."
        if self.emotion > 0.5:
            msg += f" (čustveni nivo: {self.emotion:.2f})"
        return msg
