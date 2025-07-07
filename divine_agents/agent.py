from typing import Callable, List


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

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

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."


class InsertionAgent(Agent):
    """Agent with dynamic insertion capabilities."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        super().__init__(name, state, tension, emotion)
        self.knowledge: List[str] = []
        self.behavior: Callable[[str], str] | None = None

    def insert_knowledge(self, fact: str) -> None:
        """Dynamically add knowledge that influences responses."""
        self.knowledge.append(fact)

    def insert_state(self, state: str) -> None:
        """Directly set a new ontological state."""
        self.state = state

    def insert_behavior(self, behavior: Callable[[str], str]) -> None:
        """Set a callable that transforms responses."""
        self.behavior = behavior

    def respond(self, question: str) -> str:
        response = super().respond(question)
        if self.behavior:
            response = self.behavior(response)
        if self.knowledge:
            response = f"{response} {' '.join(self.knowledge)}"
        return response
