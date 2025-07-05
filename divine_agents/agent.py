from __future__ import annotations

from dataclasses import dataclass, field

from .entities import AngelAgent, ShadowAgent


class Agent:
    """Ontological agent capable of transitioning between states.

    Parameters
    ----------
    name:
        Unique name of the agent.
    state:
        Initial ontological state. Must be one of :pydata:`STATES`.
    tension:
        Initial tension value. Clamped between 0 and 1.
    emotion:
        Initial emotion intensity. Clamped between 0 and 1.
    shadow:
        Optional instance of :class:`~divine_agents.entities.ShadowAgent`.
    angel:
        Optional instance of :class:`~divine_agents.entities.AngelAgent`.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        shadow: ShadowAgent | None = None,
        angel: AngelAgent | None = None,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = max(0.0, min(1.0, tension))
        self.emotion = max(0.0, min(1.0, emotion))
        self.history = [state]
        self.shadow = shadow or ShadowAgent(f"{name}-shadow")
        self.angel = angel or AngelAgent(f"{name}-angel")

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = max(0.0, min(1.0, value))
        self.tension = max(0.0, min(1.0, self.tension + self.emotion))

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = max(0.0, min(1.0, value))

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
        if self.emotion > 0.7:
            tone = "z močnimi čustvi"
        elif self.emotion > 0.3:
            tone = "uravnoteženo"
        else:
            tone = "mirno"

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        return f"{base} ({tone})"
