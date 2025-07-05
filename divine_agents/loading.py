import sys
import time

class LoadingScreenUnity:
    """Simulate Enotnost as a loading screen from 0.01 to 1.00."""

    def __init__(self, agent_name: str, min_value: float = 0.01, max_value: float = 1.00):
        self.agent_name = agent_name
        self.unity_value = min_value
        self.min_value = min_value
        self.max_value = max_value
        self.history = []

    def display(self) -> None:
        """Display a progress bar updating unity value."""
        while self.unity_value < self.max_value:
            self.unity_value += 0.01
            progress = int(self.unity_value * 100)
            sys.stdout.write(f"\r[{progress}%] Loading... {self.agent_name} - Enotnost: {self.unity_value:.2f}")
            sys.stdout.flush()
            time.sleep(0.05)
        self.history.append(self.unity_value)
        self.unity_value = self.min_value
        sys.stdout.write("\n")
        sys.stdout.flush()
