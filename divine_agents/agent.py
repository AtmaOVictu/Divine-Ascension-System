from __future__ import annotations

from typing import List, Optional


class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Unique identifier for the agent.
    state:
        Initial ontological state. Defaults to ``"Ego"``.
    tension:
        Current level of tension.
    emotion:
        Current emotion intensity.
    beliefs:
        Optional list of beliefs held by the agent.
    parent:
        Optional reference to a parent agent.
    children:
        Optional list used to store created child agents.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        beliefs: Optional[List[str]] = None,
        parent: Optional[Agent] = None,
        children: Optional[List[Agent]] = None,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.beliefs = beliefs or []
        self.parent = parent
        self.children = children or []
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

    def inherit_from_parent(self) -> None:
        """Copy beliefs and emotion from the parent agent, if any."""
        if not self.parent:
            return
        self.beliefs = list(self.parent.beliefs)
        self.emotion = self.parent.emotion

    def create_child(self, name: str, state: Optional[str] = None) -> Agent:
        """Create a child agent inheriting traits from this agent."""
        child = Agent(
            name=name,
            state=state or self.state,
            tension=0.0,
            emotion=0.0,
            parent=self,
            beliefs=[],
        )
        child.inherit_from_parent()
        self.children.append(child)
        return child
