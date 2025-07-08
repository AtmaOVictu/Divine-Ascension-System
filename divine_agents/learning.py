"""Utility functions for continuous learning loops."""
from typing import Tuple
import math
import random

from .agent import Agent


def emotional_feedback(agent1: Agent, agent2: Agent) -> Tuple[Agent, Agent]:
    """Adjust agent emotions based on each other's state."""
    if agent1.emotion > 0.5 and agent1.state == "Ego":
        agent2.update_emotion(0.2)  # calm response
    if agent2.emotion > 0.5 and agent2.state == "Jaz":
        agent1.update_emotion(-0.2)
    return agent1, agent2


def tension_decay(tension: float, decay_rate: float, time_step: float) -> float:
    """Exponential decay of tension over time."""
    return float(tension * math.exp(-decay_rate * time_step))


def continuous_learning_cycle(agent1: Agent, agent2: Agent, tension: float, time_step: float) -> Tuple[Agent, Agent, float]:
    """One iteration of feedback and state update."""
    agent1, agent2 = emotional_feedback(agent1, agent2)
    tension = tension_decay(tension, 0.3, time_step)
    agent1.update_tension(tension)
    agent2.update_tension(tension)
    agent1.transition()
    agent2.transition()
    return agent1, agent2, tension


class EmotionalAgent(Agent):
    """Agent using simple reinforcement learning for emotion adjustment."""

    def adjust_emotion(self, trigger: str) -> None:
        if trigger == "positive":
            self.update_emotion(max(0.0, self.emotion - 0.1))
        elif trigger == "negative":
            self.update_emotion(min(1.0, self.emotion + 0.1))

    def reinforcement(self) -> float:
        if self.emotion < 0.3:
            reward = 1
        elif self.emotion > 0.7:
            reward = -1
        else:
            reward = 0
        self.update_tension(self.tension + reward * 0.05)
        return self.tension


def learning_cycle(agent1: EmotionalAgent, agent2: EmotionalAgent, iterations: int = 10) -> None:
    triggers = ["positive", "negative"]
    for _ in range(iterations):
        agent1.adjust_emotion(random.choice(triggers))
        agent2.adjust_emotion(random.choice(triggers))
        agent1.reinforcement()
        agent2.reinforcement()
        agent1.transition()
        agent2.transition()

