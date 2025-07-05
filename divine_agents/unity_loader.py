from dataclasses import dataclass
import sys
import time

@dataclass
class UnityLoader:
    """Display unity progression from 0.01 to 1.00 then reset."""
    agent_name: str
    value: float = 0.01
    min_value: float = 0.01
    max_value: float = 1.0
    step: float = 0.01
    sleep: float = 0.0

    def load(self) -> None:
        """Run loading cycle once, resetting when done."""
        while self.value < self.max_value:
            self.value = round(self.value + self.step, 2)
            self.display()
            if self.sleep:
                time.sleep(self.sleep)
        self.value = self.min_value

    def display(self) -> None:
        progress = int(self.value * 100)
        sys.stdout.write(f"\r[{progress}%] Loading {self.agent_name} - Enotnost: {self.value:.2f}")
        sys.stdout.flush()
