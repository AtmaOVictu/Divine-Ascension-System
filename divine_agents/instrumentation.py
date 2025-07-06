class DataHarvester:
    """Collects data points for future analysis."""

    def __init__(self):
        self.data = []

    def collect_data(self, data_point):
        """Store a data point."""
        self.data.append(data_point)

    def send_data(self):
        """Return collected data for processing."""
        return self.data


class CodeLogger:
    """Simple event logger used during dialogue."""

    def __init__(self):
        self.history = []

    def log_event(self, event):
        self.history.append(event)

    def analyze_history(self):
        return [e for e in self.history if 'error' in e]


class CodeInterpreter:
    """Interprets data and decides whether an agent should transition."""

    def __init__(self, agent):
        self.agent = agent

    def interpret_decision(self, data):
        """Update agent metrics from data and trigger transition if needed."""
        if 'tension' in data:
            self.agent.update_tension(data['tension'])
        if 'emotion' in data:
            self.agent.update_emotion(data['emotion'])

        if self.agent.tension > 0.7 or self.agent.emotion > 0.5:
            return self.agent.transition()
        return self.agent.state
