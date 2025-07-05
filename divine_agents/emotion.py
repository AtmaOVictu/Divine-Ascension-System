class EmotionSystem:
    """Manage emotional state of an agent."""

    def __init__(self, emotion: str = "Nevtralno"):
        self.emotion = emotion

    def change_emotion(self, new_emotion: str) -> None:
        """Change the current emotion."""
        self.emotion = new_emotion
