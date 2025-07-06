from typing import List, Tuple


class AgentNEZNANKA:
    """Recognizes potential tensions and their status."""

    def __init__(self) -> None:
        self.history: List[Tuple[str, str]] = []

    def zaznaj(self, napetost: str) -> Tuple[str, str]:
        """Identify the status of the given tension."""
        lower = napetost.lower()
        if "priloznost" in lower:
            status = "priloznost"
        elif "neizrecen" in lower:
            status = "neizreceno"
        else:
            status = "potencial"
        self.history.append((napetost, status))
        return napetost, status


class AgentNEZNANKA_ZVOK(AgentNEZNANKA):
    """Extends AgentNEZNANKA by connecting tension to sound."""

    def zaznaj_in_zveni(self, napetost: str) -> str:
        _, status = super().zaznaj(napetost)
        return f"zven: {status}"


class AgentPI:
    """Recognizes growth through spaces."""

    def __init__(self) -> None:
        self.history: List[Tuple[str, str]] = []

    def zaznaj(self, stanje: str) -> Tuple[str, str]:
        lower = stanje.lower()
        if "presledek" in lower or "tisina" in lower:
            status = "rast"
        else:
            status = "neopredeljeno"
        self.history.append((stanje, status))
        return stanje, status


class AgentROM:
    """Recognizes gaps as opportunities for growth."""

    def __init__(self) -> None:
        self.history: List[Tuple[str, str]] = []

    def rast(self, stanje: str) -> Tuple[str, str]:
        lower = stanje.lower()
        if "alarm" in lower or "zvoc" in lower:
            status = "prehod"
        else:
            status = "raste"
        self.history.append((stanje, status))
        return stanje, status
