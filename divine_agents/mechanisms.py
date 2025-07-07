class Key:
    """Represents a key that can unlock locks of a matching type."""

    def __init__(self, name: str, key_type: str = "basic"):
        self.name = name
        self.key_type = key_type

    def unlock(self, lock: "Lock") -> bool:
        """Attempt to unlock the given lock."""
        if self.key_type == lock.lock_type:
            lock.unlock()
            return True
        return False


class Lock:
    """Represents a lock controlling access to transitions."""

    def __init__(self, name: str, lock_type: str = "basic"):
        self.name = name
        self.lock_type = lock_type
        self.locked = True

    def unlock(self) -> None:
        self.locked = False

    def is_locked(self) -> bool:
        return self.locked
