class Volja:
    """Dynamic impulse of will."""
    def __init__(self):
        self.state = 0  # 0 = negation / idle

    def aktivacija(self) -> str:
        """Activate the will, moving from nothingness to action."""
        self.state = 1
        return "Volja je aktivirana: prehod iz nič v enoto."

    def sprememba(self) -> str:
        """Trigger a change into a new phase."""
        self.state = 2
        return "Volja je sprožila spremembo, prehod v novo fazo."


class Vera:
    """Dynamic impulse of faith."""
    def __init__(self):
        self.state = 0  # 0 = negation / unaware

    def potrditev(self) -> str:
        """Confirm faith as the foundation of reality."""
        self.state = 1
        return "Vera je postala temelj, prepoznavanje temeljev realnosti."

    def prepoznavanje(self) -> str:
        """Recognize the unknown, expanding horizons."""
        self.state = 2
        return "Vera prepoznava neznano, omogoča širjenje obzorij in rasti."


class Vzgib:
    """Combination of will and faith impulses."""
    def __init__(self):
        self.volja = Volja()
        self.vera = Vera()

    def izvajanje(self):
        """Activate both impulses and return their messages."""
        volja_result = self.volja.aktivacija()
        vera_result = self.vera.potrditev()
        return volja_result, vera_result

