"""Extended agent classes and utilities."""
from __future__ import annotations

from typing import List
import random

from .agent import Agent


class SimulationPhase:
    """Represents a phase that can challenge an agent with dilemmas."""

    def __init__(self, name: str, moral_dilemma: bool = False) -> None:
        self.name = name
        self.moral_dilemma = moral_dilemma

    def run(self, agent: Agent) -> None:
        print(f"Running phase: {self.name}")
        if self.moral_dilemma:
            self.handle_moral_dilemma(agent)

    def handle_moral_dilemma(self, agent: Agent) -> None:
        if agent.state == "Ego":
            decision = "change" if agent.tension > 0.8 else "continue"
            print(f"Agent {agent.name} faces a moral dilemma and decides to {decision}.")
            agent.history.append(f"Moral dilemma decision: {decision}")


class LearningAgent(Agent):
    """Agent that learns from past transitions."""

    def __init__(self, name: str, state: str = "Ego") -> None:
        super().__init__(name, state)
        self.learning_history: List[str] = []

    def learn_from_past(self) -> None:
        if self.history:
            last_state = self.history[-1]
            self.learning_history.append(last_state)
            print(f"Learning from past: {last_state}")

    def adapt_to_environment(self) -> None:
        if self.learning_history:
            print(f"Adapting based on learning history: {self.learning_history[-1]}")


class InteractionAgent(Agent):
    """Agent capable of interacting with another agent."""

    def __init__(self, name: str, state: str = "Ego") -> None:
        super().__init__(name, state)
        self.interaction_history: List[str] = []

    def interact(self, other: "InteractionAgent") -> str:
        print(f"{self.name} interacts with {other.name}")
        if self.state == other.state:
            outcome = "cooperate"
        else:
            outcome = "compete"
        self.interaction_history.append(outcome)
        other.interaction_history.append(outcome)
        print(f"Interaction result: {outcome}")
        return outcome


class FreeWillAgent(Agent):
    """Agent that can make random decisions representing free will."""

    def make_decision(self) -> str:
        decision_point = random.random()
        if decision_point > 0.5:
            decision = "bold"
            print(f"Agent {self.name} decides to make a bold choice!")
        else:
            decision = "cautious"
            print(f"Agent {self.name} decides to stay cautious.")
        self.history.append(f"Decision: {decision}")
        return decision


def visualize_agent(agent: Agent) -> None:
    """Visualize an agent's tension and emotion."""
    import matplotlib.pyplot as plt

    plt.figure(figsize=(5, 5))
    color_map = {"Ego": "red", "Jaz": "blue", "Enotnost": "green"}
    plt.scatter(
        agent.tension,
        agent.emotion,
        color=color_map.get(agent.state, "black"),
    )
    plt.title(f"Agent: {agent.name}, State: {agent.state}")
    plt.xlabel("Tension")
    plt.ylabel("Emotion")
    plt.close()  # Avoid showing in tests

