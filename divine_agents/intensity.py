class Intensity:
    """Represents the intensity of an agent's state using color cues."""

    COLOR_CODES = {
        "visoka napetost": "Rde\u010da",
        "prehod": "Rumena",
        "stabilnost": "Zelena",
        "razjasnitev": "Modra",
        "negacija": "\u010crna",
    }

    def __init__(self, stanje: str = "stabilnost") -> None:
        self.stanje = stanje
        self.intenziteta = 0.0

    def povecaj(self) -> None:
        """Increase intensity based on the current state."""
        if self.stanje == "visoka napetost":
            self.intenziteta += 0.8
        elif self.stanje == "prehod":
            self.intenziteta += 0.5
        elif self.stanje == "stabilnost":
            self.intenziteta += 0.2
        elif self.stanje == "razjasnitev":
            self.intenziteta += 0.3
        elif self.stanje == "negacija":
            self.intenziteta = 0

    def prikazi(self) -> str:
        """Return a string describing the intensity with a color."""
        barva = self.COLOR_CODES.get(self.stanje, "Bela")
        value = self.intenziteta
        desc = f"Intenziteta je {value} in stanje je ozna\u010deno z barvo {barva}."
        return desc.upper() if value > 0.7 else desc
