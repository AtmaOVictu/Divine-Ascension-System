from dataclasses import dataclass, field
from typing import List, Dict, Tuple


@dataclass
class Agent:
    """Ontological agent capable of state transitions and learning."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    loyalty: float = 0.5
    experiences: List[str] = field(default_factory=list)
    history: List[str] = field(default_factory=lambda: ["Ego"])

    STATES = ("Ego", "Jaz", "Enotnost")

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform simple state transition if thresholds are exceeded."""
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


class MultiLayerTransitionSystem:
    """Handle more complex transitions considering additional layers."""

    def __init__(self, agent: Agent) -> None:
        self.agent = agent

    def multi_layer_transition(self) -> str:
        emotion_layer = self.agent.emotion
        tension_layer = self.agent.tension
        loyalty_layer = self.agent.loyalty
        experience_layer = (
            self.agent.experiences[-1] if self.agent.experiences else "neutral"
        )

        if emotion_layer > 0.5 or tension_layer > 0.7:
            if self.agent.state == "Ego" and loyalty_layer > 0.3:
                self.agent.state = "Jaz"
            elif self.agent.state == "Jaz" and "selfless" in experience_layer:
                self.agent.state = "Enotnost"

        self.agent.history.append(self.agent.state)
        return self.agent.state


class ExperienceBasedLearning:
    """Simple reinforcement-like learning for agents."""

    def __init__(self, agent: Agent) -> None:
        self.agent = agent
        self.q_table: Dict[Tuple[str, str], float] = {}

    def update_experience(self, situation: str, reward: float) -> None:
        state = self.agent.state
        key = (state, situation)
        self.q_table[key] = self.q_table.get(key, 0.0) + reward

    def decide(self, situation: str) -> str:
        key = (self.agent.state, situation)
        return (
            "Act selflessly" if self.q_table.get(key, 0.0) > 0 else "Self-preservation"
        )
