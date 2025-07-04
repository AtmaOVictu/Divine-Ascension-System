class LJUBEZEN:
    """Represents the process of love used to illustrate additional dynamics."""

    def __init__(self) -> None:
        self.state = 0  # 0 - negation, 1 - activation, 2 - change, 3 - harmony

    def aktivacija(self) -> str:
        self.state = 1
        return "LJUBEZEN: Prehod iz ni\u010d v enoto (aktivacija)."

    def sprememba(self) -> str:
        self.state = 2
        return "LJUBEZEN: Prehod v novo stanje (sprememba)."

    def harmonija(self) -> str:
        self.state = 3
        return "LJUBEZEN: Dose\u017eena harmonija (ljubezen kot temeljni proces)."
