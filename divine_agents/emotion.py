class Emotion:
    """Represents an agent's emotional makeup and transitions."""

    def __init__(self, joy=0.0, anger=0.0, fear=0.0, sadness=0.0,
                 guilt=0.0, hope=0.0, pride=0.0, despair=0.0,
                 regret=0.0, compassion=0.0, envy=0.0, trust=0.0):
        self.joy = joy
        self.anger = anger
        self.fear = fear
        self.sadness = sadness
        self.guilt = guilt
        self.hope = hope
        self.pride = pride
        self.despair = despair
        self.regret = regret
        self.compassion = compassion
        self.envy = envy
        self.trust = trust

    def transition(self):
        """Apply recovery transitions between emotional states."""
        if self.despair > 0.8:
            self.hope = min(1.0, self.hope + 0.4)
            self.despair = max(0.0, self.despair - 0.2)
        elif self.regret > 0.8:
            self.hope = min(1.0, self.hope + 0.2)
            self.regret = max(0.0, self.regret - 0.2)
        elif self.sadness > 0.8:
            self.compassion = min(1.0, self.compassion + 0.3)
            self.sadness = max(0.0, self.sadness - 0.2)
