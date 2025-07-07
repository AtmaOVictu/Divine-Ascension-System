from .lock import Lock


class Agent:
    """Ontological agent capable of transitioning between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.locks = [
            Lock("tension", "tension", 0.7),
            Lock("emotion", "emotion", 0.5),
        ]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity, adjust tension, and evaluate locks."""
        self.emotion = value
        self.tension += value
        for lock in self.locks:
            if lock.condition_type == "emotion":
                lock.attempt_unlock(self.emotion)
            if lock.condition_type == "tension":
                lock.attempt_unlock(self.tension)

    def update_tension(self, value: float) -> None:
        """Directly set tension level and evaluate locks."""
        self.tension = value
        for lock in self.locks:
            if lock.condition_type == "tension":
                lock.attempt_unlock(self.tension)

    def transition(self) -> str:
        """Perform state transition when any lock is unlocked."""
        if any(not lock.is_locked() for lock in self.locks):
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer based on the current ontological state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{base} Čustvo: {self.emotion:.2f}"
