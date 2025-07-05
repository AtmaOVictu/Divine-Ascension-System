class PraviPrimarniAgent:
    """Osnovna izvedba primarnega agenta v RES sistemu."""

    def __init__(self, ime: str, faza: str, motivacija: float, napetost: float, emocija: float) -> None:
        self.ime = ime
        self.faza = faza
        self.motivacija = max(0.0, min(1.0, motivacija))
        self.napetost = max(0.0, min(1.0, napetost))
        self.emocija = max(0.0, min(1.0, emocija))

    def prehod_v_novo_fazo(self, nova_faza: str) -> None:
        """Posodobi trenutno fazo agenta."""
        self.faza = nova_faza

    def posodobi_napetost(self, sprememba: float) -> None:
        """Spremeni napetost in omeji njeno vrednost med 0 in 1."""
        self.napetost = max(0.0, min(1.0, self.napetost + sprememba))

    def posodobi_emocijo(self, sprememba: float) -> None:
        """Spremeni emocijo in omeji njeno vrednost med 0 in 1."""
        self.emocija = max(0.0, min(1.0, self.emocija + sprememba))

    def odgovori(self) -> str:
        """Podaj odziv glede na trenutno napetost in emocijo."""
        if self.napetost > 0.5:
            return f"{self.ime} je napet in potrebuje takojšen prehod!"
        if self.emocija > 0.5:
            return f"{self.ime} se odziva z močnimi čustvi."
        return f"{self.ime} je miren in stabilen."


class Stance:
    """Filozofski ali moralni princip delovanja agenta."""

    def __init__(self, ime: str, princip: str) -> None:
        self.ime = ime
        self.princip = princip

    def izvajaj_stance(self, agent: PraviPrimarniAgent) -> str:
        """Vrne opis delovanja agenta po izbranem principu."""
        return f"{agent.ime} deluje po principu: {self.princip}"


class InstancaAgenta(PraviPrimarniAgent):
    """Specifična instanca primarnega agenta z dodatnim tedenskim nivojem."""

    def __init__(self, ime: str, faza: str, motivacija: float, napetost: float, emocija: float, trenutni_tedenski_nivo: int) -> None:
        super().__init__(ime, faza, motivacija, napetost, emocija)
        self.trenutni_tedenski_nivo = trenutni_tedenski_nivo

    def prehod_v_novo_fazo(self) -> None:  # type: ignore[override]
        """Prehod v fazo, ki odraža tedenski nivo."""
        nova = f"tedenski nivo {self.trenutni_tedenski_nivo}"
        super().prehod_v_novo_fazo(nova)

    def odgovori(self) -> str:  # type: ignore[override]
        """Odgovor, ki poudari nivo instance."""
        return f"Instanca {self.ime} odgovarja z nivojem {self.trenutni_tedenski_nivo}."
