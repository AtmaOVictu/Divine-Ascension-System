class RealDataConnection:
    """Simulate connection to real sensors."""

    def __init__(self, stres: int = 0, razpolozenje: int = 0):
        self.stres = stres
        self.razpolozenje = razpolozenje

    def read_data(self) -> str:
        if self.stres > 7:
            return "Visok stres! Potreben je prehod v stabilnost."
        if self.razpolozenje < 3:
            return "Slabo razpolozenje! Prehod v čustveno harmonijo."
        return f"Stres: {self.stres}, Razpoloženje: {self.razpolozenje}"
