class Generator:
    """Ontological generator controlling transitions in the system."""

    def __init__(self, aktiviran: bool = False) -> None:
        self.aktiviran = aktiviran
        self.energija = 0.0

    def aktiviraj(self) -> None:
        """Activate the generator."""
        self.aktiviran = True
        self.energija = 1.0

    def generiraj_prehod(self, stanje: str) -> str:
        """Generate transition based on the given state."""
        if not self.aktiviran:
            return "Generator ni aktiviran, ni mogoče generirati prehoda."

        if stanje == "0":
            self.energija += 0.3
            return f"Energija: {self.energija} – Prehod iz potencialnosti."
        if stanje == "1":
            self.energija += 0.5
            return f"Energija: {self.energija} – Prehod v dejanskost."
        if stanje == "⊘":
            self.energija = 0.0
            return "Generator se ustavi, prekinitev."
        return "Stanje ni prepoznano."
