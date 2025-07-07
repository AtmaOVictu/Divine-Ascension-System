"""Agent implementation with ontological states and locking mechanism."""
from __future__ import annotations

from typing import List
from .lock import Lock, Key


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history: List[str] = [state]
        self.locks: List[Lock] = []
        self.keys: List[Key] = []

    def add_lock(self, lock: Lock) -> None:
        """Attach a lock to the agent."""
        self.locks.append(lock)

    def add_key(self, key: Key) -> None:
        """Give the agent a key for unlocking locks."""
        self.keys.append(key)

    def attempt_unlock(self) -> None:
        """Attempt to unlock all locks with available keys."""
        for lock in self.locks:
            if lock.is_locked():
                for key in self.keys:
                    if key.key_type == lock.condition:
                        key.use(lock)
                        break

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded and locks are unlocked."""
        self.attempt_unlock()
        if any(lock.is_locked() for lock in self.locks):
            self.history.append(self.state)
            return self.state

        if self.tension > 0.7 or self.emotion > 0.5:
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
