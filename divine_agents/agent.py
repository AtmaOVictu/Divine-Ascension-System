from __future__ import annotations

from typing import Dict, List


class Agent:
    """Ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")
    EMOTION_KEYS = ("anger", "joy", "fear")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotions: Dict[str, float] | None = None,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotions: Dict[str, float] = emotions or {
            key: 0.0 for key in self.EMOTION_KEYS
        }
        self.history: List[str] = [state]

    def update_emotion(self, emotion_type: str, value: float) -> None:
        """Update an emotion value and recalculate tension."""
        if emotion_type in self.emotions:
            self.emotions[emotion_type] = value
        self.calculate_tension()

    def calculate_tension(self) -> None:
        """Recalculate tension as the average of emotion values."""
        self.tension = sum(self.emotions.values()) / len(self.emotions)

    def update_tension(self, value: float) -> None:
        """Directly set the tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform a state transition if thresholds are exceeded."""
        if self.tension > 0.7 or any(e > 0.5 for e in self.emotions.values()):
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


class AgentWithHistory(Agent):
    """Agent that keeps detailed history of decisions."""

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotions: Dict[str, float] | None = None,
        history: List[dict] | None = None,
    ) -> None:
        super().__init__(name, state, tension, emotions)
        if history is not None:
            self.history = history  # type: ignore[assignment]

    def update_history(self) -> None:
        """Record current state, emotion and tension."""
        self.history.append(
            {"state": self.state, "emotion": self.emotions.copy(), "tension": self.tension}
        )

    def transition(self) -> str:
        """Transition considering recent history as well."""
        if len(self.history) > 3:
            recent_entries = [h for h in self.history if isinstance(h, dict)][-3:]
            if len(recent_entries) == 3:
                avg_tension = sum(h["tension"] for h in recent_entries) / 3
                if avg_tension > 0.6:
                    self.state = "Jaz"
                elif avg_tension > 0.5:
                    self.state = "Enotnost"
        super().transition()
        self.update_history()
        return self.state


class EmotionalAgent(Agent):
    """Agent capable of influencing another agent during interaction."""

    def interact(self, other_agent: Agent) -> None:
        """Modify both agents' emotional state during interaction."""
        if self.state != other_agent.state:
            mutual = min(self.tension, other_agent.tension) * 0.1
            self.tension += mutual
            other_agent.tension += mutual
            self.update_emotion("anger", self.emotions["anger"] + mutual)
            other_agent.update_emotion("fear", other_agent.emotions["fear"] + mutual)
