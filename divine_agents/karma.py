def _clip(value: float, min_value: float, max_value: float) -> float:
    return max(min(value, max_value), min_value)

class Karma:
    """Represents karma accumulation influenced by emotions and group dynamics."""

    def __init__(self, karma_value: float = 0.0):
        self.karma_value = karma_value

    def update(self, emotion, agent_state, emotional_influence=None):
        """Update karma based on emotional state and group influence."""
        if emotional_influence is not None:
            agent_state += emotional_influence

        if getattr(emotion, "anger", 0) > 0.8:
            self.karma_value -= 0.1
        elif getattr(emotion, "fear", 0) > 0.8:
            self.karma_value += 0.05
        elif getattr(emotion, "joy", 0) > 0.8:
            self.karma_value += 0.1
        elif getattr(emotion, "guilt", 0) > 0.8:
            self.karma_value -= 0.05
        elif getattr(emotion, "hope", 0) > 0.8:
            self.karma_value += 0.1
        elif getattr(emotion, "pride", 0) > 0.8:
            self.karma_value -= 0.1
        elif getattr(emotion, "despair", 0) > 0.8:
            self.karma_value -= 0.05

        self.karma_value = float(_clip(self.karma_value, -1.0, 1.0))
        return self.karma_value
