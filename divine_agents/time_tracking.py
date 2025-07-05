import time
from typing import Dict, Sequence, Callable


class TimeTracker:
    """Track time spent in each state for an agent."""

    def __init__(self, states: Sequence[str], time_fn: Callable[[], float] | None = None) -> None:
        self._time_fn = time_fn or time.time
        self._time_spent: Dict[str, float] = {state: 0.0 for state in states}
        self._current_state: str | None = None
        self._state_start: float | None = None

    @property
    def time_spent(self) -> Dict[str, float]:
        """Return accumulated time spent in each state."""
        return dict(self._time_spent)

    def start(self, state: str) -> None:
        """Start tracking a state."""
        self._current_state = state
        self._state_start = self._time_fn()

    def switch(self, state: str) -> None:
        """Switch to a new state and accumulate time spent in the previous state."""
        now = self._time_fn()
        if self._current_state is not None and self._state_start is not None:
            self._time_spent[self._current_state] += now - self._state_start
        self._current_state = state
        self._state_start = now
