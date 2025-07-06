from enum import Enum

class OntologyState(Enum):
    """Possible ontological states for an agent."""
    EGO = "Ego"
    JAZ = "Jaz"
    ENOTNOST = "Enotnost"

STATE_SYMBOLS = {
    OntologyState.EGO: "\u2298",       # ⊘
    OntologyState.JAZ: "\u222B(dru/x)", # ∫(dru/x)
    OntologyState.ENOTNOST: "RES001",
}
