from enum import Enum

class State(Enum):
    """Enumerates ontological states."""
    EGO = "Ego"
    JAZ = "Jaz"
    ENOTNOST = "Enotnost"


def philosophy_response(state: State) -> str:
    """Return a philosophical statement for the given state."""
    if state == State.EGO:
        return "Resnica je absolutna in neodvisna od drugih."
    if state == State.JAZ:
        return "Resnica je relativna, oblikovana z našimi odnosi."
    return "Vse resnice so eno, medsebojno povezane."
