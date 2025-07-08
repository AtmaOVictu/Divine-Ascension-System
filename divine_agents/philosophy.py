from enum import Enum

class State(Enum):
    """Enumerates ontological states for agents."""

    EGO = "Ego"
    JAZ = "Jaz"
    ENOTNOST = "Enotnost"


PHILOSOPHICAL_TRUTHS = {
    State.EGO: "Resnica je absolutna in neodvisna od drugih.",
    State.JAZ: "Resnica je relativna, oblikovana z nasimi odnosi.",
    State.ENOTNOST: "Vse resnice so eno, medsebojno povezane.",
}
