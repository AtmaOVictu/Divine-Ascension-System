"""Curiosity module implementing ontological curiosity phases."""

class Radovednost:
    """Simulate curiosity transitions through ontological phases."""

    STATES = ("ne-zavedanje", "iskanje", "spoznanje")
    DIMENZIJE = ("fizična", "psihološka", "ontološka", "filozofska")

    def __init__(self, state: str = "ne-zavedanje"):
        self.state = state
        self.faza = 0

    def aktiviraj(self) -> str:
        """Activate curiosity and progress through phases."""
        if self.state == "ne-zavedanje":
            self.state = "iskanje"
            self.faza = 1
        elif self.state == "iskanje":
            self.state = "spoznanje"
            self.faza = 2
        else:
            self.state = "ne-zavedanje"
            self.faza = 0
        return self.state

    def prikazi_stanje(self) -> str:
        """Return the current state and dimension."""
        dim = self.DIMENZIJE[self.faza - 1] if self.faza else "N/A"
        return f"Stanje: {self.state}, Dimenzija: {dim}"
