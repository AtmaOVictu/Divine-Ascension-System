from enum import Enum

class State(Enum):
    """Ontological states an agent can be in."""

    EGO = "Ego"
    JAZ = "Jaz"
    ENOTNOST = "Enotnost"

# Philosophical responses for each state
RESPONSES = {
    State.EGO: "Resnica je absolutna in neodvisna od drugih.",
    State.JAZ: "Resnica je relativna, oblikovana z našimi odnosi.",
    State.ENOTNOST: "Vse resnice so eno, medsebojno povezane.",
}
