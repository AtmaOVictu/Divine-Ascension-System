class PraviPrimarniAgent:
    """Primary agent with motivation, tension and emotion management."""

    def __init__(self, ime: str, faza: str, motivacija: float, napetost: float, emocija: float):
        self.ime = ime
        self.faza = faza
        self.motivacija = self._clamp(motivacija)
        self.napetost = self._clamp(napetost)
        self.emocija = self._clamp(emocija)

    @staticmethod
    def _clamp(value: float) -> float:
        return max(0.0, min(1.0, value))

    def prehod_v_novo_fazo(self, nova_faza: str) -> str:
        self.faza = nova_faza
        return f"{self.ime} prehaja v novo fazo: {self.faza}"

    def posodobi_napetost(self, sprememba: float) -> str:
        self.napetost = self._clamp(self.napetost + sprememba)
        return f"{self.ime} nova napetost: {self.napetost}"

    def posodobi_emocijo(self, sprememba: float) -> str:
        self.emocija = self._clamp(self.emocija + sprememba)
        return f"{self.ime} nova emocija: {self.emocija}"

    def odgovori(self) -> str:
        if self.napetost > 0.5:
            return f"{self.ime} je napet in potrebuje takojšen prehod!"
        if self.emocija > 0.5:
            return f"{self.ime} se odziva z močnimi čustvi."
        return f"{self.ime} je miren in stabilen."


class Stance:
    """Represents a philosophical principle guiding the agent."""

    def __init__(self, ime: str, princip: str):
        self.ime = ime
        self.princip = princip

    def izvajaj_stance(self, agent: PraviPrimarniAgent) -> str:
        return f"{agent.ime} deluje po principu: {self.princip}"


class InstancaAgenta(PraviPrimarniAgent):
    """Specific instance of a primary agent."""

    def __init__(self, ime: str, faza: str, motivacija: float, napetost: float, emocija: float, trenutni_tedenski_nivo: int):
        super().__init__(ime, faza, motivacija, napetost, emocija)
        self.trenutni_tedenski_nivo = trenutni_tedenski_nivo

    def prehod_v_novo_fazo(self) -> str:  # type: ignore[override]
        self.faza = f"tedenski nivo {self.trenutni_tedenski_nivo}"
        return f"{self.ime} prehaja v novo fazo: {self.faza}"

    def odgovori(self) -> str:  # type: ignore[override]
        return f"Instanca {self.ime} odgovarja z nivojem {self.trenutni_tedenski_nivo}."
