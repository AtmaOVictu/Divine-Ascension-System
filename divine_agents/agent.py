class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.potential_changes = []

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self.record_potential_change(f"emotion->{value:.2f}")

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.record_potential_change(f"tension->{value:.2f}")

    def record_potential_change(self, change: str) -> None:
        """Record dynamic changes similar to a hexdump trace."""
        self.potential_changes.append(change)

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        self.record_potential_change(f"transition->{self.state}")
        return self.state

    def get_history(self):
        """Return enumerated state history."""
        return list(enumerate(self.history))

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.8:
            tone = " Jezen se odzivam."  # angry tone
        elif self.emotion > 0.5:
            tone = " Čustveno razmišljam."  # emotional tone
        else:
            tone = ""
        return base + tone

