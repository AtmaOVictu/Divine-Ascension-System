import math
from .agent import Agent

class EmotionCycleAgent(Agent):
    """Agent with cyclical emotional behavior."""

    def __init__(self, name: str, frequency: float = 1.0, amplitude: float = 1.0,
                 phase_shift: float = 0.0, **kwargs):
        super().__init__(name, **kwargs)
        self.frequency = frequency
        self.amplitude = amplitude
        self.phase_shift = phase_shift
        self.time = 0.0

    def emotion_cycle(self) -> float:
        """Generate current emotion based on a sinusoidal cycle."""
        return self.amplitude * math.sin(2 * math.pi * self.frequency * self.time + self.phase_shift)

    def step(self, external_input: float = 0.0) -> None:
        """Advance the emotional cycle and update state."""
        emotion_value = self.emotion_cycle() + external_input
        self.update_emotion(emotion_value)
        self.transition()
        self.time += 0.1
