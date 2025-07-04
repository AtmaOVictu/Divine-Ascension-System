
from dataclasses import dataclass
from typing import List

@dataclass
class Phase:
    label: str
    emotion: str = "Neutral"
    tension: float = 0.5
    purpose: str = "Initial Purpose"
    gift: str = ""


def generate_phases() -> List[Phase]:
    """Generate RES phases from RES0, RES00, RES000 and RES001-RES100."""
    phases = [
        Phase("RES0"),
        Phase("RES00"),
        Phase("RES000"),
    ]
    for i in range(1, 101):
        label = f"RES{str(i).zfill(3)}"
        phases.append(Phase(label))
    return phases
