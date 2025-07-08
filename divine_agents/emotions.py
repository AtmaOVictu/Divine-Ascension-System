from typing import Iterable, List


class Emotion:
    """Represents a set of emotional states for an agent."""

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

    def modulate(self, agent_state: Iterable[Iterable[float]]) -> List[List[float]]:
        """Return a modulated agent state based on emotional values."""
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
        factor = 1 + emotional_value
        return [[cell * factor for cell in row] for row in agent_state]
