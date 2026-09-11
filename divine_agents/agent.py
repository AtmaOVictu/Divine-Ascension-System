class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")
    EXTREME_TENSION_BOX = "High Tension Box"
    EXTREME_EMOTION_BOX = "Extreme Emotion Box"

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.new_boxes = []

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension = min(1.0, self.tension + value)
        if self.emotion > 0.8:
            self.create_new_box(self.EXTREME_EMOTION_BOX)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = min(1.0, value)
        if self.tension > 0.8:
            self.create_new_box(self.EXTREME_TENSION_BOX)

    def create_new_box(self, name: str) -> None:
        """Add a new box representing an extreme condition."""
        if name not in self.new_boxes:
            self.new_boxes.append(name)

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
            answer = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            answer = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            answer = "Vse resnice so eno, medsebojno povezane."

        if self.new_boxes:
            answer += f" (Nova faza: {', '.join(self.new_boxes)})"
        return answer
