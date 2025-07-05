class EmotionSystem:
    """Manage emotional state and derive tension."""

    def __init__(self, initial_emotion: float = 0.0, tension: float = 0.0):
        self.emotion = initial_emotion
        self.tension = tension

    def update_emotion(self, value: float) -> None:
        """Update emotion and adjust tension."""
        self.emotion = value
        # Tension increases as emotion intensifies
        self.tension += value
        if self.tension > 1.0:
            self.tension = 1.0

    def set_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = max(0.0, min(1.0, value))

    def reset(self) -> None:
        self.emotion = 0.0
        self.tension = 0.0
