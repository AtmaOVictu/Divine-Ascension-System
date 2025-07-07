from typing import List

from .lock import Lock, Key


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.locks: List[Lock] = []
        self.keys: List[Key] = []

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def add_lock(self, lock: Lock) -> None:
        """Attach a lock to the agent."""
        self.locks.append(lock)

    def add_key(self, key: Key) -> None:
        """Provide a key to the agent."""
        self.keys.append(key)

    def attempt_unlock(self) -> bool:
        """Try to unlock all locks using available keys."""
        unlocked_any = False
        for lock in self.locks:
            if lock.is_locked():
                for key in self.keys:
                    if key.key_type == lock.condition:
                        key.use(lock)
                        unlocked_any = True
                        break
        return unlocked_any

    def transition(self) -> str:
        """Perform state transition if thresholds and unlock conditions are met."""
        if self.locks:
            self.attempt_unlock()
        locked = any(lock.is_locked() for lock in self.locks)
        if not locked and (self.tension > 0.7 or self.emotion > 0.5):
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
