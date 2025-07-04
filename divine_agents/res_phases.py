"""Module defining RES phases used as keys or transformers."""
from dataclasses import dataclass
from typing import List


@dataclass
class RESPhase:
    """Represents a single RES phase."""

    label: str
    emotion: str
    tension: float
    purpose: str
    gift: str = ""

    def transition_ready(self) -> bool:
        """Return True if the phase is ready for transition."""
        return self.tension >= 0.7


def create_res_phases() -> List[RESPhase]:
    """Create RES phases from RES000 to RES100 and special zero states."""
    phases: List[RESPhase] = []

    # Add explicit zero states
    for lbl in ("RES0", "RES00", "RES000"):
        phases.append(
            RESPhase(
                label=lbl,
                emotion="Neutral",
                tension=0.5,
                purpose="Initial Purpose",
            )
        )

    for i in range(1, 101):
        if i < 10:
            label = f"RES00{i}"
        elif i < 100:
            label = f"RES0{i}"
        else:
            label = f"RES{i}"

        phases.append(
            RESPhase(
                label=label,
                emotion="Neutral",
                tension=0.5,
                purpose="Initial Purpose",
            )
        )

    return phases
