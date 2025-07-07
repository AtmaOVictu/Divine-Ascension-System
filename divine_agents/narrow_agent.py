from .agent import Agent


class NarrowAgent(Agent):
    """A specialised agent focused on a narrow task."""

    def __init__(self, name: str, threshold: float = 0.5, state: str = "Ego",
                 tension: float = 0.0, emotion: float = 0.0):
        super().__init__(name, state, tension, emotion)
        self.threshold = threshold
        self.value = 0.0

    def update_value(self, value: float) -> None:
        self.value = value
        if self.value > self.threshold:
            self.tension = self.value
            self.transition()
