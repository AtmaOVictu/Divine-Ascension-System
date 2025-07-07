class Lock:
    """Represents a lock preventing transitions until a condition is met."""

    def __init__(self, name: str, condition: str = "emotion") -> None:
        self.name = name
        self.condition = condition
        self.locked = True

    def unlock(self) -> None:
        self.locked = False

    def is_locked(self) -> bool:
        return self.locked


class Key:
    """Represents a key that can unlock a lock when conditions match."""

    def __init__(self, name: str, key_type: str = "emotion") -> None:
        self.name = name
        self.key_type = key_type

    def use(self, lock: Lock) -> bool:
        if self.key_type == lock.condition:
            lock.unlock()
            return True
        return False
