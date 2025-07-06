class DataHarvester:
    """Collects data points for further analysis."""

    def __init__(self):
        self.data = []

    def collect_data(self, data_point):
        """Store a single data point."""
        self.data.append(data_point)

    def send_data(self):
        """Return all collected data."""
        return list(self.data)


class CodeLogger:
    """Logs important events for future inspection."""

    def __init__(self):
        self.history = []

    def log_event(self, event: str) -> None:
        self.history.append(event)

    def analyze_history(self):
        return [e for e in self.history if "error" in e]


class CodeInterpreter:
    """Interpret data and trigger agent behaviour."""

    def __init__(self, agent):
        self.agent = agent

    def interpret_decision(self, data: dict) -> str:
        """Interpret the incoming data and possibly trigger a decision."""
        emotion = data.get("emotion")
        tension = data.get("tension")
        if emotion is not None:
            self.agent.update_emotion(emotion)
        if tension is not None:
            self.agent.update_tension(tension)
        return self.agent.transition()
