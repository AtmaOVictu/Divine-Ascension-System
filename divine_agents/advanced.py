"""Advanced components for dynamic agents."""

class SelfRegulation:
    """Simple mechanism to adapt energy based on tension."""
    def __init__(self, energy: float, tension: float):
        self.energy = energy
        self.tension = tension

    def adjust(self) -> None:
        """Adjust energy according to tension."""
        if self.tension > 0.8:
            self.energy *= 0.5
        elif self.tension < 0.2:
            self.energy *= 1.2


class Learning:
    """Store experiences and optimize decisions."""
    def __init__(self):
        self.experiences = []

    def add_experience(self, exp: str) -> None:
        self.experiences.append(exp)

    def optimize(self) -> bool:
        """Return True if enough experiences for optimization."""
        return len(self.experiences) > 5




class EmotionalDynamics:
    """Track and update emotional state."""
    def __init__(self, state: str = "Nevtralno"):
        self.state = state

    def update_state(self, new_state: str) -> None:
        self.state = new_state

    def ethical_warning(self) -> str:
        if self.state == "tesnoba":
            return "Etika opozarja: tesnoba lahko ovira smiselne odločitve."
        return ""
