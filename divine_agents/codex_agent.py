"""Advanced agent models for Codex philosophical simulations."""

from __future__ import annotations

from typing import List, Dict


class CodexAgent:
    """Agent capable of complex emotional and philosophical transitions."""

    STATES = ("Ego", "Jaz", "Enotnost", "Transcendenca")

    def __init__(self, name: str, state: str = "Ego") -> None:
        self.name = name
        self.state = state
        self.tension = 0.0
        self.emotion = 0.0
        self.love = 0.0
        self.hate = 0.0
        self.history: List[str] = [f"Initialized in {state}"]
        self.philosophical_context: Dict[str, str] = {}

    def update_emotion(self) -> None:
        """Update combined emotion based on love and hate."""
        self.emotion = self.love - self.hate
        self.history.append(f"Emotion updated: {self.emotion}")

    def update_love(self, value: float) -> None:
        """Set love and update emotion."""
        self.love = value
        self.update_emotion()

    def update_hate(self, value: float) -> None:
        """Set hate and update emotion."""
        self.hate = value
        self.update_emotion()

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Transition through ontological states if thresholds are exceeded."""
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
        """Analyze the agent's philosophical alignment."""
        if self.love > self.hate:
            msg = "Agent is following a path of love and unity."
        elif self.hate > self.love:
            msg = "Agent is experiencing conflict and division."
        else:
            msg = "Agent is in a state of equilibrium."
        self.philosophical_context[self.name] = msg

    def print_history(self) -> None:
        """Print the agent's history to stdout."""
        print(f"History of {self.name}:")
        for event in self.history:
            print(event)


class CodexSimulation:
    """Run simulations across multiple agents."""

    def __init__(self, agents: List[CodexAgent]):
        self.agents = agents

    def run_simulation(self) -> List[str]:
        """Execute transitions and philosophical analyses for all agents."""
        lines: List[str] = []
        for agent in self.agents:
            lines.append(f"Running simulation for agent: {agent.name}")
            agent.transition()
            agent.philosophical_analysis()
            lines.extend(agent.history)
            lines.append(
                f"{agent.name}'s philosophical context: {agent.philosophical_context.get(agent.name)}"
            )
        return lines

    def print_agents_philosophical_context(self) -> None:
        """Print philosophical contexts for all agents."""
        for agent in self.agents:
            context = agent.philosophical_context.get(agent.name, "No analysis")
            print(f"{agent.name}'s philosophical context: {context}")


class CriticalReflectionAgent(CodexAgent):
    """Agent capable of reflecting on its past actions."""

    def reflect_on_actions(self) -> None:
        """Record reflective thoughts based on past transitions."""
        if any("Ego" in h for h in self.history):
            self.history.append(
                f"{self.name} is reflecting on Ego state: How does this affect my perception of reality?"
            )
        if any("Jaz" in h for h in self.history):
            self.history.append(
                f"{self.name} is reflecting on Jaz state: Am I progressing towards unity?"
            )
        if any("Enotnost" in h for h in self.history):
            self.history.append(
                f"{self.name} is reflecting on Enotnost state: Have I reached a state of transcendence?"
            )
        self.history.append(f"Critical reflection completed for {self.name}.")


class LoveHatePhilosophicalAgent(CriticalReflectionAgent):
    """Agent that evaluates love and hate within philosophical contexts."""

    def evaluate_emotional_impact(self) -> None:
        """Add contextual information on emotional impact."""
        if self.love > self.hate:
            self.history.append(
                f"{self.name} is motivated by love, seeking harmony and unity."
            )
        elif self.hate > self.love:
            self.history.append(
                f"{self.name} is motivated by hate, creating conflict and division."
            )
        else:
            self.history.append(
                f"{self.name} is in a state of emotional equilibrium, seeking balance."
            )
