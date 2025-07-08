from .emotion import Emotion

class Karma:
    """Simple karma system influenced by emotions."""

    def __init__(self, karma_value: float = 0.0) -> None:
        self.karma_value = karma_value

    def update(self, emotion: Emotion, agent_state: list[list[float]], emotional_influence: float | None = None) -> float:
        """Update karma based on emotional state and influence."""
        if emotional_influence is not None:
            for row in agent_state:
                for i, _ in enumerate(row):
                    row[i] += emotional_influence

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

        self.karma_value = max(min(self.karma_value, 1), -1)
        return self.karma_value
