class Agent:
    """Ontological agent capable of state transitions based on emotions.

    Parameters
    ----------
    name:
        Agent identifier.
    state:
        Initial ontological state.
    tension:
        Initial tension value.
    emotion:
        Initial emotion intensity.
    emotional_state:
        Current emotion descriptor (e.g. ``fear`` or ``joy``).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotional_state: str = "neutral") -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotional_state = emotional_state
        self.history = [state]

    def update_emotion(self, emotion: str, intensity: float) -> None:
        """Set emotional state and update tension accordingly."""
        self.emotional_state = emotion
        self.emotion = intensity
        self.tension += intensity

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

    def interact(self, other: "Agent") -> None:
        """Adjust emotion based on interaction with another agent."""
        if self.state != other.state:
            self.update_emotion("anger", 0.6)
        else:
            self.update_emotion("joy", 0.2)

    def _base_response(self) -> str:
        """Return the philosophical principle for the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by emotion."""
        base = self._base_response()
        if self.emotion > 0.5:
            return f"({self.emotional_state}) {base}"
        return base
