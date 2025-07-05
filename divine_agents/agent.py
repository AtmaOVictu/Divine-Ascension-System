from .advanced import SelfRegulation, Learning, EmotionalDynamics


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, energy: float = 1.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.energy = energy
        self.history = [state]

        self.regulation = SelfRegulation(self.energy, self.tension)
        self.learning = Learning()
        self.emotions = EmotionalDynamics()

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self.emotions.update_state("veselje" if value > 0 else "tesnoba")

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.self_regulate()

    def self_regulate(self) -> None:
        """Adapt energy based on current tension."""
        self.regulation.tension = self.tension
        self.regulation.energy = self.energy
        self.regulation.adjust()
        self.energy = self.regulation.energy

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        warning = self.emotions.ethical_warning()
        return f"{base} {warning}".strip()

    def record_experience(self, exp: str) -> None:
        """Store an experience for later optimization."""
        self.learning.add_experience(exp)


class MultiDimensionalAgent(Agent):
    """Agent capable of moving through multiple dimensions."""

    def __init__(self, name: str, state: str = "Ego", dimension: int = 1,
                 tension: float = 0.0, emotion: float = 0.0, energy: float = 1.0):
        super().__init__(name, state, tension, emotion, energy)
        self.dimension = dimension

    def move_dimension(self) -> int:
        """Move to the next dimension."""
        self.dimension += 1
        return self.dimension
