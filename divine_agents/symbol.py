import time

class Symbol:
    """Represents a symbolic entity with evolving versions."""

    def __init__(self, name: str, version: str = "1.0"):
        self.name = name
        self.version = version
        self.history = [self.version]
        self.timestamp = time.time()

    def evolve(self) -> None:
        """Evolve the symbol to a new version."""
        major, minor = self.version.split('.')
        minor = int(minor) + 1
        self.version = f"{major}.{minor}"
        self.history.append(self.version)
        self.timestamp = time.time()

    def get_current_state(self) -> str:
        """Return a string representing the current version of the symbol."""
        return f"Symbol {self.name} at version {self.version}"
