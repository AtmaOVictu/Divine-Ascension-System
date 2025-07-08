from dataclasses import dataclass

@dataclass(frozen=True)
class OntologicalState:
    """Represents philosophical state and its core principle."""
    name: str
    principle: str

EGO = OntologicalState(
    "Ego",
    "Resnica je absolutna in neodvisna od drugih."
)

JAZ = OntologicalState(
    "Jaz",
    "Resnica je relativna, oblikovana z našimi odnosi."
)

ENOTNOST = OntologicalState(
    "Enotnost",
    "Vse resnice so eno, medsebojno povezane."
)

STATES = (EGO, JAZ, ENOTNOST)
