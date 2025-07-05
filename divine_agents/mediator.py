class Mediator:
    """Coordinate transitions and validate commands for an agent."""

    def __init__(self, agent):
        self.agent = agent

    def validate_command(self, command: str) -> str:
        """Validate and execute supported commands."""
        if command == "prehod":
            return self.check_conditions_for_transition()
        if command == "respond":
            return self.agent.respond("Kaj je resnica?")
        return "Ukaz ni veljaven."

    def check_conditions_for_transition(self) -> str:
        """Check if the agent meets requirements for a state transition."""
        if self.agent.tension > 0.7 or self.agent.emotion > 0.5:
            self.agent.transition()
            return f"Prehod uspešno izveden: {self.agent.state}"
        return "Pogoji za prehod niso izpolnjeni."
