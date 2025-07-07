class Agent:
    """Represents an ontological agent capable of transitioning states.

    Agents use *keys* to unlock transitions between ontological states while
    *locks* can temporarily block movement. Transitions occur only when
    emotional or tension thresholds are exceeded and the required key is
    present.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.keys = []
        self.locks = []

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    # Key and lock management -------------------------------------------------

    def acquire_key(self, key: str) -> None:
        """Give the agent a new key enabling future transitions."""
        if key not in self.keys:
            self.keys.append(key)

    def add_lock(self, lock: str) -> None:
        """Place a lock that prevents transitions until removed."""
        if lock not in self.locks:
            self.locks.append(lock)

    def remove_lock(self, lock: str) -> None:
        """Remove a previously added lock."""
        if lock in self.locks:
            self.locks.remove(lock)

    def has_key(self, key: str) -> bool:
        """Check whether the agent currently holds a given key."""
        return key in self.keys

    def is_locked(self) -> bool:
        """Determine if any lock is active."""
        return bool(self.locks)

    def transition(self) -> str:
        """Perform a state transition when thresholds and key conditions allow."""
        if self.is_locked():
            self.history.append(self.state)
            return self.state

        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego" and self.has_key("Ego_to_Jaz"):
                self.state = "Jaz"
            elif self.state == "Jaz" and self.has_key("Jaz_to_Enotnost"):
                self.state = "Enotnost"

        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        emotion_note = "" if self.emotion <= 0.5 else " Čutim močna čustva glede tega."
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih." + emotion_note
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi." + emotion_note
        return "Vse resnice so eno, medsebojno povezane." + emotion_note
