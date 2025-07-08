from enum import Enum


class State(str, Enum):
    EGO = "Ego"
    JAZ = "Jaz"
    ENOTNOST = "Enotnost"


PRINCIPLES = {
    State.EGO: "Resnica je absolutna in neodvisna od drugih.",
    State.JAZ: "Resnica je relativna, oblikovana z našimi odnosi.",
    State.ENOTNOST: "Vse resnice so eno, medsebojno povezane.",
}
