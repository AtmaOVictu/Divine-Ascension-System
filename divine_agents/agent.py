import time
from typing import List


class Agent:
    """Represents an ontological agent capable of transitioning states with timestamped logging."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history: List[str] = [state]
        self.timestamp = time.time()
        self.version = self._generate_version()
        self.log_file = f"{self.name}_log_{self.version}.txt"
        self._initialize_log()

    def _generate_version(self) -> str:
        """Generate a unique version identifier based on time."""
        return time.strftime("%Y%m%d%H%M%S", time.gmtime(self.timestamp))

    def _initialize_log(self) -> None:
        """Initialize the log file and write initial data."""
        with open(self.log_file, "w") as file:
            file.write(f"Log Version: {self.version}\n")
            file.write(f"Agent: {self.name}\n")
            file.write(f"Start Time: {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(self.timestamp))}\n\n")

    def log(self, message: str) -> None:
        """Log a message with a timestamp."""
        timestamp_str = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(self.timestamp))
        with open(self.log_file, "a") as file:
            file.write(f"{timestamp_str} - {message}\n")

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self.log(f"Emotion updated to {self.emotion}")

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.log(f"Tension updated to {self.tension}")

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
            elif self.state == "Enotnost":
                self.state = "Ego"
        self.history.append(self.state)
        self.timestamp = time.time()
        self.log(f"State transitioned to {self.state}")
        return self.state

    def apply_emotion_influence(self, response: str) -> str:
        """Influence response with emotional tone."""
        if self.emotion > 0.7:
            return f"Z veseljem: {response}"
        if self.emotion < 0.3:
            return f"S strahom: {response}"
        return response

    def respond(self, question: str) -> str:
        """Generate a philosophical answer depending on the current state."""
        if self.state == "Ego":
            response = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            response = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            response = "Vse resnice so eno, medsebojno povezane."
        response = self.apply_emotion_influence(response)
        self.log(f"Response: {response}")
        return response

    def save_history(self) -> None:
        """Save history to external file."""
        history_file = f"{self.name}_history_{self.version}.txt"
        with open(history_file, "w") as file:
            file.write(f"State History for {self.name}\n")
            for state in self.history:
                file.write(f"{state}\n")


class SubAgent:
    """Responsible for sorting and managing agent logs."""

    def __init__(self) -> None:
        self.agents_logs: dict[str, Agent] = {}

    def add_agent(self, agent: Agent) -> None:
        """Add an agent's log to the manager."""
        self.agents_logs[agent.name] = agent

    def sort_logs_by_version(self) -> list[Agent]:
        """Sort logs based on the version timestamp."""
        sorted_agents = sorted(self.agents_logs.values(), key=lambda a: a.timestamp)
        return sorted_agents

    def save_all_logs(self) -> None:
        """Save logs and histories of all agents."""
        for agent in self.agents_logs.values():
            agent.save_history()
            print(f"Log saved for {agent.name} with version {agent.version}")

