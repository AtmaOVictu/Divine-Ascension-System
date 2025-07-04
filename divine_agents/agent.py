class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name : str
        Agent identifier.
    state : str, optional
        Ontological state of the agent. Must be one of :data:`STATES`.
    tension : float, optional
        Current tension level (0-1).
    emotion : float, optional
        Current emotional intensity (0-1).
    phase : int, optional
        Evolutionary phase from 1 to 100.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, phase: int = 1):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.phase = max(1, min(phase, 100))
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    # Evolution, permutation and degradation -------------------------------
    def evolve(self) -> int:
        """Advance the phase when growth conditions are met."""
        if self.phase < 100:
            self.phase += 1
        return self.phase

    def permute(self) -> int:
        """Slightly adjust the phase to reflect reconfiguration."""
        if 1 < self.phase < 100:
            self.phase = min(100, self.phase + 5)
        return self.phase

    def degrade(self) -> int:
        """Reduce the phase to represent a setback."""
        if self.phase > 1:
            self.phase -= 1
        return self.phase

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            self.evolve()
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        else:
            # Without sufficient drive the agent slowly degrades
            self.degrade()
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            answer = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            answer = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            answer = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.5:
            answer += " Čutim močna čustva ob tem spoznanju." 
        return answer
