class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Display name of the agent.
    state:
        Initial ontological state. One of ``Ego``, ``Jaz`` or ``Enotnost``.
    tension:
        Initial tension value in range ``0.0`` - ``1.0``.
    emotion:
        Initial emotion intensity in range ``0.0`` - ``1.0``.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.keys: list[str] = []
        self.locks: list[str] = []

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def acquire_key(self, key: str) -> None:
        """Add a key to the agent's collection if not already present."""
        if key not in self.keys:
            self.keys.append(key)

    def add_lock(self, lock: str) -> None:
        """Add a lock that restricts transitions."""
        if lock not in self.locks:
            self.locks.append(lock)

    def remove_lock(self, lock: str) -> None:
        """Remove a lock if present."""
        if lock in self.locks:
            self.locks.remove(lock)

    def has_access(self, key: str) -> bool:
        """Return ``True`` if the agent possesses the given key."""
        return key in self.keys

    def is_locked(self) -> bool:
        """Return ``True`` if any locks are active."""
        return bool(self.locks)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition when thresholds and key conditions are met."""
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
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."


class MultiDimensionalAgent(Agent):
    """Agent operating in a simple multi-dimensional space."""

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
    ) -> None:
        super().__init__(name, state, tension, emotion)
        self.dimensions: dict[str, int] = {"time": 0, "space": 0}

    def update_dimension(self, dimension: str, value: int) -> None:
        """Update the specified dimension if present."""
        if dimension in self.dimensions:
            self.dimensions[dimension] += value

    def transition(self) -> str:
        """Perform transition and update dimensions accordingly."""
        prev_state = self.state
        new_state = super().transition()
        if prev_state != new_state:
            if new_state == "Jaz":
                self.update_dimension("time", 1)
            elif new_state == "Enotnost":
                self.update_dimension("space", 1)
        return new_state
