import random
from typing import List


class Simulation:
    """Simulate possible future states based on current data."""

    def __init__(self) -> None:
        self.scenarios: List[str] = []

    def simulate_future(self, current_state: str) -> str:
        """Generate one possible future scenario with slight random shifts."""
        future_state = []
        for char in current_state:
            if char.isalpha():
                future_state.append(chr(ord(char) + random.randint(1, 3)))
            else:
                future_state.append(char)
        result = "".join(future_state)
        self.scenarios.append(result)
        return result

    def generate_multiple_scenarios(self, current_state: str, num_scenarios: int = 5) -> List[str]:
        """Create multiple future scenarios based on the current state."""
        return [self.simulate_future(current_state) for _ in range(num_scenarios)]
