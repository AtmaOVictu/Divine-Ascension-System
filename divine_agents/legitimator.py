class Legitimator:
    """Validate and perform state transitions based on ontological principles."""

    tension_threshold = 0.7
    emotion_threshold = 0.5

    @staticmethod
    def is_legitimate(agent) -> bool:
        """Return True if the agent meets conditions for a legitimate transition."""
        return (
            agent.tension > Legitimator.tension_threshold
            or agent.emotion > Legitimator.emotion_threshold
        )

    @staticmethod
    def next_state(state: str) -> str:
        """Return the next state in the ontological hierarchy."""
        if state == "Ego":
            return "Jaz"
        if state == "Jaz":
            return "Enotnost"
        return state

    @classmethod
    def transition(cls, agent, force: bool = False) -> str:
        """Transition agent to the next state if legitimate or if forced."""
        if cls.is_legitimate(agent) or force:
            agent.state = cls.next_state(agent.state)
        agent.history.append(agent.state)
        return agent.state
