from .agent import Agent


class MultiDimensionalAgent(Agent):
    """Agent with multiple dimensions influencing behavior."""

    def __init__(self, name: str, dimensions: dict | None = None, **kwargs) -> None:
        super().__init__(name, **kwargs)
        self.dimensions = dimensions or {"time": 0, "space": 0, "emotion": 0, "tension": 0}

    def update_dimension(self, dimension: str, value: float) -> None:
        self.dimensions[dimension] = value
        if dimension == "emotion":
            self.update_emotion(value)
        if dimension == "tension":
            self.update_tension(value)

    def transition(self) -> str:
        emotion_level = self.dimensions.get("emotion", 0)
        if emotion_level > 0.6:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
            self.history.append(self.state)
            return self.state
        return super().transition()
