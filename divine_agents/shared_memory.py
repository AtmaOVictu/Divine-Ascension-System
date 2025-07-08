class SharedMemory:
    """Store historical events shared among agents."""

    def __init__(self) -> None:
        self._log: list[str] = []

    def record_event(self, event: str) -> None:
        """Record an event to the shared memory."""
        self._log.append(event)

    def retrieve_history(self) -> list[str]:
        """Return the list of recorded events."""
        return list(self._log)
