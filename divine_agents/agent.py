class Agent:
    """Represents an ontological agent capable of transitioning states and RES phases."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, phase: int = 1):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.phase = phase  # RES phase from 1 to 100
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    # RES phase manipulation methods
    def evolve(self) -> int:
        """Progress to the next RES phase."""
        if self.phase < 100:
            self.phase += 1
        return self.phase

    def degrade(self) -> int:
        """Move backwards in RES phases."""
        if self.phase > 1:
            self.phase -= 1
        return self.phase

    def permute(self) -> int:
        """Randomly adjust the RES phase within a small range."""
        import random

        self.phase = max(1, min(100, self.phase + random.choice([-1, 0, 1])))
        return self.phase

    def phase_label(self) -> str:
        """Return formatted RES phase label."""
        return f"RES{self.phase:03d}"

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
            self.evolve()
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        emotion_prefix = "" if self.emotion < 0.3 else "(čustveno) "
        if self.state == "Ego":
            return emotion_prefix + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return emotion_prefix + "Resnica je relativna, oblikovana z našimi odnosi."
        return emotion_prefix + "Vse resnice so eno, medsebojno povezane."
