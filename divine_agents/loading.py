"""Unity loading screen implementation."""
from __future__ import annotations

import sys
import time
from dataclasses import dataclass, field


@dataclass
class LoadingScreenUnity:
    """Represents a loading screen cycling unity from 0.01 to 1.0."""

    agent_name: str
    min_value: float = 0.01
    max_value: float = 1.0
    step: float = 0.01
    unity_value: float = field(init=False, default=0.01)

    def update_unity(self) -> None:
        """Increment unity until max_value then reset to min_value."""
        self.unity_value += self.step
        if self.unity_value > self.max_value:
            self.unity_value = self.min_value

    def display(self) -> None:
        """Display the current progress in the console."""
        progress = int(self.unity_value * 100)
        sys.stdout.write(f"\r[{progress}%] Loading... {self.agent_name} - Enotnost: {self.unity_value:.2f}")
        sys.stdout.flush()

    def run_cycle(self, delay: float = 0.1) -> None:
        """Run a full loading cycle from min_value to max_value."""
        while self.unity_value < self.max_value:
            self.update_unity()
            self.display()
            time.sleep(delay)
        self.display()
        sys.stdout.write("\n")
        self.update_unity()

