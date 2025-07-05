from enum import Enum, auto


class OntoState(Enum):
    """Enumeration of ontological states."""
    Ego = auto()
    Jaz = auto()
    Enotnost = auto()


# Transition thresholds
TRANSITION_TENSION_THRESHOLD = 0.7
TRANSITION_EMOTION_THRESHOLD = 0.5


def should_transition(tension: float, emotion: float) -> bool:
    """Return True if thresholds for a state change are exceeded."""
    return tension > TRANSITION_TENSION_THRESHOLD or emotion > TRANSITION_EMOTION_THRESHOLD


def truth_statement(state: OntoState) -> str:
    """Return a truth statement based on ontological state."""
    if state == OntoState.Ego:
        return "Resnica je absolutna in neodvisna od drugih."
    if state == OntoState.Jaz:
        return "Resnica je relativna, oblikovana z našimi odnosi."
    return "Vse resnice so eno, medsebojno povezane."
