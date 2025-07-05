class PraviPrimarniAgent:
    """Primary agent with basic motivational and emotional attributes."""

    def __init__(self, ime: str, faza: str, motivacija: float, napetost: float, emocija: float):
        self.ime = ime
        self.faza = faza
        self.motivacija = max(0, min(1, motivacija))
        self.napetost = max(0, min(1, napetost))
        self.emocija = max(0, min(1, emocija))

    def prehod_v_novo_fazo(self, nova_faza: str) -> str:
        self.faza = nova_faza
        return f"{self.ime} prehaja v novo fazo: {self.faza}"

    def posodobi_napetost(self, sprememba: float) -> float:
        self.napetost = max(0, min(1, self.napetost + sprememba))
        return self.napetost

    def posodobi_emocijo(self, sprememba: float) -> float:
        self.emocija = max(0, min(1, self.emocija + sprememba))
        return self.emocija

    def odgovori(self) -> str:
        if self.napetost > 0.5:
            return f"{self.ime} je napet in potrebuje takojšen prehod!"
        if self.emocija > 0.5:
            return f"{self.ime} se odziva z močnimi čustvi."
        return f"{self.ime} je miren in stabilen."


class Stance:
    """Represents a philosophical stance guiding an agent."""

    def __init__(self, ime: str, princip: str):
        self.ime = ime
        self.princip = princip

    def izvajaj_stance(self, agent: PraviPrimarniAgent) -> str:
        return f"{agent.ime} deluje po principu: {self.princip}"


class InstancaAgenta(PraviPrimarniAgent):
    """Specific instance of a primary agent with weekly level information."""

    def __init__(self, ime: str, faza: str, motivacija: float, napetost: float, emocija: float, trenutni_tedenski_nivo: int):
        super().__init__(ime, faza, motivacija, napetost, emocija)
        self.trenutni_tedenski_nivo = trenutni_tedenski_nivo

    def prehod_v_novo_fazo(self) -> str:  # type: ignore[override]
        return super().prehod_v_novo_fazo(f"tedenski nivo {self.trenutni_tedenski_nivo}")

    def odgovori(self) -> str:  # type: ignore[override]
        return f"Instanca {self.ime} odgovarja z nivojem {self.trenutni_tedenski_nivo}."
