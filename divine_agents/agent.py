from typing import List, Tuple


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.speed = 0.0
        self.direction: Tuple[int, int] = (0, 0)
        self.past_tension: List[float] = []

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self.past_tension.append(self.tension)
        if len(self.past_tension) > 5:
            self.past_tension.pop(0)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.past_tension.append(self.tension)
        if len(self.past_tension) > 5:
            self.past_tension.pop(0)

    def interact_with(self, other: "Agent") -> None:
        """Influence another agent's tension based on this agent's emotion."""
        if self.emotion > 0.5:
            other.tension += 0.1
        elif self.emotion < -0.5:
            other.tension = max(0.0, other.tension - 0.1)

    def move(self) -> Tuple[float, Tuple[int, int]]:
        """Determine movement based on current emotion."""
        if self.emotion > 0.5:
            self.speed = 2 * (1 + self.emotion)
            self.direction = (1, 0)
        elif self.emotion < -0.5:
            self.speed = 1 * (1 + abs(self.emotion))
            self.direction = (-1, 0)
        else:
            self.speed = 0.5
            self.direction = (0, 0)
        return self.speed, self.direction

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

        if self.emotion > 0.5:
            base += " Čutim močna čustva ob tej misli."
        elif self.emotion < -0.5:
            base += " Ta misel me pomirja."

        return base
