class Kapacitor:
    """Enota za zbiranje uporabniških vhodov in sprožitev procesnih prehodov."""

    def __init__(self):
        self.stanje = "Začetno"
        self.intenziteta = 0.0

    def sprejmi_vhod(self, odgovor: str) -> None:
        """Obdelaj uporabniški odgovor in prilagodi stanje kapacitorja."""
        if odgovor == "aktiviraj":
            self.stanje = "Aktivacija"
            self.intenziteta += 0.3
            self.prikazi_sporocilo("Sistem se aktivira!")
        elif odgovor == "prehod":
            self.stanje = "Prehod"
            self.intenziteta += 0.5
            self.prikazi_sporocilo("Prehod je uspešen, premikamo se naprej.")
        elif odgovor == "zaključi":
            self.stanje = "Zaključek"
            self.intenziteta = 0.0
            self.prikazi_sporocilo("Proces je zaključen.")

    def prikazi_sporocilo(self, sporocilo: str) -> None:
        """Izpiši sporočilo uporabniku."""
        print(f"[OKNO] - {sporocilo}")

    def preveri_stanje(self) -> tuple[str, float]:
        """Vrni trenutno stanje in intenziteto."""
        return self.stanje, self.intenziteta


class OkenskoSporocilo:
    """Interaktivno okno, ki prejme uporabniški odgovor."""

    def __init__(self, sporocilo: str = "Dobrodošli!", input_func=input) -> None:
        self.sporocilo = sporocilo
        self.input_func = input_func

    def prikazi_okno(self) -> str:
        """Prikaži okno in vrni uporabnikov odgovor."""
        print(f"[INTERAKTIVNO OKNO] {self.sporocilo}")
        return self.input_func(
            "Kako želite nadaljevati? (aktiviraj/prehod/zaključi): "
        )
