class Emotion:
    """Represents detailed emotional states for an agent."""

    def __init__(self, joy=0.0, anger=0.0, fear=0.0, sadness=0.0,
                 guilt=0.0, hope=0.0, pride=0.0, despair=0.0):
        self.joy = joy
        self.anger = anger
        self.fear = fear
        self.sadness = sadness
        self.guilt = guilt
        self.hope = hope
        self.pride = pride
        self.despair = despair

    def intensity(self) -> float:
        """Return the maximum emotional intensity."""
        return max(
            self.joy,
            self.anger,
            self.fear,
            self.sadness,
            self.guilt,
            self.hope,
            self.pride,
            self.despair,
        )

    def modulate(self, agent_state):
        """Modulate the numerical agent state by emotional influence."""
        emotional_value = (
            (self.joy * 0.3)
            + (self.anger * 0.2)
            - (self.fear * 0.1)
            - (self.sadness * 0.15)
            + (self.guilt * -0.2)
            + (self.hope * 0.25)
            + (self.pride * 0.1)
            + (self.despair * -0.3)
        )
        return agent_state * (1 + emotional_value)
