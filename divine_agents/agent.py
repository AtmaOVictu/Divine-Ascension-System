class Agent:
    """Represent an ontological agent and its state evolution.

    Each agent exists in one of three states: ``"Ego"``, ``"Jaz"`` or
    ``"Enotnost"``.  The current state is affected by two continuous values,
    ``emotion`` and ``tension``.  When :py:meth:`update_emotion` is called the
    supplied emotion level is stored and also *added* to the agent's tension to
    model how strong feelings raise internal pressure.  Tension may also be
    directly manipulated via :py:meth:`update_tension`.

    State transitions are evaluated in :py:meth:`transition`.  If the agent's
    tension rises above ``0.7`` or its emotion level surpasses ``0.5``, the
    agent progresses to the next state in the order ``Ego → Jaz → Enotnost``.
    Every transition is recorded in ``history`` so that simulations can track
    the agent's philosophical journey.
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
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
