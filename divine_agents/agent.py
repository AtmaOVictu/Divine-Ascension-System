class Agent:
    """Represents an ontological agent capable of transitioning states.

    Attributes
    ----------
    name: str
        Agent identifier.
    state: str
        Current ontological state.
    tension: float
        Current tension value on ``0-1`` scale.
    emotion: float
        Current emotion value on ``0-1`` scale.
    history: List[str]
        History of states agent transitioned through.
    new_boxes: List[str]
        Dynamically created phases triggered by extreme values.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.new_boxes = []

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly.

        A new box is created when ``emotion`` exceeds ``0.8``.
        """
        self.emotion = max(0.0, min(1.0, value))
        self.tension = max(0.0, min(1.0, self.tension + self.emotion))
        if self.emotion > 0.8 and "Extreme Emotion Box" not in self.new_boxes:
            self.create_new_box("Extreme Emotion Box")

    def update_tension(self, value: float) -> None:
        """Directly set tension level.

        A new box is created when ``tension`` exceeds ``0.8``.
        """
        self.tension = max(0.0, min(1.0, value))
        if self.tension > 0.8 and "High Tension Box" not in self.new_boxes:
            self.create_new_box("High Tension Box")

    def create_new_box(self, box_name: str) -> None:
        """Register a new phase triggered by extreme values."""
        self.new_boxes.append(box_name)

    def transition(self) -> str:
        """Perform state transition when thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        emotion_note = "" if self.emotion <= 0.5 else " (čustveno nabito)"
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih." + emotion_note
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi." + emotion_note
        return "Vse resnice so eno, medsebojno povezane." + emotion_note
