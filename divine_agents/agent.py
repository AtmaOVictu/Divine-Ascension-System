from __future__ import annotations

from typing import List

from .mechanisms import Key, Lock


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history: List[str] = [state]
        self.keys: List[Key] = []
        self.locks: List[Lock] = []

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def add_key(self, key: Key) -> None:
        """Add a key to the agent's collection."""
        self.keys.append(key)

    def add_lock(self, lock: Lock) -> None:
        """Add a lock to the agent's collection."""
        self.locks.append(lock)

    def attempt_unlock(self) -> bool:
        """Attempt to unlock any locks with available keys."""
        unlocked = False
        for lock in self.locks:
            if lock.is_locked():
                for key in self.keys:
                    if key.unlock(lock):
                        self.history.append(f"{self.name} unlocked {lock.name}")
                        unlocked = True
                        break
        return unlocked

    def transition(self) -> str:
        """Perform state transition if thresholds or unlocks allow it."""
        unlocked = self.attempt_unlock()
        if unlocked or self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.7:
            mood = "z velikim čustvom"
        elif self.emotion > 0.3:
            mood = "mirno"
        else:
            mood = "brez posebnih čustev"
        return f"{base} ({mood})"
