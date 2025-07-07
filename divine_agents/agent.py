"""Agent module defining stateful ontological actors.

This module contains the :class:`Agent` class used throughout the project.
Agents manage emotional and tension values while progressing through the
ontological phases ``Ego``, ``Jaz`` and ``Enotnost``.  State transitions occur
when emotion or tension rise above specific thresholds.
"""


class Agent:
    """Represents an ontological agent capable of transitioning states.

    Each agent tracks its current state, emotional intensity and tension.
    When either emotion or tension exceed predefined limits the agent will
    evolve to the next philosophical state as described in the specification.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Set the agent's emotional state and propagate tension changes.

        Emotion influences tension directly in this simplified model.
        Increasing emotion will raise tension by the same amount which may
        trigger a state transition on the next call to :meth:`transition`.
        """
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level without modifying emotion."""
        self.tension = value

    def transition(self) -> str:
        """Advance to the next philosophical state when thresholds are met.

        The agent progresses from ``Ego`` to ``Jaz`` and finally ``Enotnost``
        when either the ``tension`` value exceeds ``0.7`` or the ``emotion``
        value exceeds ``0.5``.  The resulting state is appended to the history
        and returned to the caller.
        """
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical statement reflecting the current state.

        The response embodies the principle associated with the agent's
        ontological phase:

        - ``Ego``: truth is absolute and self-contained
        - ``Jaz``: truth is relative and relationship-driven
        - ``Enotnost``: truth is unified across all things
        """
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
