class Environment:
    """External context that influences agents via conditions."""

    def __init__(self, name: str, conditions=None):
        self.name = name
        self.conditions = conditions or {}

    def update_condition(self, condition: str, value: float) -> None:
        """Set or update a condition influencing agents."""
        self.conditions[condition] = value

    def influence(self, agent) -> None:
        """Modify agent's emotion or tension based on current conditions."""
        if self.conditions.get("social_pressure", 0) > 0.7:
            agent.update_emotion(0.8)
        if self.conditions.get("moral_dilemma", 0) > 0.5:
            agent.update_tension(0.8)
