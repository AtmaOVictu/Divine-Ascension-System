import time

class Log:
    """Simple logging utility with timestamped messages."""
    def __init__(self):
        self.entries = []

    def add(self, message: str) -> None:
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
        self.entries.append(f"{timestamp} - {message}")

    def __iter__(self):
        return iter(self.entries)

    def last(self):
        return self.entries[-1] if self.entries else None
