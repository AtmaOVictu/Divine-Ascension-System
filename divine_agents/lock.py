class Lock:
    """Represents a lock preventing transitions until unlocked."""

    def __init__(self, name: str, condition: str = "emotion", threshold: float = 0.5):
        self.name = name
        self.condition = condition  # 'emotion' or 'tension'
        self.threshold = threshold
        self.locked = True

    def attempt_unlock(self, agent) -> bool:
        """Attempt to unlock based on the agent's state."""
        value = getattr(agent, self.condition, 0)
        if value > self.threshold:
            self.locked = False
        return not self.locked

    def is_locked(self) -> bool:
        return self.locked


class Key:
    """Represents a key capable of unlocking a lock if conditions match."""

    def __init__(self, name: str, key_type: str = "emotion"):
        self.name = name
        self.key_type = key_type

    def use(self, lock: Lock) -> bool:
        if self.key_type == lock.condition:
            lock.locked = False
            return True
        return False
