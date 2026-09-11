import random
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, numerology_number: int | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.numerology_number = numerology_number
        self.fame = 0.0
        self.actions = ["Help", "Hurt", "Explore", "Conquer", "Reflect"]
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

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        if self.emotion > 0.5:
            return base + " Čutim to zelo močno."  # Emotional emphasis
        return base

    # ------------------------------------------------------------------
    # Numerology integration
    # ------------------------------------------------------------------
    def generate_numerology_influence(self) -> str:
        """Generate an action influenced by numerology number."""
        if self.numerology_number == 1:
            return self.actions[0]  # Help
        if self.numerology_number == 2:
            return self.actions[1]  # Hurt
        if self.numerology_number == 3:
            return self.actions[2]  # Explore
        return random.choice(self.actions)

    def perform_action(self) -> str:
        """Perform an action and adjust fame based on the result."""
        action = self.generate_numerology_influence()
        if action == "Help":
            self.fame += 0.1
        elif action == "Hurt":
            self.fame -= 0.1
        return action
