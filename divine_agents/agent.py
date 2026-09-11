class Agent:
    """Ontological agent capable of transitioning and creating new phases."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.new_boxes = []

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity, adjust tension and check for extremes."""
        self.emotion = value
        self.tension = max(0.0, min(1.0, self.tension + value))
        if self.emotion > 0.8 and "Extreme Emotion Box" not in self.new_boxes:
            self.create_new_box("Extreme Emotion Box")
        if self.tension > 0.8 and "High Tension Box" not in self.new_boxes:
            self.create_new_box("High Tension Box")

    def update_tension(self, value: float) -> None:
        """Directly set tension level and create a new box if extreme."""
        self.tension = max(0.0, min(1.0, value))
        if self.tension > 0.8 and "High Tension Box" not in self.new_boxes:
            self.create_new_box("High Tension Box")

    def create_new_box(self, box_name: str) -> None:
        """Register a new phase when an extreme threshold is reached."""
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

    def report(self) -> str:
        """Return a summary of current state and any new boxes."""
        boxes = ", ".join(self.new_boxes) if self.new_boxes else "None"
        return f"{self.name} is in {self.state}. New boxes: {boxes}"

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
