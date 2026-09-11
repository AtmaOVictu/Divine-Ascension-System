from typing import List, Optional


class Agent:
    """Represents an ontological agent capable of transitioning states.

    The agent tracks its emotional intensity and tension levels. When either
    value reaches an extreme (above ``0.8``), a new "box" (phase) is created
    that reflects the agent entering a new behavioural state.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0):
        self.name: str = name
        self.state: str = state
        self.tension: float = tension
        self.emotion: float = emotion
        self.history: List[str] = [state]
        self.new_boxes: List[str] = []

    def update_emotion(self, value: float) -> Optional[str]:
        """Update emotion intensity and adjust tension accordingly.

        If the updated emotion exceeds ``0.8`` a new phase is created.
        """
        self.emotion = max(0.0, min(1.0, value))
        self.tension = max(0.0, min(1.0, self.tension + value))
        if self.emotion > 0.8 and "Extreme Emotion Box" not in self.new_boxes:
            return self.create_new_box("Extreme Emotion Box")
        return None

    def update_tension(self, value: float) -> Optional[str]:
        """Directly set tension level and create a new phase if extreme."""
        self.tension = max(0.0, min(1.0, value))
        if self.tension > 0.8 and "High Tension Box" not in self.new_boxes:
            return self.create_new_box("High Tension Box")
        return None

    def create_new_box(self, box_name: str) -> str:
        """Register a new box and return a report string."""
        self.new_boxes.append(box_name)
        return f"{self.name} has entered a new phase: {box_name}"

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
