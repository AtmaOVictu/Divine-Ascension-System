class Environment:
    """Represents external factors influencing an agent."""

    def __init__(self, name: str, societal_influence: float = 0.0, natural_condition: float = 0.0):
        self.name = name
        self.societal_influence = societal_influence
        self.natural_condition = natural_condition

    def influence_agent(self, agent: 'Agent') -> None:
        """Adjust the agent's emotional state and tension based on the environment."""
        agent.update_emotion(agent.emotion + self.societal_influence)
        agent.update_tension(agent.tension + self.natural_condition)

