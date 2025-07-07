from typing import List
from .key_lock import Key, Lock


class Agent:
    """Represents an ontological agent capable of transitioning states.

    Agents hold collections of keys and locks which can influence state
    transitions. A transition occurs when the agent's tension or emotion
    exceeds predefined thresholds and any matching locks are unlocked.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.keys: List[Key] = []
        self.locks: List[Lock] = []

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    # Key and lock management -------------------------------------------------

    def add_key(self, key: Key) -> None:
        """Add a key to the agent's collection."""
        self.keys.append(key)

    def add_lock(self, lock: Lock) -> None:
        """Add a lock to the agent's collection."""
        self.locks.append(lock)

    def _attempt_unlocks(self) -> None:
        """Try to unlock all locks using available keys."""
        for lock in self.locks:
            if lock.locked:
                for key in self.keys:
                    if key.unlock(lock):
                        break

    def transition(self) -> str:
        """Perform state transition if thresholds and locks allow it."""
        self._attempt_unlocks()

        if self.tension > 0.7 or self.emotion > 0.5:
            # ensure all locks are unlocked before moving forward
            if all(not lock.locked for lock in self.locks):
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
