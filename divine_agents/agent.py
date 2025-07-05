class Agent:
    """Represents an ontological agent capable of transitioning states.

    Attributes
    ----------
    name: str
        Agent's identifier.
    state: str
        Current ontological state (``Ego``, ``Jaz``, ``Enotnost``).
    tension: float
        Current tension level influencing transitions.
    emotion: float
        Emotional intensity influencing transitions and dialogue tone.
    history: list[str]
        Log of state changes for the agent.
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

    def philosophical_principle(self) -> str:
        """Return the philosophical principle for the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by emotion."""
        if self.emotion > 0.8:
            prefix = "Strastno odgovarjam:" 
        elif self.emotion > 0.5:
            prefix = "Čustveno pravim:" 
        else:
            prefix = "Mirno razlagam:" 
        return f"{prefix} {self.philosophical_principle()}"

    def __repr__(self) -> str:
        return f"Agent(name={self.name!r}, state={self.state!r}, emotion={self.emotion}, tension={self.tension})"
