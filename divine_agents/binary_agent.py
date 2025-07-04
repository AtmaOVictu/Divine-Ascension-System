class BinaryAgent:
    """A simple agent with binary states (0=RES000, 1=active)."""

    def __init__(self, agent_id: int, phase: int = 0, tension: float = 0.0, emotion: float = 0.0):
        """Initialize the binary agent.

        Parameters
        ----------
        agent_id : int
            Unique identifier for the agent.
        phase : int, optional
            Current phase (0 for RES000, 1 for active), by default 0.
        tension : float, optional
            Current tension level, by default 0.0.
        emotion : float, optional
            Current emotion intensity, by default 0.0.
        """
        self.id = agent_id
        self.phase = phase
        self.tension = tension
        self.emotion = emotion

    def transition(self) -> int:
        """Transition from RES000 (0) to active (1) if thresholds exceeded."""
        if self.phase == 0 and (self.tension > 0.5 or self.emotion > 0.5):
            self.phase = 1
        return self.phase

    def get_state(self) -> str:
        """Return a human-readable description of the current phase."""
        return "RES000 - Mirovanje (0)" if self.phase == 0 else "Aktivacija (1)"

