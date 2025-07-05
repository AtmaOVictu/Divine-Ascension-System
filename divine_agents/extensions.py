class Samoregulacija:
    """Simple self-regulation mechanism adjusting energy based on tension."""

    def __init__(self, energija: float, napetost: float) -> None:
        self.energija = energija
        self.napetost = napetost

    def prilagodi(self) -> None:
        if self.napetost > 0.8:
            self.energija *= 0.5
        elif self.napetost < 0.2:
            self.energija *= 1.2


class VecDimenzionalniAgent:
    """Agent capable of moving through multiple dimensions."""

    def __init__(self, ime: str, dimenzija: int = 1) -> None:
        self.ime = ime
        self.dimenzija = dimenzija

    def prehod_v_dimenzijo(self) -> int:
        if self.dimenzija >= 1:
            self.dimenzija += 1
        return self.dimenzija


class Ucenje:
    """Store experiences and optimise future decisions."""

    def __init__(self) -> None:
        self.izkusnje = []

    def uci(self, nova_izkusnja: str) -> None:
        self.izkusnje.append(nova_izkusnja)

    def optimiziraj_odlocitve(self) -> bool:
        return len(self.izkusnje) > 5


class CustvenaDinamika:
    """Manage emotional state and allow for simple ethical evaluation."""

    def __init__(self, stanje: str = "Nevtralno") -> None:
        self.stanje = stanje

    def posodobi_stanje(self, novo_stanje: str) -> None:
        self.stanje = novo_stanje

    def eticna_presoja(self) -> bool:
        return self.stanje != "tesnoba"

