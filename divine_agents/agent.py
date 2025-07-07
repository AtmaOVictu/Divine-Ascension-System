"""Basic ontological agent implementation."""


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    # ------------------------------------------------------------------
    # Updaters
    # ------------------------------------------------------------------
    def update_emotion(self, delta: float) -> None:
        """Adjust emotion and consequently increase tension."""
        self.emotion = max(0.0, min(1.0, self.emotion + delta))
        self.tension = max(0.0, min(1.0, self.tension + abs(delta)))

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = max(0.0, min(1.0, value))

    # ------------------------------------------------------------------
    # Transitions
    # ------------------------------------------------------------------
    def can_transition(self) -> bool:
        """Return ``True`` if thresholds for transition are exceeded."""
        return self.tension > 0.7 or self.emotion > 0.5

    def transition(self) -> str:
        """Perform state transition if allowed."""
        if self.can_transition():
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    # ------------------------------------------------------------------
    # Responses
    # ------------------------------------------------------------------
    def philosophical_principle(self) -> str:
        """Return the philosophical statement for the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by emotion."""
        base = self.philosophical_principle()
        if self.emotion > 0.5:
            return f"{base} Čutim močna čustva glede tega."
        return base

