from enum import Enum, auto

class OntologicalState(Enum):
    """Possible ontological states for an agent."""

    EGO = "Ego"
    JAZ = "Jaz"
    ENOTNOST = "Enotnost"


class EmotionType(Enum):
    """Basic emotions influencing an agent's tension."""

    NEUTRAL = "neutral"
    FEAR = "fear"
    JOY = "joy"
    ANGER = "anger"
