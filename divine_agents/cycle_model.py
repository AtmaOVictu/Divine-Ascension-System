class CycleModel:
    """Model representing a simple cyclic animation state."""

    def __init__(self):
        self.angle = 0
        self.color = "blue"

    def step(self):
        """Advance the cycle by one step.

        Returns a tuple of (angle, color, changed) where ``changed`` is True
        if the color changed in this step.
        """
        self.angle = (self.angle + 1) % 360
        changed = False
        if self.angle % 60 == 0:
            self.color = "red" if self.color == "blue" else "blue"
            changed = True
        return self.angle, self.color, changed
