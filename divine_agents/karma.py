class Karma:
    """Track karma accumulation over time."""

    def __init__(self, karma_value=0.0):
        self.karma_value = karma_value
        self.karma_history = []

    def update(self, emotion, agent_state=None, emotional_influence=None):
        if emotional_influence is not None:
            self.karma_value += emotional_influence

        if emotion.anger > 0.8:
            self.karma_value -= 0.1
        elif emotion.fear > 0.8:
            self.karma_value += 0.05
        elif emotion.joy > 0.8:
            self.karma_value += 0.1
        elif emotion.regret > 0.8:
            self.karma_value -= 0.15
        elif emotion.compassion > 0.8:
            self.karma_value += 0.2

        self.karma_history.append(self.karma_value)
        if self.karma_value > 1:
            self.karma_value = 1
        elif self.karma_value < -1:
            self.karma_value = -1
        return self.karma_value

    def track_karma_over_time(self):
        return self.karma_history
