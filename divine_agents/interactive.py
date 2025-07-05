class Kapacitor:
    """Simple handler for user input based transitions."""

    def __init__(self):
        self.state = "Začetno"
        self.intensity = 0.0

    def process_input(self, command: str) -> str:
        """Process a textual command and update internal state."""
        if command == "aktiviraj":
            self.state = "Aktivacija"
            self.intensity += 0.3
            return "Sistem se aktivira!"
        if command == "prehod":
            self.state = "Prehod"
            self.intensity += 0.5
            return "Prehod je uspešen, premikamo se naprej."
        if command == "zaključi":
            self.state = "Zaključek"
            self.intensity = 0.0
            return "Proces je zaključen."
        return "Nepoznan ukaz."

    def status(self) -> str:
        """Return current state description."""
        return f"Trenutno stanje: {self.state}, intenziteta: {self.intensity}"


class OkenskoSporocilo:
    """Basic window simulator for interactions."""

    def __init__(self, message: str = "Dobrodošli!"):
        self.message = message

    def prompt(self, user_response: str) -> str:
        """Simulate showing a message and processing a response."""
        kapacitor = Kapacitor()
        result = kapacitor.process_input(user_response)
        return result
