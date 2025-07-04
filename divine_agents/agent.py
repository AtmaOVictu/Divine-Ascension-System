from __future__ import annotations

from typing import Optional

from .phases import RESPhase


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        phase: Optional[RESPhase] = None,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.phase = phase
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
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

    # ------------------------------------------------------------------
    # Phase handling methods
    # ------------------------------------------------------------------
    def set_phase(self, phase: RESPhase) -> None:
        """Assign a phase to the agent."""
        self.phase = phase

    def modify_phase(
        self,
        new_emotion: str | None = None,
        new_tension: float | None = None,
        new_purpose: str | None = None,
        new_gift: str | None = None,
    ) -> None:
        """Modify the assigned phase if present."""
        if self.phase is not None:
            self.phase.modify(new_emotion, new_tension, new_purpose, new_gift)

    def progress_phase(self) -> bool:
        """Attempt to transition the current phase."""
        if self.phase is None:
            return False
        return self.phase.transition()
