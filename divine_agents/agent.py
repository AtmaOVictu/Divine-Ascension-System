"""Agent module implementing ontological state transitions and interactions."""

import random


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        tasks=None,
        beliefs=None,
        team=None,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.tasks = tasks or []
        self.beliefs = beliefs or []
        self.team = team

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def add_task(self, task: str) -> None:
        """Assign a new task to the agent."""
        self.tasks.append(task)

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

    def interact(self, other: "Agent") -> str:
        """Interact with another agent and possibly trigger a state change."""
        feedback = random.choice(
            ["pozitivno", "negativno", "nevtralno", "strah", "jeza", "veselje"]
        )
        if feedback in {"strah", "jeza"}:
            self.update_emotion(0.6)
        else:
            self.update_emotion(0.3)
        previous = self.state
        self.transition()
        return (
            f"{self.name} komunicira z {other.name}. Povratna informacija: {feedback}. "
            f"Stanje: {previous} -> {self.state}"
        )

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
