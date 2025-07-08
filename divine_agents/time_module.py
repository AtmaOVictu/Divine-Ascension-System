import time

class TimeModule:
    """Track elapsed time and make simple predictions based on it."""

    def __init__(self) -> None:
        self.start_time = time.time()
        self.elapsed_time = 0.0

    def update_time(self) -> float:
        """Update and return elapsed time since initialization."""
        self.elapsed_time = time.time() - self.start_time
        return self.elapsed_time

    def time_to_future(self, prediction_factor: float) -> float:
        """Predict a future state based on elapsed time."""
        self.update_time()
        return self.elapsed_time * prediction_factor

    def reset_time(self) -> None:
        """Reset the timer for a new cycle."""
        self.start_time = time.time()
        self.elapsed_time = 0.0
