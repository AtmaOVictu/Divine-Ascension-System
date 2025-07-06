class Agent:
    """Represents an ontological agent capable of transitioning states.

    The agent can recognise problems (``desire``) and attempt to resolve them
    through state transitions influenced by ``emotion`` and ``tension`` levels.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.desire: str | None = None
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    # ------------------------------------------------------------------
    # Problem handling helpers
    # ------------------------------------------------------------------

    def zaznaj_problem(self, problem: str) -> None:
        """Store the problem as the agent's current desire."""
        self.desire = problem
        self.history.append(f"Prepoznan problem: {problem}")

    def resi_problem(self) -> None:
        """Attempt to resolve the recognised problem via a state transition."""
        if not self.desire:
            self.history.append("Ni problema za reševanje.")
            return

        # Increase emotion to trigger possible transition
        self.update_emotion(0.6)
        previous_state = self.state
        self.transition()
        self.history.append(
            f"Prehod iz {previous_state} v {self.state}, da reši problem: {self.desire}"
        )

        if self.state == "Enotnost":
            self.history.append(f"{self.name} doseže rešitev v Enotnosti.")
            self.desire = None

    def hrepeni_po_resitvi(self) -> None:
        """Record the agent's yearning for a solution."""
        if self.desire:
            self.history.append(
                f"Želja po rešitvi '{self.desire}' sproži iskanje v stanju {self.state}."
            )

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

    def pokazi_zgodovino(self) -> list[str]:
        """Return the recorded history of actions."""
        return self.history

    def dialog(self, drugi_agent: "Agent") -> None:
        """Simulate a simple dialogue affecting both agents."""
        self.hrepeni_po_resitvi()
        drugi_agent.hrepeni_po_resitvi()
