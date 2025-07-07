import time
from typing import List, Tuple


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, version: int = 1):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.version = version
        self.history = [state]
        self.sub_agents: List["SubAgent"] = []
        self.logs: List[str] = []
        self.log_entries: List[Tuple[float, str]] = []
        self.log_file = f"{self.name}_log.txt"
        self.timestamp: float = 0.0

    def add_sub_agent(self, sub_agent: "SubAgent") -> None:
        """Register a sub-agent without producing log output."""
        self.sub_agents.append(sub_agent)

    def log(self, message: str) -> str:
        """Record an action with a timestamp to memory and file."""
        self.timestamp = time.time()
        timestamp_str = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(self.timestamp))
        entry = f"{timestamp_str} - {message}"
        self.logs.append(message)
        self.log_entries.append((self.timestamp, message))
        with open(self.log_file, 'a') as file:
            file.write(entry + '\n')
        return entry

    def sort_logs(self) -> List[str]:
        """Return logs sorted by their timestamp."""
        ordered = sorted(self.log_entries, key=lambda x: x[0])
        return [msg for _, msg in ordered]

    def save_history(self) -> str:
        """Persist state history to a file."""
        file_name = f"{self.name}_history_{self.version}.txt"
        with open(file_name, 'w') as file:
            file.write(f"State History for {self.name}\n")
            for state in self.history:
                file.write(state + '\n')
        return file_name

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self.log(f"Emotion updated to {value}")
        for sub in self.sub_agents:
            sub.log(f"Emotion updated to {value}")

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.log(f"Tension set to {value}")

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        self.log(f"State transitioned to {self.state}")
        for sub in self.sub_agents:
            sub.log(f"State transitioned to {self.state}")
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."


class SubAgent:
    """A lightweight agent tied to a primary agent for logging purposes."""

    def __init__(self, name: str, associated_agent: Agent):
        self.name = name
        self.associated_agent = associated_agent
        self.logs: List[str] = []
        self.log_entries: List[Tuple[float, str]] = []

    def log(self, message: str) -> str:
        """Log an action while delegating to the associated agent."""
        entry = self.associated_agent.log(message)
        timestamp = self.associated_agent.timestamp
        self.logs.append(message)
        self.log_entries.append((timestamp, message))
        return entry

    def log_action(self, message: str) -> str:
        """Alias for log to mirror API from tests."""
        return self.log(message)

    def sort_logs(self) -> List[str]:
        ordered = sorted(self.log_entries, key=lambda x: x[0])
        return [msg for _, msg in ordered]
