class Krak:
    """Represents a task (krak) that activates when conditions are met."""

    def __init__(self, name: str, condition: str):
        self.name = name
        self.condition = condition
        self.completed = False

    def check_condition(self, agent) -> bool:
        """Return True if the krak's activation condition is satisfied."""
        if self.condition == "high_emotion":
            return agent.emotion > 0.7
        if self.condition == "state_transition":
            return agent.state in ("Jaz", "Enotnost")
        return False

    def activate(self) -> str:
        """Mark the krak as completed and return an activation message."""
        self.completed = True
        return f"Krak {self.name} completed."
