class Lock:
    """Represents a lock preventing the agent from transitioning until a condition is met."""

    def __init__(self, name: str, lock_type: str = "state", condition: str = "emotion"):
        self.name = name
        self.lock_type = lock_type
        self.condition = condition
        self.locked = True

    def unlock(self) -> str:
        """Unlock the lock."""
        self.locked = False
        return f"{self.name} is now unlocked."

    def is_locked(self) -> bool:
        """Return True if the lock is active."""
        return self.locked


class Key:
    """Represents a key that can unlock a specific lock."""

    def __init__(self, name: str, key_type: str = "emotion"):
        self.name = name
        self.key_type = key_type

    def use(self, lock: Lock) -> str:
        """Try to unlock the lock if key type matches the lock condition."""
        if self.key_type == lock.condition:
            return lock.unlock()
        return f"Key {self.name} cannot unlock {lock.name} because conditions do not match."
