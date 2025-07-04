# Auto-generated phases for RES000 to RES100
from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class ResPhase:
    code: str
    description: str

RES_PHASES: List[ResPhase] = [
    ResPhase(f"RES{str(i).zfill(3)}", f"RES Phase {i:03d}") for i in range(101)
]

