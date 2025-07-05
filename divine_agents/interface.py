"""Interactive components for the Divine Ascension system."""

from typing import Callable


class Kapacitor:
    """Simple handler that reacts to user inputs and manages state."""

    def __init__(self) -> None:
        self.stanje = "Začetno"
        self.intenziteta = 0.0

    def sprejmi_vhod(self, odgovor: str) -> str:
        """Process user input and update internal state."""
        if odgovor == "aktiviraj":
            self.stanje = "Aktivacija"
            self.intenziteta += 0.3
            return "Sistem se aktivira!"
        if odgovor == "prehod":
            self.stanje = "Prehod"
            self.intenziteta += 0.5
            return "Prehod je uspešen, premikamo se naprej."
        if odgovor == "zaključi":
            self.stanje = "Zaključek"
            self.intenziteta = 0
            return "Proces je zaključen."
        return ""

    def preveri_stanje(self) -> tuple[str, float]:
        """Return current state and intensity."""
        return self.stanje, self.intenziteta


class OkenskoSporocilo:
    """Display messages and capture user responses."""

    def __init__(self, sporocilo: str = "Dobrodošli!", input_func: Callable[[str], str] | None = None) -> None:
        self.sporocilo = sporocilo
        self.input_func = input_func or input

    def prikazi_okno(self) -> str:
        """Show the interactive window and obtain the user's choice."""
        print(f"[INTERAKTIVNO OKNO] {self.sporocilo}")
        return self.input_func("Kako želite nadaljevati? (aktiviraj/prehod/zaključi): ")


def interactive_session() -> None:
    """Run a simple interactive session using the Kapacitor."""
    kapacitor = Kapacitor()
    okno = OkenskoSporocilo("Začnimo proces prehoda.")

    while True:
        odgovor = okno.prikazi_okno()
        msg = kapacitor.sprejmi_vhod(odgovor)
        if msg:
            print(f"[OKNO] - {msg}")
        state, _ = kapacitor.preveri_stanje()
        if state == "Zaključek":
            break


if __name__ == "__main__":
    interactive_session()

