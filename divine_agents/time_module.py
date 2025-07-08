import time

class TimeModule:
    """Track and manage elapsed time for the agent system."""

    def __init__(self) -> None:
        self.start_time = time.time()
        self.elapsed_time = 0.0

    def update_time(self) -> float:
        """Update and return elapsed time since start."""
        self.elapsed_time = time.time() - self.start_time
        return self.elapsed_time

    def time_to_future(self, prediction_factor: float) -> float:
        """Predict a future value based on elapsed time."""
        return self.elapsed_time * prediction_factor

    def reset_time(self) -> None:
        """Reset the clock for a new cycle."""
        self.start_time = time.time()
        self.elapsed_time = 0.0
