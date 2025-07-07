class Agent:
    """Represents an ontological agent capable of transitioning states.

    Agents hold ``keys`` that enable transitions and ``locks`` that prevent them.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name: str | None = None
        self.history = [state]
        self.keys: list[str] = []
        self.locks: list[str] = []

    def update_emotion(self, value: float, name: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value:
            Emotional intensity in the ``0-1`` range.
        name:
            Optional textual description of the emotion (e.g. ``'fear'``).
        """
        self.emotion = value
        if name is not None:
            self.emotion_name = name
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    # --- Key/Lock management -------------------------------------------------

    def acquire_key(self, key: str) -> None:
        """Add a key to the agent's set of available keys."""
        if key not in self.keys:
            self.keys.append(key)

    def add_lock(self, lock: str) -> None:
        """Add a lock that restricts transitions."""
        if lock not in self.locks:
            self.locks.append(lock)

    def has_access(self, key: str) -> bool:
        """Return ``True`` if the agent possesses the given key."""
        return key in self.keys

    def is_locked(self) -> bool:
        """Return ``True`` if any locks are present."""
        return bool(self.locks)

    def transition(self) -> str:
        """Perform state transition if thresholds and key/lock conditions allow."""
        if self.is_locked():
            return self.state

        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego" and self.has_access("Ego_to_Jaz"):
                self.state = "Jaz"
            elif self.state == "Jaz" and self.has_access("Jaz_to_Enotnost"):
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by state and emotion."""

        prefix = ""
        if self.emotion_name:
            prefix = f"[{self.emotion_name}] "

        if self.state == "Ego":
            return prefix + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return prefix + "Resnica je relativna, oblikovana z našimi odnosi."
        return prefix + "Vse resnice so eno, medsebojno povezane."


class MultiDimensionalAgent(Agent):
    """Agent that operates within a simple time/space model."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        super().__init__(name, state, tension, emotion)
        self.dimensions = {"time": 0, "space": 0}

    def update_dimension(self, dimension: str, value: float) -> None:
        if dimension in self.dimensions:
            self.dimensions[dimension] += value

    def transition(self) -> str:
        """Transition while also adjusting dimensional values."""
        original_state = self.state
        new_state = super().transition()
        if new_state != original_state:
            if new_state == "Jaz":
                self.update_dimension("time", 1)
            elif new_state == "Enotnost":
                self.update_dimension("space", 1)
        return new_state
