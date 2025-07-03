class EgoComponent:
    """Represents the Ego aspect tracking its reaction to urgency."""

    def __init__(self) -> None:
        self.state = 0  # -1 negative, 0 neutral, 1 positive

    def react(self, urgency: int) -> str:
        """Adjust internal state based on urgency level."""
        if urgency == -1:
            self.state = -1
            return "Ego zavra\u010da nalogo."
        if urgency == 0:
            self.state = 0
            return "Ego ostaja v stabilnem stanju."
        if urgency == 1:
            self.state = 1
            return "Ego sprejema nalogo."
        return "Neprepoznana nujnost."


class JazComponent:
    """Represents the Jaz aspect reacting to urgency and oscillating with Ego."""

    def __init__(self) -> None:
        self.state = 0  # -1 negative, 0 neutral, 1 positive

    def react(self, urgency: int) -> str:
        """Adjust internal state based on urgency level."""
        if urgency == -1:
            self.state = -1
            return "Jaz umika nalogo."
        if urgency == 0:
            self.state = 0
            return "Jaz ostaja v nevtralnem stanju."
        if urgency == 1:
            self.state = 1
            return "Jaz sprejema nalogo in napreduje."
        return "Neprepoznana nujnost."

    def oscillate(self) -> str:
        """Describe oscillation with Ego based on current state."""
        if self.state == -1:
            return "Oscilacija: Negativno stanje - Jaz in Ego se zavra\u010data."
        if self.state == 0:
            return "Oscilacija: Nevtralno stanje - Jaz in Ego sta stabilna."
        if self.state == 1:
            return "Oscilacija: Pozitivno stanje - Jaz in Ego sprejemata nalogo in napredujeta."
        return "Neprepoznano stanje."
