class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self._ready_for_transition = False

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def meditate(self) -> str:
        """Reflect on internal state and decide if transition is needed."""
        self._ready_for_transition = self.tension > 0.7 or self.emotion > 0.5
        if self._ready_for_transition:
            return "Meditacija zaključena: prehod potreben"
        return "Meditacija zaključena: prehod ni potreben"

    def transition(self) -> str:
        """Perform state transition if meditation determined it is needed."""
        if self._ready_for_transition and (self.tension > 0.7 or self.emotion > 0.5):
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        self._ready_for_transition = False
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
