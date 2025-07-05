class OntologicalSymbol:
    """Represents a symbolic entity used in ontological modelling."""

    def __init__(self, symbol: str, meaning: str) -> None:
        self.symbol = symbol
        self.meaning = meaning

    def activate(self) -> str:
        """Activate the symbol and return a descriptive message."""
        return f"Simbol '{self.symbol}' aktiviran z pomenom: {self.meaning}"

    def transition(self, new_meaning: str) -> str:
        """Change the meaning of the symbol."""
        old = self.meaning
        self.meaning = new_meaning
        return f"Simbol '{self.symbol}' prehaja iz '{old}' v '{new_meaning}'"


class OntologicalUnit:
    """Represents a basic unit operating in a certain dimension."""

    def __init__(self, unit_name: str, state: str, dimension: str) -> None:
        self.unit_name = unit_name
        self.state = state
        self.dimension = dimension

    def activate(self) -> str:
        return (
            f"Enota {self.unit_name} aktivirana v {self.dimension} "
            f"z začetnim stanjem: {self.state}"
        )

    def transition(self, new_state: str) -> str:
        old = self.state
        self.state = new_state
        return f"Enota {self.unit_name} prehaja iz {old} v {new_state}"

    def change_dimension(self, new_dimension: str) -> str:
        old = self.dimension
        self.dimension = new_dimension
        return f"Enota {self.unit_name} prehaja iz dimenzije {old} v {new_dimension}"
