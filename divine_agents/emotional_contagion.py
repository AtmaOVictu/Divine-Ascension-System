class EmotionalContagion:
    """Handle emotional influence between agents."""

    def __init__(self) -> None:
        self.agents = []

    def add_agent(self, agent: 'Agent') -> None:
        """Add an agent to the contagion network."""
        self.agents.append(agent)

    def spread_emotion(self, agent_index: int, emotion_influence: float) -> None:
        """Spread emotion from one agent to all others."""
        source = self.agents[agent_index]
        for idx, other in enumerate(self.agents):
            if idx == agent_index:
                continue
            other.update_emotion(source.emotion + emotion_influence)
            print(f"{other.name} čuti vpliv čustva od {source.name}, novo čustvo: {other.emotion}")
