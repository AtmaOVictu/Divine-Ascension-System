class Agent:
    """A philosophical agent that evolves through emotional tension.

    Each agent inhabits one of three **ontological states** which represent a
    different view on truth:

    ``Ego``
        Truth is absolute and independent of others.
    ``Jaz``
        Truth is relative and shaped by relationships and interactions.
    ``Enotnost``
        All truths are unified and interconnected; separation is an illusion.

    Agents store an emotion intensity and a tension level. When either the
    tension exceeds ``0.7`` or the emotion exceeds ``0.5`` a state transition is
    triggered in the order ``Ego → Jaz → Enotnost``. Every visited state is
    appended to :pyattr:`history`.

    Example
    -------
    >>> a = Agent("Ada")
    >>> a.update_emotion(0.8)
    >>> a.transition()
    'Jaz'
    >>> a.respond("Kaj je resnica?")
    'Resnica je relativna, oblikovana z našimi odnosi.'
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Set a new emotion level and increase tension.

        Parameters
        ----------
        value:
            New emotion intensity in the ``0.0-1.0`` range.

        Updating emotion also increments :pyattr:`tension` by the same amount,
        making a future state transition more likely.
        """
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set the current tension level."""
        self.tension = value

    def transition(self) -> str:
        """Trigger a state change when tension or emotion is high enough.

        Returns
        -------
        str
            The agent's new state after evaluating the thresholds.

        A transition occurs when ``tension > 0.7`` or ``emotion > 0.5``.
        ``Ego`` evolves to ``Jaz`` and ``Jaz`` evolves to ``Enotnost``. The
        resulting state is appended to :pyattr:`history` and returned.
        """
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical statement about truth.

        Parameters
        ----------
        question:
            Ignored in this simplified example but included for API symmetry.

        Returns
        -------
        str
            The agent's view of truth according to its current state.
        """
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
