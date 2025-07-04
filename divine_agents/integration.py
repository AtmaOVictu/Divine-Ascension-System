class ExternalIntegrationLayer:
    """Simple layer for storing and retrieving external data."""

    def __init__(self):
        self.external_data = {}

    def add_data(self, data_key: str, data_value: str) -> None:
        """Add data from the external world."""
        self.external_data[data_key] = data_value

    def get_data(self, data_key: str):
        """Retrieve data from the external world."""
        return self.external_data.get(data_key)


class CodeX:
    """Log all state transitions performed by agents."""

    def __init__(self):
        self.transitions = []

    def log_transition(self, agent_name: str, from_state: str, to_state: str) -> None:
        self.transitions.append((agent_name, from_state, to_state))

    def review_transitions(self):
        return list(self.transitions)

