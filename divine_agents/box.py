class IntegrityBox:
    """A box that wraps data and tracks integrity."""

    def __init__(self, name: str, data: dict | None = None):
        self.name = name
        self.data = data if data is not None else {"integrity_status": "valid"}
        self.history = []
        self.protection_flag = False

    def update_data(self, new_data: dict) -> None:
        """Update the data inside the box while storing history."""
        if self.protection_flag:
            raise PermissionError("Box is protected. Cannot modify data.")
        self.history.append(self.data.copy())
        self.data.update(new_data)

    def set_protection(self, flag: bool) -> None:
        """Toggle protection on the box."""
        self.protection_flag = flag

    def transition(self, new_data: dict) -> None:
        """Transition to a new state with integrity validation."""
        if self.protection_flag:
            raise PermissionError("Box is protected. Cannot transition.")
        self.update_data(new_data)

    def check_integrity(self) -> str:
        """Return the current integrity status."""
        return self.data.get("integrity_status", "unknown")

    def __str__(self) -> str:
        return f"Box for {self.name} with data: {self.data} and protection: {self.protection_flag}"


from .agent import Agent


class AgentBox(IntegrityBox):
    """Specialised box that wraps an Agent and logs state changes."""

    def __init__(self, agent: Agent):
        super().__init__(
            name=agent.name,
            data={
                "state": agent.state,
                "tension": agent.tension,
                "emotion": agent.emotion,
                "integrity_status": "valid",
            },
        )
        self.agent = agent

    def update_agent(self, tension: float | None = None, emotion: float | None = None) -> None:
        """Update the underlying agent and record the change."""
        if self.protection_flag:
            raise PermissionError("Box is protected. Cannot modify agent.")
        if tension is not None:
            self.agent.update_tension(tension)
        if emotion is not None:
            self.agent.update_emotion(emotion)
        self.transition({"state": self.agent.state, "tension": self.agent.tension, "emotion": self.agent.emotion})

    def transition_agent(self) -> str:
        """Perform agent state transition and log the outcome."""
        if self.protection_flag:
            raise PermissionError("Box is protected. Cannot transition agent.")
        new_state = self.agent.transition()
        self.transition({"state": self.agent.state, "tension": self.agent.tension, "emotion": self.agent.emotion})
        return new_state
