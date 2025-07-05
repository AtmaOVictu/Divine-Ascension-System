# -*- coding: utf-8 -*-
"""Codex agents with philosophical and emotional dynamics."""
from typing import List, Dict


class CodexAgent:
    """Agent with extended emotional and philosophical attributes."""

    STATES = ("Ego", "Jaz", "Enotnost", "Transcendenca")

    def __init__(self, name: str, state: str = "Ego") -> None:
        if state not in self.STATES:
            raise ValueError(f"Invalid state: {state}")
        self.name = name
        self.state = state
        self.tension = 0.0
        self.emotion = 0.0
        self.love = 0.0
        self.hate = 0.0
        self.history: List[str] = [state]
        self.philosophical_context: Dict[str, str] = {}

    def update_emotion(self) -> None:
        """Update overall emotion based on love and hate."""
        self.emotion = self.love - self.hate
        self.history.append(f"Emotion updated: {self.emotion}")

    def update_love(self, value: float) -> None:
        """Set love and recalculate emotion."""
        self.love = value
        self.update_emotion()

    def update_hate(self, value: float) -> None:
        """Set hate and recalculate emotion."""
        self.hate = value
        self.update_emotion()

    def transition(self) -> str:
        """Move to the next ontological state if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
            elif self.state == "Enotnost":
                self.state = "Transcendenca"
        self.history.append(f"Transitioned to: {self.state}")
        return self.state

    def philosophical_analysis(self) -> None:
        """Store a philosophical note based on love and hate balance."""
        if self.love > self.hate:
            self.philosophical_context[self.name] = (
                "Agent is following a path of love and unity." )
        elif self.hate > self.love:
            self.philosophical_context[self.name] = (
                "Agent is experiencing conflict and division." )
        else:
            self.philosophical_context[self.name] = (
                "Agent is in a state of equilibrium." )

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        if self.state == "Enotnost":
            return "Vse resnice so eno, medsebojno povezane."
        return "Resnica presega individualno izkušnjo in je transcendentna."

    def print_history(self) -> None:
        """Print transition history for debugging purposes."""
        print(f"History of {self.name}:")
        for event in self.history:
            print(event)


class CodexSimulation:
    """Run a simple simulation for multiple agents."""

    def __init__(self, agents: List[CodexAgent]):
        self.agents = agents

    def run_simulation(self) -> None:
        for agent in self.agents:
            agent.transition()
            agent.philosophical_analysis()
            agent.print_history()

    def print_agents_philosophical_context(self) -> None:
        for agent in self.agents:
            context = agent.philosophical_context.get(agent.name, "No analysis")
            print(f"{agent.name}'s philosophical context: {context}")


class CriticalReflectionAgent(CodexAgent):
    """Agent capable of reflecting on past states."""

    def reflect_on_actions(self) -> None:
        if "Ego" in self.history:
            self.history.append(
                f"{self.name} is reflecting on Ego state: How does this affect my perception of reality?" )
        if "Jaz" in self.history:
            self.history.append(
                f"{self.name} is reflecting on Jaz state: Am I progressing towards unity?" )
        if "Enotnost" in self.history:
            self.history.append(
                f"{self.name} is reflecting on Enotnost state: Have I reached a state of transcendence?" )
        self.history.append(f"Critical reflection completed for {self.name}.")


class LoveHatePhilosophicalAgent(CriticalReflectionAgent):
    """Agent that evaluates the impact of emotions on its philosophy."""

    def evaluate_emotional_impact(self) -> None:
        if self.love > self.hate:
            self.history.append(
                f"{self.name} is motivated by love, seeking harmony and unity." )
        elif self.hate > self.love:
            self.history.append(
                f"{self.name} is motivated by hate, creating conflict and division." )
        else:
            self.history.append(
                f"{self.name} is in a state of emotional equilibrium, seeking balance." )
