from __future__ import annotations

from typing import List

from .keylock import Key, Lock


class Agent:
    """Represents an ontological agent capable of transitioning states.

    The agent holds collections of :class:`Key` objects and :class:`Lock` objects
    which can influence its ability to move between ontological states.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
    ) -> None:
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

    # ------------------------------------------------------------------
    # Key and Lock management
    # ------------------------------------------------------------------
    def add_key(self, key: Key) -> None:
        """Add a key to the agent's collection."""
        self.keys.append(key)

    def add_lock(self, lock: Lock) -> None:
        """Add a lock to the agent's collection."""
        self.locks.append(lock)

    def attempt_unlock(self) -> bool:
        """Attempt to unlock locks using available keys."""
        for lock in self.locks:
            if lock.is_locked():
                for key in self.keys:
                    if key.unlock(lock):
                        self.history.append(f"{self.name} unlocked {lock.name}")
                        return True
        return False

    def transition(self) -> str:
        """Perform state transition if thresholds or unlock conditions are met."""
        triggered = self.tension > 0.7 or self.emotion > 0.5 or self.attempt_unlock()
        if triggered:
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
