class Agent:
    """Ontological agent that can transition between philosophical states."""

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

    def is_transition_due(self) -> bool:
        """Return ``True`` if emotion or tension exceed transition thresholds."""
        return self.tension > 0.7 or self.emotion > 0.5

    def transition(self) -> str:
        """Perform state transition when :py:meth:`is_transition_due` is ``True``."""
        if self.is_transition_due():
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the current emotion."""
        base = self.generate_base_response()
        feedback = self.generate_emotional_feedback() if self.emotion > 0.3 else ""
        return f"{base} {feedback}".strip()

    def generate_base_response(self) -> str:
        """Generate the philosophical statement for the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def generate_emotional_feedback(self) -> str:
        """Return a textual description of the agent's emotions."""
        if self.emotion > 0.7:
            return "Močno čustvujem."
        return "Čustva rahlo vplivajo na moj odgovor."
