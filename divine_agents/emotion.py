class EmotionHandler:
    """Manage emotion intensity and resulting tension."""

    def __init__(self, initial_emotion: float = 0.0, initial_tension: float = 0.0) -> None:
        self.emotion = initial_emotion
        self.tension = initial_tension

    def update_emotion(self, value: float) -> None:
        """Update emotion and adjust tension."""
        self.emotion = value
        self.tension += value

    def set_tension(self, value: float) -> None:
        """Set tension directly."""
        self.tension = value
