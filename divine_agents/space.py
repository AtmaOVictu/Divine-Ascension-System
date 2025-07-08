class Space:
    """Manage basic agent location information."""

    def __init__(self) -> None:
        self.locations = {}

    def set_location(self, agent_name: str, location: str) -> None:
        """Set the current location for an agent."""
        self.locations[agent_name] = location

    def get_location(self, agent_name: str) -> str:
        """Get an agent's location, defaulting to 'neznano'."""
        return self.locations.get(agent_name, "neznano")
