class Intensity:
    """Handle intensity states and color mapping."""

    def __init__(self, stanje: str = "stabilnost") -> None:
        self.stanje = stanje
        self.intenziteta = 0.0

    def povecaj_intenziteto(self) -> str:
        """Increase intensity based on current state and return color."""
        if self.stanje == "visoka napetost":
            self.intenziteta += 0.8
            barva = "Rde\u010da"
        elif self.stanje == "prehod":
            self.intenziteta += 0.5
            barva = "Rumena"
        elif self.stanje == "stabilnost":
            self.intenziteta += 0.2
            barva = "Zelena"
        elif self.stanje == "razjasnitev":
            self.intenziteta += 0.3
            barva = "Modra"
        elif self.stanje == "negacija":
            self.intenziteta = 0
            barva = "\u010crna"
        else:
            barva = "Brez"
        return barva
