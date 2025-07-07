from __future__ import annotations

from typing import List
from .lock import Lock, Key


class Agent:
    """Ontological agent capable of transitioning between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history: List[str] = [state]
        self.locks: List[Lock] = []
        self.keys: List[Key] = []

    # ----- Emotion and tension management -----
    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    # ----- Lock management -----
    def add_lock(self, lock: Lock) -> None:
        self.locks.append(lock)

    def add_key(self, key: Key) -> None:
        self.keys.append(key)

    def attempt_unlock(self) -> None:
        """Attempt to unlock all locks using available keys."""
        for lock in self.locks:
            if lock.is_locked():
                for key in self.keys:
                    if key.use(lock):
                        break

    # ----- State transitions -----
    def can_transition(self) -> bool:
        """Check if thresholds allow transition and locks are open."""
        threshold_met = self.tension > 0.7 or self.emotion > 0.5
        if not threshold_met:
            return False
        self.attempt_unlock()
        if any(lock.is_locked() for lock in self.locks):
            return False
        return True

    def transition(self) -> str:
        """Perform state transition if possible."""
        if self.can_transition():
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    # ----- Responses -----
    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the agent's state and emotion."""
        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }[self.state]
        if self.emotion > 0.5:
            return f"{base} Čutim močna čustva."
        return base
