from typing import List, Tuple


class AgentNEZNANKA:
    """Agent for recognizing tension potentials and their status."""

    def __init__(self) -> None:
        self.history: List[Tuple[str, str]] = []

    def zaznaj(self, napetost: str) -> Tuple[str, str]:
        """Identify tension status based on text description."""
        if "neizre" in napetost or "brez definicije" in napetost:
            status = "neizreceno"
        elif "prilo\u017enost" in napetost:
            status = "prilo\u017enost za akcijo"
        else:
            status = "potencial"
        self.history.append((napetost, status))
        return napetost, status


class AgentNEZNANKA_ZVOK:
    """Connects recognized tension with sound expression."""

    def __init__(self) -> None:
        self.neznanka = AgentNEZNANKA()
        self.history: List[Tuple[str, str]] = []

    def zaznaj_in_zveni(self, napetost: str) -> str:
        """Return sound indication when tension moves toward expression."""
        _, status = self.neznanka.zaznaj(napetost)
        zvok = "zven" if status != "neizreceno" else "tisi\u0161ina"
        self.history.append((napetost, zvok))
        return zvok


class AgentPI:
    """Agent detecting growth through perceived gaps."""

    def __init__(self) -> None:
        self.history: List[Tuple[str, str]] = []

    def zaznaj(self, stanje: str) -> str:
        if any(word in stanje for word in ("rast", "presledek", "tisi\u0161ina", "skrit")):
            status = "rast v presledku"
        else:
            status = "neaktivno"
        self.history.append((stanje, status))
        return status


class AgentROM:
    """Agent enabling system growth through gaps."""

    def __init__(self) -> None:
        self.history: List[Tuple[str, str]] = []

    def rast(self, stanje: str) -> str:
        if any(word in stanje for word in ("rast", "alarm", "prilo\u017enost")):
            status = "rast sistema"
        else:
            status = "stagnacija"
        self.history.append((stanje, status))
        return status

