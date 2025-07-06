from enum import Enum

class AgentState(str, Enum):
    """Enumeration of possible ontological agent states."""

    EGO = "Ego"
    JAZ = "Jaz"
    ENOTNOST = "Enotnost"
