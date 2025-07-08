from .emotions import Emotion


class Karma:
    """Accumulates karma based on emotional states."""

    def __init__(self, karma_value: float = 0.0):
        self.karma_value = karma_value

    def update(self, emotion: Emotion, agent_state) -> float:
        """Update karma based on current emotional profile."""
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

        self.karma_value = max(-1, min(self.karma_value, 1))
        return self.karma_value
