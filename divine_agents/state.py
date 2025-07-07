from enum import Enum, auto


class OntoState(Enum):
    """Ontological states that agents can occupy."""

    EGO = auto()
    JAZ = auto()
    ENOTNOST = auto()

    def philosophy(self) -> str:
        """Return the philosophical principle associated with the state."""
        if self is OntoState.EGO:
            return "Resnica je absolutna in neodvisna od drugih."
        if self is OntoState.JAZ:
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
