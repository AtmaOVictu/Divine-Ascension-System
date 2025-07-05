from __future__ import annotations

import random
from typing import Dict, List


class Agent:
    """Represents an ontological agent capable of transitioning states.

    The agent keeps track of its emotional and tension history and can be
    extended with additional behaviour through subclassing.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0) -> None:
        self.name: str = name
        self.state: str = state
        self.tension: float = tension
        self.emotion: float = emotion
        self.history: List[str] = [state]
        self.external_factors: Dict[str, float] = {}

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self.history.append(f"Emotion: {value}")

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.history.append(f"Tension: {value}")

    def update_external_factors(self, factor: str, value: float) -> None:
        """Store an external factor influencing the agent."""
        self.external_factors[factor] = value
        self.history.append(f"External factor {factor}: {value}")

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


class SimulationPhase:
    """Represents a stage in which an agent can experience moral dilemmas."""

    def __init__(self, phase_name: str, moral_dilemma: bool = False) -> None:
        self.phase_name = phase_name
        self.moral_dilemma = moral_dilemma

    def run(self, agent: Agent) -> None:
        """Execute the simulation phase, optionally presenting a dilemma."""
        if self.moral_dilemma:
            self.handle_moral_dilemma(agent)

    def handle_moral_dilemma(self, agent: Agent) -> None:
        if agent.state == "Ego":
            decision = "change" if agent.tension > 0.8 else "continue"
            agent.history.append(f"Moral dilemma decision: {decision}")


class LearningAgent(Agent):
    """Agent variant that learns from its previous states."""

    def __init__(self, name: str, state: str = "Ego") -> None:
        super().__init__(name, state)
        self.learning_history: List[str] = []

    def learn_from_past(self) -> None:
        if self.history:
            last_state = self.history[-1]
            self.learning_history.append(last_state)

    def adapt_to_environment(self) -> None:
        if self.learning_history:
            _ = self.learning_history[-1]


class InteractionAgent(Agent):
    """Agent capable of interacting with another agent."""

    def __init__(self, name: str, state: str = "Ego") -> None:
        super().__init__(name, state)
        self.interaction_history: List[str] = []

    def interact(self, other: "InteractionAgent") -> None:
        if self.state == other.state:
            outcome = "cooperate"
        else:
            outcome = "compete"
        self.interaction_history.append(outcome)
        other.interaction_history.append(outcome)


class FreeWillAgent(Agent):
    """Agent that can make stochastic decisions."""

    def make_decision(self) -> str:
        decision_point = random.random()
        decision = "bold" if decision_point > 0.5 else "cautious"
        self.history.append(f"Decision: {decision}")
        return decision
