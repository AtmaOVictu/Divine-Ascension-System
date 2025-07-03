from .agent import Agent


class ResonanceAgent(Agent):
    """Agent with resonance-based emotional transitions."""

    def resonance_transition(self) -> str:
        return super().resonance_transition()
