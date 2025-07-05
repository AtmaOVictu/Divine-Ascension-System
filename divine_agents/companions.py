class ShadowAgent:
    """Represents the shadow aspect of an agent."""

    def interact(self, agent: "Agent") -> str:
        """Increase the agent's tension when confronting their shadow."""
        agent.update_tension(min(1.0, agent.tension + 0.2))
        return f"{agent.name} se soo\u010da s svojo senco."


class AngelAgent:
    """Represents the angelic aspect of an agent."""

    def interact(self, agent: "Agent") -> str:
        """Increase the agent's emotion when inspired by the angelic side."""
        agent.update_emotion(min(1.0, agent.emotion + 0.2))
        return f"{agent.name} prejema navdih angelne strani."
