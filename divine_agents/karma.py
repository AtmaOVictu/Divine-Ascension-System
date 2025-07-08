from .emotion import Emotion

class Karma:
    """Simple karma accumulator based on emotions and interactions."""

    def __init__(self, karma_value: float = 0.0):
        self.karma_value = karma_value

    def update(self, emotion: Emotion, agent_state: float = 0.0, emotional_influence: float | None = None) -> float:
        """Update karma based on emotions and optional external influence."""
        if emotional_influence is not None:
            agent_state += emotional_influence

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

        self.karma_value = max(-1.0, min(1.0, self.karma_value))
        return self.karma_value
