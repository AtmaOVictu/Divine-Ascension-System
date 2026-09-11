class Environment:
    """Represents external conditions influencing agents."""

    def __init__(self):
        self.conditions = {}

    def update_condition(self, key: str, value: float) -> None:
        """Set an environmental condition."""
        self.conditions[key] = value

    def influence_agent(self, agent) -> None:
        """Modify agent's emotion and tension based on conditions."""
        if self.conditions.get("social_pressure", 0) > 0.7:
            new_emotion = min(1.0, agent.emotion + 0.1)
            agent.update_emotion(new_emotion)
        if self.conditions.get("moral_dilemma", 0) > 0.5:
            new_tension = min(1.0, agent.tension + 0.2)
            agent.update_tension(new_tension)
