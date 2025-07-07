class ShortEgoRecorder:
    """Recorder tracking transitions and limitations of agents."""

    def __init__(self):
        self.records = []
        self.limitations = []

    def record_transition(self, agent, new_state: str) -> None:
        """Record a transition from agent.state to new_state with context."""
        info = {
            "state_from": agent.state,
            "state_to": new_state,
            "emotion": agent.emotion,
            "tension": agent.tension,
            "transition_time": agent.transition_time(),
        }
        self.records.append(info)
        self._check_limitations(agent, new_state)

    def _check_limitations(self, agent, new_state: str) -> None:
        """Capture reasons an agent might be unable to reach broader states."""
        if new_state == "Jaz" and agent.tension < 0.5:
            self.limitations.append(
                f"Agent {agent.name} is limited by low tension to move to Jaz."
            )
        elif new_state == "Ego" and agent.emotion < 0.3:
            self.limitations.append(
                f"Agent {agent.name} cannot transcend to broader states due to low emotion."
            )

    def get_records(self):
        return self.records

    def get_limitations(self):
        return self.limitations
