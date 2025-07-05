class Agent:
    """Dynamic participant with emotional and ontological attributes.

    An ``Agent`` models a conversational entity that moves through the
    ontological phases **Ego**, **Jaz**, and **Enotnost**. Each phase embodies a
    distinct philosophical view of truth:

    - ``Ego`` – truth is absolute and self-contained.
    - ``Jaz`` – truth is relative and informed by relationships.
    - ``Enotnost`` – all truths form a unified whole.

    The agent tracks ``tension`` and ``emotion`` values. When ``tension``
    exceeds ``0.7`` or ``emotion`` surpasses ``0.5``, the agent transitions to
    the next state. ``update_emotion`` influences both ``emotion`` and
    ``tension`` to reflect heightened feelings during dialogue.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and increase tension accordingly.

        Heightened emotions raise an agent's ``tension`` level, making state
        transitions more likely during dialogue.
        """
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly assign a new tension level independent of emotion."""
        self.tension = value

    def transition(self) -> str:
        """Move to the next ontological phase when thresholds are exceeded.

        If ``tension`` is greater than ``0.7`` or ``emotion`` exceeds ``0.5``,
        the agent progresses from ``Ego`` → ``Jaz`` → ``Enotnost``. The chosen
        state is appended to ``history`` and returned.
        """
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer reflecting the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
