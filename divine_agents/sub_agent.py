import time


class SubAgent:
    """Helper entity that logs actions for an associated agent."""

    def __init__(self, name: str, associated_agent: 'Agent'):
        self.name = name
        self.associated_agent = associated_agent
        self.logs = []

    def log_action(self, action: str) -> None:
        """Record an action with a timestamp."""
        timestamp_str = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
        self.logs.append(f"{timestamp_str} - {self.name}: {action}")

    def sort_logs(self):
        """Return logs sorted chronologically."""
        self.logs.sort(key=lambda x: x.split(' - ')[0])
        return self.logs
