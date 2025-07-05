class Kapacitor:
    """Simple capacitor that processes user input to drive state changes."""

    def __init__(self) -> None:
        self.stanje = "Začetno"
        self.intenziteta = 0.0

    def sprejmi_vhod(self, odgovor: str) -> None:
        """Process user input and update internal state."""
        if odgovor == "aktiviraj":
            self.stanje = "Aktivacija"
            self.intenziteta += 0.3
            self.prikazi_sporocilo("Sistem se aktivira!")
        elif odgovor == "prehod":
            self.stanje = "Prehod"
            self.intenziteta += 0.5
            self.prikazi_sporocilo("Prehod je uspesen, premikamo se naprej.")
        elif odgovor == "zaključi":
            self.stanje = "Zaključek"
            self.intenziteta = 0
            self.prikazi_sporocilo("Proces je zaključen.")

    def prikazi_sporocilo(self, sporocilo: str) -> None:
        """Display a message to the user (simulated window)."""
        print(f"[OKNO] - {sporocilo}")

    def preveri_stanje(self) -> str:
        """Return a string describing the current state."""
        return f"Trenutno stanje: {self.stanje}, intenziteta: {self.intenziteta}"


class OkenskoSporocilo:
    """Simple dialog window used to retrieve user choice."""

    def __init__(self, sporocilo: str = "Dobrodošli!") -> None:
        self.sporocilo = sporocilo

    def prikazi_okno(self, vnos: str | None = None) -> str:
        """Return the user choice. If *vnos* is provided it's returned directly."""
        print(f"[INTERAKTIVNO OKNO] {self.sporocilo}")
        if vnos is not None:
            return vnos
        return ""


class ModularnoOkno:
    """Window that can be extended with different modules."""

    def __init__(self, ime: str = "Modularni sistem") -> None:
        self.ime = ime

    def dodaj_modul(self, modul: str) -> str:
        """Add a module and return the action performed."""
        print(f"[MODUL] Dodajanje modula: {modul}")
        if modul == "Pomoč":
            return "Tukaj so navodila za pomoč..."
        if modul == "Povratne informacije":
            return "Vnesite povratne informacije o procesu."
        return ""

    def prikazi_okno(self, izbran_modul: str) -> str:
        """Simulate showing the window and adding the selected module."""
        print(f"[OKNO] {self.ime} je pripravljen na interakcijo.")
        return self.dodaj_modul(izbran_modul)
