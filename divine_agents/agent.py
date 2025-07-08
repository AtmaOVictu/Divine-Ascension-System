class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Name of the agent.
    state:
        Initial ontological state, defaults to ``"Ego"``.
    tension:
        Initial tension level.
    emotion:
        Initial emotion intensity.
    parent:
        Optional parent :class:`Agent` from which to inherit beliefs and emotion.
    beliefs:
        Optional list of beliefs held by the agent.  Defaults to an empty list.

    When ``parent`` is supplied the agent automatically calls
    :meth:`inherit_from_parent` to copy the parent's beliefs and emotion.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, *, parent: "Agent | None" = None,
                 beliefs: list[str] | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.beliefs = beliefs[:] if beliefs else []
        self.parent: Agent | None = parent
        self.children: list[Agent] = []
        if parent is not None:
            parent.children.append(self)
            self.inherit_from_parent()

    def inherit_from_parent(self) -> None:
        """Copy parent's beliefs and emotion into this agent."""
        if self.parent is None:
            return
        # copy beliefs and emotion
        self.beliefs = self.parent.beliefs[:]
        self.emotion = self.parent.emotion

    def create_child(self, name: str) -> "Agent":
        """Create a new child agent linked to this agent."""
        return Agent(name, parent=self)

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
