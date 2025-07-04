from dataclasses import dataclass
from typing import List

@dataclass
class RESPhase:
    """Represents a single RES phase."""
    label: str
    emotion: str = "Neutral"
    tension: float = 0.5
    purpose: str = "Initial Purpose"
    gift: str = ""

    def ready_for_transition(self) -> bool:
        """Check if the phase is ready for transition based on tension."""
        return self.tension >= 0.7


def create_res_phases() -> List[RESPhase]:
    """Create all RES phases from RES000, RES00, RES0 and RES001-RES100."""
    labels = ["RES000", "RES00", "RES0"]
    for i in range(1, 101):
        if i < 10:
            labels.append(f"RES00{i}")
        elif i < 100:
            labels.append(f"RES0{i}")
        else:
            labels.append(f"RES{i}")
    return [RESPhase(label=l) for l in labels]
