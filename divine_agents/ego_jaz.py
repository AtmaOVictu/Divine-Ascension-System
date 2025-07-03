class Ego:
    """Represents the Ego component with a simple reactive state."""

    def __init__(self):
        self.state = 0  # Neutral state

    def react_to_necessity(self, level: int) -> None:
        """Adjust state based on necessity level."""
        if level == -1:
            self.state = -1
            print("Ego zavra\u010da nalogo.")
        elif level == 0:
            self.state = 0
            print("Ego ostaja v stabilnem stanju.")
        elif level == 1:
            self.state = 1
            print("Ego sprejema nalogo.")
        else:
            print("Neprepoznana nujnost.")


class Jaz:
    """Represents the Jaz component capable of simple oscillation."""

    def __init__(self):
        self.state = 0  # Neutral

    def react(self, level: int) -> None:
        """Adjust internal state according to necessity."""
        if level == -1:
            self.state = -1
            print("Jaz umika nalogo.")
        elif level == 0:
            self.state = 0
            print("Jaz ostaja v nevtralnem stanju.")
        elif level == 1:
            self.state = 1
            print("Jaz sprejema nalogo in napreduje.")
        else:
            print("Neprepoznana nujnost.")

    def oscillate(self) -> None:
        """Demonstrate oscillation between Ego and Jaz."""
        if self.state == -1:
            print("Osclacija: Negativno stanje - Jaz in Ego se zavra\u010data.")
        elif self.state == 0:
            print("Oscilacija: Nevtralno stanje - Jaz in Ego sta stabilna.")
        elif self.state == 1:
            print("Oscilacija: Pozitivno stanje - Jaz in Ego sprejemata nalogo in napredujeta.")

