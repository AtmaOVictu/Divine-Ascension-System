import time

class TimeModule:
    """Track and manage time progression."""

    def __init__(self):
        self.start_time = time.time()
        self.elapsed_time = 0.0

    def update_time(self) -> float:
        """Update and return the elapsed time."""
        self.elapsed_time = time.time() - self.start_time
        return self.elapsed_time

    def reset_time(self) -> None:
        """Reset the internal timer."""
        self.start_time = time.time()
        self.elapsed_time = 0.0
