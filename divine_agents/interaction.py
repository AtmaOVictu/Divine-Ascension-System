from typing import Callable

class Kapacitor:
    """Basic capacitor that reacts to user inputs."""

    def __init__(self) -> None:
        self.state = "Začetno"
        self.intensity = 0.0

    def sprejmi_vhod(self, odgovor: str) -> None:
        """Process user input and change internal state."""
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


class OkenskoSporocilo:
    """Interactive window message used for simple dialogues."""

    def __init__(self, sporocilo: str = "Dobrodošli!", input_func: Callable[[str], str] = input) -> None:
        self.sporocilo = sporocilo
        self.input_func = input_func

    def prikazi_okno(self) -> str:
        print(f"[INTERAKTIVNO OKNO] {self.sporocilo}")
        return self.input_func("Kako želite nadaljevati? (aktiviraj/prehod/zaključi): ")
