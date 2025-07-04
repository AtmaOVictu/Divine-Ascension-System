import math


def evolution_function(t: float) -> float:
    """Return logistic progress between 0 and 1."""
    return 1 / (1 + math.exp(-t))


def transition_res(percentage: float) -> str:
    """Map progress percentage to RES phase description."""
    if percentage <= 0.1:
        return "RES001 - Začetek: Stabilno stanje, minimalen napredek."
    elif 0.1 < percentage <= 0.3:
        return "RES010 - Iskanje ravnotežja: Začetni prehodi, rast napetosti."
    elif 0.3 < percentage <= 0.6:
        return "RES030 - Stabilnost napetosti: Stabilizacija čustev in napetosti."
    elif 0.6 < percentage <= 0.9:
        return "RES060 - Povečana harmonija: Progresivne refleksije in harmonija."
    elif 0.9 < percentage <= 1:
        return "RES100 - Popolna integracija: Dosežena popolna enotnost."
    return "Neveljaven napredek."
