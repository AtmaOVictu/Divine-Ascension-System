from .agent import Agent


class ResonanceAgent(Agent):
    """Agent that adjusts state based on tension and emotion changes."""

    def process_stimuli(self, tension_delta: float = 0.0, emotion_delta: float = 0.0) -> str:
        """Update internal metrics and perform state transition."""
        self.update_tension(self.tension + tension_delta)
        self.update_emotion(self.emotion + emotion_delta)
        return self.transition()
