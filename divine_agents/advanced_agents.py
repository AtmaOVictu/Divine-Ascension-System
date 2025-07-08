from .agent import Agent


class AgentWithNumber3(Agent):
    """Agent influenced by the numerology number 3."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0) -> None:
        super().__init__(name, state=state, tension=tension, emotion=emotion)
        self.numerology_number = 3

    def perform_action(self) -> str:
        if self.state == "Ego":
            return f"{self.name} seeks to express individuality and explore creative ideas."
        if self.state == "Jaz":
            return f"{self.name} collaborates with others to find a balanced solution."
        return f"{self.name} achieves unity by synthesizing diverse ideas into a harmonious whole."


class AgentWithNumber7(Agent):
    """Agent influenced by the numerology number 7."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0) -> None:
        super().__init__(name, state=state, tension=tension, emotion=emotion)
        self.numerology_number = 7

    def perform_action(self) -> str:
        if self.state == "Ego":
            return f"{self.name} is questioning the nature of existence and seeking deeper truth."
        if self.state == "Jaz":
            return f"{self.name} reflects deeply before taking action, searching for knowledge."
        return f"{self.name} achieves inner wisdom and transcendence through philosophical understanding."


class AgentWithNumber9(Agent):
    """Agent influenced by the numerology number 9."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0) -> None:
        super().__init__(name, state=state, tension=tension, emotion=emotion)
        self.numerology_number = 9

    def perform_action(self) -> str:
        if self.state == "Ego":
            return f"{self.name} seeks final resolution of personal issues, moving toward fulfillment."
        if self.state == "Jaz":
            return f"{self.name} aims to bring people together, resolving conflicts and completing tasks."
        return f"{self.name} reaches universal understanding and brings closure to the cycle."


class PhilosopherAgent(Agent):
    """Agent embodying the philosopher figure."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0) -> None:
        super().__init__(name, state=state, tension=tension, emotion=emotion)
        self.philosophy = "Seeker"

    def engage_in_dialogue(self) -> str:
        return f"{self.name} asks: 'What is the meaning of existence? Can opposites coexist?'"


class HeroAgent(Agent):
    """Agent embodying the hero figure."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0) -> None:
        super().__init__(name, state=state, tension=tension, emotion=emotion)
        self.philosophy = "Doer"

    def engage_in_dialogue(self) -> str:
        return f"{self.name} declares: 'It is time for change. I will bring justice to the world.'"


class SageAgent(Agent):
    """Agent embodying the sage figure."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0) -> None:
        super().__init__(name, state=state, tension=tension, emotion=emotion)
        self.philosophy = "Sage"

    def engage_in_dialogue(self) -> str:
        return f"{self.name} says: 'All things are in balance. We must let go and flow with the universe.'"


def agent_dialogue(agent1: Agent, agent2: Agent) -> list[str]:
    """Simulate dialogue influenced by philosophical figures and numerology."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(agent1.engage_in_dialogue())
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    lines.append(agent2.engage_in_dialogue())

    if getattr(agent1, 'numerology_number', None) == 3:
        lines.append(f"{agent1.name} seeks balance and unity in this conversation.")
    if getattr(agent2, 'numerology_number', None) == 7:
        lines.append(f"{agent2.name} reflects on the deeper meanings of the words spoken.")

    return lines
