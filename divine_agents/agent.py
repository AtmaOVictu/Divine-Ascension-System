from dataclasses import dataclass, field
from typing import List, Literal


State = Literal["Ego", "Jaz", "Enotnost"]


@dataclass
class Agent:
    """An ontological agent capable of transitioning through defined states."""

    name: str
    state: State = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    history: List[State] = field(default_factory=list)

    def __post_init__(self) -> None:
        """Initialize the agent's history with its starting state."""
        self.history.append(self.state)

    def update_emotion(self, value: float) -> None:
        """Set emotion intensity and increment tension.

        Parameters
        ----------
        value: float
            New emotion value in the range ``0.0`` to ``1.0``.
        """
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Set the agent's tension level.

        Parameters
        ----------
        value: float
            Tension value in the range ``0.0`` to ``1.0``.
        """
        self.tension = value

    def transition(self) -> State:
        """Transition to the next state when thresholds are exceeded.

        Returns
        -------
        State
            The new state after transition (may be unchanged).
        """
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Answer a question according to the agent's current state.

        Parameters
        ----------
        question: str
            The asked question (currently unused).

        Returns
        -------
        str
            A philosophical response aligned with the current state.
        """
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
