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
        self.locks: list[Lock] = []
        self.keys: list[Key] = []

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def add_lock(self, lock: Lock) -> None:
        """Associate a lock with the agent."""
        self.locks.append(lock)

    def add_key(self, key: Key) -> None:
        """Provide a key to the agent."""
        self.keys.append(key)

    def _attempt_unlocks(self) -> None:
        """Attempt to unlock locks using keys or thresholds."""
        for lock in self.locks:
            if not lock.locked:
                continue
            # try keys first
            for key in self.keys:
                if key.use(lock):
                    break
            if lock.is_locked():
                lock.attempt_unlock(self)

    def transition(self) -> str:
        """Perform state transition if locks are unlocked and thresholds met."""
        self._attempt_unlocks()
        locked = any(lock.is_locked() for lock in self.locks)
        if not locked and (self.tension > 0.7 or self.emotion > 0.5):
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state and emotion."""
        if self.state == "Ego":
            response = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            response = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            response = "Vse resnice so eno, medsebojno povezane."
        return f"{response} (emocija: {self.emotion:.2f})"
