from typing import List

from .keylock import Key, Lock


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.keys: List[Key] = []
        # Locks control when a transition may occur. Either emotion or tension can
        # unlock the next state.
        self.locks: List[Lock] = [
            Lock("Emotion Lock", lock_type="emotion"),
            Lock("Tension Lock", lock_type="tension"),
        ]

    def add_key(self, key: Key) -> None:
        """Add a key to the agent's collection."""
        self.keys.append(key)

    def add_lock(self, lock: Lock) -> None:
        """Add a lock to the agent's collection."""
        self.locks.append(lock)

    def attempt_unlock(self) -> None:
        """Attempt to unlock locks using available keys."""
        for lock in self.locks:
            if lock.is_locked():
                for key in list(self.keys):
                    if key.unlock(lock):
                        self.keys.remove(key)
                        break

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        # emotion influences tension
        self.tension += value
        if value > 0.5:
            self.add_key(Key("Emotion Key", key_type="emotion"))
            self.attempt_unlock()

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        if value > 0.7:
            self.add_key(Key("Tension Key", key_type="tension"))
            self.attempt_unlock()

    def transition(self) -> str:
        """Perform state transition if any lock has been unlocked."""
        # create keys when thresholds are reached
        if self.emotion > 0.5:
            self.add_key(Key("Emotion Key", key_type="emotion"))
        if self.tension > 0.7:
            self.add_key(Key("Tension Key", key_type="tension"))

        self.attempt_unlock()

        # move to the next state if a lock is unlocked
        unlocked = any(not lock.is_locked() for lock in self.locks)
        if unlocked:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
            # reset locks for future transitions
            for lock in self.locks:
                lock.locked = True

        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        emotional_prefix = ""
        if self.emotion > 0.5:
            emotional_prefix = "Čustveno, "

        if self.state == "Ego":
            return f"{emotional_prefix}Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return f"{emotional_prefix}Resnica je relativna, oblikovana z našimi odnosi."
        return f"{emotional_prefix}Vse resnice so eno, medsebojno povezane."
