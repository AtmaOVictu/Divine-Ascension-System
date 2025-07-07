from typing import List, Optional

from .locks import Key, Lock


class Agent:
    """Ontological agent capable of transitioning states using keys and locks."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_label: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label
        self.history: List[str] = [state]
        self.keys: List[Key] = []
        self.locks: List[Lock] = [Lock(f"{state}_lock", "transition")]

    def add_key(self, key: Key) -> None:
        """Add a key to the agent's collection."""
        self.keys.append(key)

    def add_lock(self, lock: Lock) -> None:
        """Add a lock controlling access to the next state."""
        self.locks.append(lock)

    def update_emotion(self, value: float, label: Optional[str] = None) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        if label:
            self.emotion_label = label
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def attempt_unlock(self) -> bool:
        """Try unlocking any locks using available keys."""
        for lock in self.locks:
            if lock.is_locked():
                for key in self.keys:
                    if key.unlock(lock):
                        return True
        return False

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded and lock is opened."""
        if self.tension > 0.7 or self.emotion > 0.5:
            self.add_key(Key("Transition Key", "transition"))
            if self.attempt_unlock():
                if self.state == "Ego":
                    self.state = "Jaz"
                elif self.state == "Jaz":
                    self.state = "Enotnost"
                self.locks = [Lock(f"{self.state}_lock", "transition")]
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        emotion_prefix = ""
        if self.emotion_label != "neutral":
            emotion_prefix = f"[{self.emotion_label}] "

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return emotion_prefix + base
