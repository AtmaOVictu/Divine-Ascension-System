from typing import List
from .keylock import Key, Lock


class Agent:
    """Represents an ontological agent capable of transitioning states.

    The agent can hold keys and locks. State transitions are triggered when
    tension or emotion thresholds are exceeded and, if locks are present,
    at least one lock has been unlocked with a corresponding key.
    """

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

    def add_key(self, key: Key) -> None:
        """Add a key to the agent's collection."""
        self.keys.append(key)

    def add_lock(self, lock: Lock) -> None:
        """Add a lock the agent must unlock before transitioning."""
        self.locks.append(lock)

    def attempt_unlock(self) -> bool:
        """Try to unlock locks with available keys."""
        unlocked = False
        for lock in self.locks:
            if lock.is_locked():
                for key in self.keys:
                    if key.unlock(lock):
                        self.history.append(f"{self.name} unlocked {lock.name}")
                        unlocked = True
                        break
        return unlocked

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition when conditions and locks allow it."""
        can_transition = True
        if self.locks:
            can_transition = self.attempt_unlock()

        if can_transition and (self.tension > 0.7 or self.emotion > 0.5):
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
