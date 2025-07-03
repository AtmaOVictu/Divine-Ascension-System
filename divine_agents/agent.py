"""Ontological agents capable of transitioning between philosophical states."""

from __future__ import annotations


class Agent:
    """Represents an ontological agent with emotional dynamics."""

    STATES = ("Ego", "Jaz", "Enotnost")
    WORLDS = ("Miza", "Svet", "Vest")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        world: str = "Miza",
        tension: float = 0.0,
        emotion: float = 0.0,
    ) -> None:
        self.name = name
        self.state = state
        self.world = world
        self.tension = tension
        self.emotion = emotion
        self.history: list[str] = [state]

    def __repr__(self) -> str:
        return (
            f"Agent(name={self.name}, state={self.state}, world={self.world}, "
            f"tension={self.tension}, emotion={self.emotion})"
        )

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def change_world(self, new_world: str) -> None:
        """Switch the agent's world if valid."""
        if new_world in self.WORLDS:
            self.world = new_world

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
        prefix = f"(emocija: {self.emotion:.2f}) "
        if self.state == "Ego":
            return prefix + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return prefix + "Resnica je relativna, oblikovana z našimi odnosi."
        return prefix + "Vse resnice so eno, medsebojno povezane."
