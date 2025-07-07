"""Utility classes representing keys and locks for agent state transitions."""

from __future__ import annotations


class Key:
    """Represents a key that can unlock a specific lock."""

    def __init__(self, name: str, key_type: str = "basic") -> None:
        self.name = name
        self.key_type = key_type

    def unlock(self, lock: "Lock") -> bool:
        """Attempt to unlock a lock if the key type matches."""
        if self.key_type == lock.lock_type:
            lock.unlock()
            return True
        return False


class Lock:
    """Represents a lock controlling access to a state or task."""

    def __init__(self, name: str, lock_type: str = "emotion") -> None:
        self.name = name
        self.lock_type = lock_type
        self._locked = True

    def unlock(self) -> None:
        """Unlock the lock."""
        self._locked = False

    def is_locked(self) -> bool:
        """Return whether the lock is currently locked."""
        return self._locked
