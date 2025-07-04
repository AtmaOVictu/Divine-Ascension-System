from __future__ import annotations

"""Additional contextual agents for philosophical simulations."""

from typing import List

from .agent import Agent


class PhilosophicalResearchAgent(Agent):
    """Agent focused on progressing through research stages."""

    def __init__(self, name: str, state: str = "Ego") -> None:
        super().__init__(name, state)
        self.research_stage = 0
        self.research_phases = [
            "Iskanje definicije resnice",
            "Iskanje pomena obstoja",
            "Preizkus ontolo\u0161kih protislovij",
            "Refleksija o moralnih vpra\u0161anjih",
            "Razumevanje praznine in ničesar",
        ]

    def transition(self) -> str:
        if self.research_stage < len(self.research_phases):
            self.research_stage += 1
        return super().transition()


class EmotionalDynamicAgent(Agent):
    """Agent managing emotional state transitions."""

    def __init__(self, name: str, state: str = "Ego", emotional_state: str = "Neutral") -> None:
        super().__init__(name, state)
        self.emotional_state = emotional_state
        self.emotions = ["Neutral", "Anger", "Sadness", "Joy", "Fear"]

    def next_emotion(self) -> str:
        index = self.emotions.index(self.emotional_state)
        return self.emotions[(index + 1) % len(self.emotions)]

    def transition(self) -> str:
        self.emotional_state = self.next_emotion()
        return super().transition()


class MoralDilemmaAgent(Agent):
    """Agent facing sequential moral dilemmas."""

    def __init__(self, name: str, state: str = "Ego", dilemma: str = "Truth vs. Lie") -> None:
        super().__init__(name, state)
        self.dilemma = dilemma
        self.dilemmas = [
            "Truth vs. Lie",
            "Selfishness vs. Altruism",
            "Justice vs. Mercy",
            "Freedom vs. Control",
        ]

    def transition(self) -> str:
        if self.dilemma in self.dilemmas:
            current_index = self.dilemmas.index(self.dilemma)
            if current_index + 1 < len(self.dilemmas):
                self.dilemma = self.dilemmas[current_index + 1]
        return super().transition()


class MultiContextualAgentSystem:
    """Coordinate transitions for multiple agents."""

    def __init__(self, agents: List[Agent]):
        self.agents = agents

    def transition_all(self) -> List[str]:
        lines = []
        for agent in self.agents:
            before = agent.state
            agent.transition()
            lines.append(f"{agent.name}: {before} -> {agent.state}")
        return lines
