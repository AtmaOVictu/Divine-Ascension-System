"""
Generator predstavlja ontoloski motor, ki s svojo aktivacijo spodbuja prehode skozi razlicne faze sistema.
"""



class Generator:
    """Ontological generator enabling dynamic transitions in the system."""

    def __init__(self, aktiviran: bool = False):
        self.aktiviran = aktiviran
        self.energija = 0.0

    def aktiviraj(self) -> None:
        """Activate the generator and start energy generation."""
        self.aktiviran = True
        self.energija = 1.0

    def generiraj_prehod(self, stanje: str) -> str:
        """Generate phase transitions based on the provided state."""
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
            self.aktiviran = False
            return "Generator se ustavi, prekinitev."
        return "Stanje ni prepoznano."
