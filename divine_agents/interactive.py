class Kapacitor:
    """Simple interactive component for collecting user input."""

    def __init__(self):
        self.state = "Začetno"
        self.intensity = 0.0

    def sprejmi_vhod(self, odgovor: str) -> None:
        if odgovor == "aktiviraj":
            self.state = "Aktivacija"
            self.intensity += 0.3
            self.prikazi_sporocilo("Sistem se aktivira!")
        elif odgovor == "prehod":
            self.state = "Prehod"
            self.intensity += 0.5
            self.prikazi_sporocilo("Prehod je uspešen, premikamo se naprej.")
        elif odgovor == "zaključi":
            self.state = "Zaključek"
            self.intensity = 0
            self.prikazi_sporocilo("Proces je zaključen.")

    def prikazi_sporocilo(self, sporocilo: str) -> None:
        print(f"[OKNO] - {sporocilo}")

    def preveri_stanje(self) -> str:
        return f"Trenutno stanje: {self.state}, intenziteta: {self.intensity}"
