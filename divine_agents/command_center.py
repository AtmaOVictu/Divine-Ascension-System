class CommandCenter:
    """Simple coordinator that handles upward and downward commands."""

    def __init__(self):
        self.log = []

    def receive_from_agent(self, agent, message: str) -> None:
        """Record a message from an agent (upward command transfer)."""
        self.log.append(f"{agent.name}:{message}")

    def send_command(self, agent, command: str) -> None:
        """Send a command downward to an agent."""
        agent.receive_instruction(command)
        self.log.append(f"to {agent.name}:{command}")
