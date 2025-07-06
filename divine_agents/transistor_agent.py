class TransistorAgent:
    """Simulates a transistor as an ontological agent."""

    def __init__(self, name: str, state: str = "off"):
        self.name = name
        self.state = state
        self.signal_in = 0.0
        self.signal_out = 0.0

    def receive_signal(self, input_signal: float) -> None:
        """Receive an input signal expressed in volts."""
        self.signal_in = input_signal

    def switch_state(self) -> None:
        """Switch state based on the received signal."""
        if self.signal_in >= 1:
            self.state = "on"
        else:
            self.state = "off"

    def output_signal(self) -> float:
        """Return output signal depending on current state."""
        self.signal_out = 5 if self.state == "on" else 0
        return self.signal_out

    def transition(self, input_signal: float) -> float:
        """Perform full transition cycle with a given input signal."""
        self.receive_signal(input_signal)
        self.switch_state()
        return self.output_signal()
