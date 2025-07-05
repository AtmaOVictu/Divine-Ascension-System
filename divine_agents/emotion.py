class EmotionHandler:
    """Manage emotion intensity and tension for an agent."""

    def __init__(self, emotion: float = 0.0, tension: float = 0.0) -> None:
        self.emotion = emotion
        self.tension = tension

    def update_emotion(self, value: float) -> None:
        """Update emotion and increase tension accordingly."""
        self.emotion = value
        self.tension += value

    def set_tension(self, value: float) -> None:
        """Explicitly set tension level."""
        self.tension = value
