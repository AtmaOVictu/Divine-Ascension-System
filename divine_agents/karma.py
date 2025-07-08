class Karma:
    """Accumulates karma based on emotional states."""

    def __init__(self, value: float = 0.0) -> None:
        self.karma_value = value

    def update(self, emotion: 'Emotion') -> float:
        """Adjust karma according to dominant emotions."""
        if emotion.anger > 0.8:
            self.karma_value -= 0.1
        elif emotion.fear > 0.8:
            self.karma_value += 0.05
        elif emotion.joy > 0.8:
            self.karma_value += 0.1
        elif emotion.guilt > 0.8:
            self.karma_value -= 0.05
        elif emotion.hope > 0.8:
            self.karma_value += 0.1
        elif emotion.pride > 0.8:
            self.karma_value -= 0.1
        elif emotion.despair > 0.8:
            self.karma_value -= 0.05

        if self.karma_value > 1:
            self.karma_value = 1
        if self.karma_value < -1:
            self.karma_value = -1
        return self.karma_value
