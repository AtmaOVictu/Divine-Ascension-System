from typing import List


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.new_boxes: List[str] = []  # stores names of phases entered due to extreme values

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        if self.emotion > 0.8 and "Extreme Emotion Box" not in self.new_boxes:
            self.create_new_box("Extreme Emotion Box")
        if self.tension > 0.8 and "High Tension Box" not in self.new_boxes:
            self.create_new_box("High Tension Box")

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        if self.tension > 0.8 and "High Tension Box" not in self.new_boxes:
            self.create_new_box("High Tension Box")

    def create_new_box(self, box_name: str) -> None:
        """Register entry into a new phase triggered by an extreme value."""
        self.new_boxes.append(box_name)

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
