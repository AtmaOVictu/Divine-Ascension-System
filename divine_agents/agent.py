import random
from typing import List, Optional


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")
    ACTIONS = ["Help", "Hurt", "Explore", "Conquer", "Reflect"]

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        numerology_number: Optional[int] = None,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.numerology_number = numerology_number
        self.history: List[str] = [state]

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
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    # Numerology related functionality ----------------------------------

    def generate_numerology_influence(self) -> str:
        """Return an action influenced by the agent's numerology number."""
        if self.numerology_number == 1:
            return self.ACTIONS[0]  # Help
        if self.numerology_number == 2:
            return self.ACTIONS[1]  # Hurt
        if self.numerology_number == 3:
            return self.ACTIONS[2]  # Explore
        return random.choice(self.ACTIONS)

    def perform_action(self) -> str:
        """Select and return an action based on numerology influence."""
        return self.generate_numerology_influence()
