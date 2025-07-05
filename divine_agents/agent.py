class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Agent name.
    state:
        Initial ontological state (``Ego``, ``Jaz`` or ``Enotnost``).
    tension:
        Initial level of internal tension.
    emotion:
        Initial emotion intensity.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        # value represents a progress metric in the imaginary time cycle
        self.value = 0.0
        self.history = [state]
        self.loop_count = 0

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    # value update methods and imaginary time simulation
    def update_value(self, delta: float = 0.1) -> None:
        """Increase the internal value used to represent imaginary time."""
        self.value = min(1.0, self.value + delta)

    def simulate_imaginary_time(self, cycles: int = 10, delta: float = 0.1) -> list[str]:
        """Run a sequence of state transitions across imaginary time cycles.

        Parameters
        ----------
        cycles:
            Number of imaginary time cycles to execute.
        delta:
            Increment applied to ``value`` each cycle.

        Returns
        -------
        list[str]
            States reached after each cycle.
        """
        results: list[str] = []
        self.loop_count = 0
        while self.loop_count < cycles:
            self.loop_count += 1
            self.update_value(delta)
            # emotion grows with value allowing transitions to occur
            self.update_emotion(self.value)
            results.append(self.transition())
        return results

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
