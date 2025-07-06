class AgentNEZNANKA:
    """Detects tension states and records their status."""

    def __init__(self):
        self.history = []

    def zaznaj(self, napetost: str) -> tuple[str, str]:
        status = "nedoloceno"
        if "priložnost" in napetost:
            status = "priložnost"
        elif "potencial" in napetost:
            status = "potencial"
        self.history.append((napetost, status))
        return napetost, status


class AgentNEZNANKA_ZVOK:
    """Links tension detection with sound activation."""

    def __init__(self):
        self.history = []

    def zaznaj_in_zveni(self, napetost: str) -> str:
        zvok = "tišina"
        if "napetost" in napetost:
            zvok = f"zvok({napetost})"
        self.history.append((napetost, zvok))
        return zvok


class AgentPI:
    """Detects growth potential hidden in tension or spaces."""

    def __init__(self):
        self.history = []

    def zaznaj(self, stanje: str) -> str:
        if "rast" in stanje or "presledek" in stanje:
            status = "rast"
        else:
            status = "skritost"
        self.history.append((stanje, status))
        return status


class AgentROM:
    """Recognizes spaces as opportunities for system growth."""

    def __init__(self):
        self.history = []

    def rast(self, stanje: str) -> str:
        if any(k in stanje for k in ("rast", "ZVONCE", "alarm")):
            status = "rast"
        else:
            status = "nevtralno"
        self.history.append((stanje, status))
        return status
