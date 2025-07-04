class BaseProcess:
    """Base class for spiritual processes like VERA, VOLJA, and LJUBEZEN."""

    def __init__(self, name: str):
        self.name = name
        self.state = 0  # 0 = negation, 1 = aktivacija, 2 = sprememba, 3 = harmonija

    def aktivacija(self) -> str:
        self.state = 1
        return f"{self.name}: Prehod iz nič v enoto (aktivacija)."

    def sprememba(self) -> str:
        self.state = 2
        return f"{self.name}: Prehod v novo stanje (sprememba)."

    def harmonija(self) -> str:
        self.state = 3
        return f"{self.name}: Dosežena harmonija."


class VERA(BaseProcess):
    def __init__(self):
        super().__init__("VERA")


class VOLJA(BaseProcess):
    def __init__(self):
        super().__init__("VOLJA")


class LJUBEZEN(BaseProcess):
    def __init__(self):
        super().__init__("LJUBEZEN")
