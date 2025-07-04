"""Enumeration of RES states from 0.01% to 100%.

Each state represents a phase in the ontological
transition process described by the system. The
states are ordered sequentially and can be used to
track progress through the process E/Jaz.
"""

from dataclasses import dataclass
from typing import Callable, Dict, List


@dataclass
class ResState:
    status: str
    description: str
    action: Callable[[], None]


def _default_action(name: str, description: str) -> Callable[[], None]:
    def _action():
        print(f"State {name}: {description}")
    return _action


RES_SEQUENCE: List[str] = [
    "RES000",
    "RES001",
    "RES010",
    "RES020",
    "RES030",
    "RES040",
    "RES050",
    "RES060",
    "RES080",
    "RES100",
]

RES_STATES: Dict[str, ResState] = {
    "RES000": ResState(
        status="inactive",
        description="Initial state - No requirement, awaiting activation.",
        action=_default_action("RES000", "Initiation of potential."),
    ),
    "RES001": ResState(
        status="active",
        description="First transition into activation. Possibilities start forming.",
        action=_default_action("RES001", "Activation initiated."),
    ),
    "RES010": ResState(
        status="searching",
        description="Searching for balance amidst emerging tensions.",
        action=_default_action("RES010", "Searching for equilibrium."),
    ),
    "RES020": ResState(
        status="tension",
        description="Tension builds, adapting to new circumstances.",
        action=_default_action("RES020", "Adjusting through tension."),
    ),
    "RES030": ResState(
        status="transformation",
        description="Transition through change, forming new structures.",
        action=_default_action("RES030", "Transformation in progress."),
    ),
    "RES040": ResState(
        status="expansion",
        description="Opening up to new possibilities and wider perspectives.",
        action=_default_action("RES040", "Expanding through new possibilities."),
    ),
    "RES050": ResState(
        status="reflection",
        description="Reflecting on progress and preparing for further evolution.",
        action=_default_action("RES050", "Reflecting and growing."),
    ),
    "RES060": ResState(
        status="stabilization",
        description="Stabilizing and integrating all prior phases into a coherent structure.",
        action=_default_action("RES060", "Integration and stabilization."),
    ),
    "RES080": ResState(
        status="maturity",
        description="Achieving maturity and preparing for final transitions.",
        action=_default_action("RES080", "Maturity achieved."),
    ),
    "RES100": ResState(
        status="unity",
        description="Complete unity and harmony across all phases.",
        action=_default_action("RES100", "Achieved unity and harmony."),
    ),
}
