class EmotionHandler:
    """Handles emotional updates and tension levels."""

    def __init__(self, initial_emotion: float = 0.0, initial_tension: float = 0.0) -> None:
        self.emotion = initial_emotion
        self.tension = initial_tension

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension."""
        self.emotion = value
        self.tension += value

    def adjust_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
