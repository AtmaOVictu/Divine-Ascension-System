from typing import List, Optional

from .keylock import Key, Lock


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_type: str = "neutral",
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history: List[str] = [state]
        self.keys: List[Key] = []
        self.locks: List[Lock] = []

    def update_emotion(self, value: float, emotion_type: Optional[str] = None) -> None:
        """Update emotion intensity and optionally its type."""
        self.emotion = value
        if emotion_type is not None:
            self.emotion_type = emotion_type
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def add_key(self, key: Key) -> None:
        """Add a key to this agent."""
        self.keys.append(key)

    def add_lock(self, lock: Lock) -> None:
        """Add a lock controlling a transition."""
        self.locks.append(lock)

    def attempt_unlock(self) -> bool:
        """Try to unlock any managed locks with available keys."""
        for lock in self.locks:
            if lock.is_locked():
                for key in self.keys:
                    if key.unlock(lock):
                        return True
        return False

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded or locks are unlocked."""
        unlocked = self.attempt_unlock()
        if unlocked or self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_type == "fear":
            return f"{base} (Občuti strah.)"
        if self.emotion_type == "joy":
            return f"{base} (Preveva ga veselje.)"
        if self.emotion_type == "anger":
            return f"{base} (Izraža jezo.)"
        return base
