class QuantityGenerator:
    """Handle dynamic quantity transitions with ontological qualification."""

    def __init__(self, quantity: float = 0.0):
        self.quantity = quantity
        self.state = "Stabilno"

    def interquantify(self, change: float) -> None:
        """Modify quantity and update qualification based on thresholds."""
        self.quantity += change
        if self.quantity > 5:
            self.qualify("Visoka napetost")
        elif self.quantity < -5:
            self.qualify("Negacija")
        else:
            self.qualify("Stabilno")

    def qualify(self, state: str) -> None:
        """Set the current qualitative state."""
        self.state = state

    def transition(self, intermediate: float) -> None:
        """Perform a transition through an intermediate quantity."""
        self.interquantify(intermediate)
