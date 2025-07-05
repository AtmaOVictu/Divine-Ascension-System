import math
from dataclasses import dataclass, field
from typing import List


def logistic_function(t: float, k: float, c: float) -> float:
    """Compute logistic transition value."""
    return 1 / (1 + math.exp(-k * (t - c)))


def exponential_transition(t: float, k: float) -> float:
    """Compute exponential transition value."""
    return 1 - math.exp(-k * t)


@dataclass
class AgentWithContradictions:
    """Agent that evolves through ontological states with contradictions."""

    name: str
    k_bio: float = 1.0
    c_bio: float = 0.5
    k_soc: float = 1.5
    c_soc: float = 0.6
    tension: float = 0.0
    emotion: float = 0.0
    shadow: float = 0.0
    state: str = "Ego"
    history: List[str] = field(default_factory=lambda: ["Ego"])

    def update_emotion(self, emotion_value: float, shadow_value: float) -> None:
        """Update emotion and its opposite (shadow) to adjust tension."""
        self.emotion = emotion_value
        self.shadow = shadow_value
        self.tension += self.emotion + self.shadow

    def evolve(self) -> None:
        """Evolve tension through logistic transitions."""
        bio = logistic_function(self.tension, self.k_bio, self.c_bio)
        soc = logistic_function(self.tension, self.k_soc, self.c_soc)
        self.tension = bio + soc

    def transition(self) -> str:
        """Transition ontological state based on tension or emotion."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Respond according to current ontological state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."


def philosophical_debate(agent1: AgentWithContradictions, agent2: AgentWithContradictions) -> List[str]:
    """Simulate a short debate between two agents."""
    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.6, -0.2)
    agent1.evolve()
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.4, 0.3)
    agent2.evolve()
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines
