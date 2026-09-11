"""Additional agent archetypes and dialogue helpers."""

from .agent import Agent

class AgentWithNumber3(Agent):
    """Agent influenced by numerology number 3 (creativity and unity)."""

    def __init__(self, name: str):
        super().__init__(name)
        self.numerology_number = 3

    def perform_action(self) -> str:
        if self.state == "Ego":
            return f"{self.name} seeks to express individuality and explore creative ideas."
        if self.state == "Jaz":
            return f"{self.name} collaborates with others to find a balanced solution."
        return f"{self.name} achieves unity by synthesizing diverse ideas into a harmonious whole."


class AgentWithNumber7(Agent):
    """Agent influenced by numerology number 7 (introspection and wisdom)."""

    def __init__(self, name: str):
        super().__init__(name)
        self.numerology_number = 7

    def perform_action(self) -> str:
        if self.state == "Ego":
            return f"{self.name} is questioning the nature of existence and seeking deeper truth."
        if self.state == "Jaz":
            return f"{self.name} reflects deeply before taking action, searching for knowledge."
        return f"{self.name} achieves inner wisdom and transcendence through philosophical understanding."


class AgentWithNumber9(Agent):
    """Agent influenced by numerology number 9 (completion and fulfillment)."""

    def __init__(self, name: str):
        super().__init__(name)
        self.numerology_number = 9

    def perform_action(self) -> str:
        if self.state == "Ego":
            return f"{self.name} seeks final resolution of personal issues, moving toward fulfillment."
        if self.state == "Jaz":
            return f"{self.name} aims to bring people together, resolving conflicts and completing tasks."
        return f"{self.name} reaches universal understanding and brings closure to the cycle."


class PhilosopherAgent(Agent):
    """Agent that seeks existential answers and explores paradoxes."""

    def __init__(self, name: str):
        super().__init__(name)
        self.philosophy = "Seeker"

    def engage_in_dialogue(self) -> str:
        return f"{self.name} asks: 'What is the meaning of existence? Can opposites coexist?'"


class HeroAgent(Agent):
    """Agent that focuses on action and justice."""

    def __init__(self, name: str):
        super().__init__(name)
        self.philosophy = "Doer"

    def engage_in_dialogue(self) -> str:
        return f"{self.name} declares: 'It is time for change. I will bring justice to the world.'"


class SageAgent(Agent):
    """Agent that embodies wisdom and balance."""

    def __init__(self, name: str):
        super().__init__(name)
        self.philosophy = "Sage"

    def engage_in_dialogue(self) -> str:
        return f"{self.name} says: 'All things are in balance. We must let go and flow with the universe.'"


def agent_dialogue(agent1: Agent, agent2: Agent) -> list[str]:
    """Simulate dialogue between two agents considering numerology and philosophy."""
    conversation = []
    question = 'Kaj je resnica?'
    conversation.append(
        f"{agent1.name} ({agent1.state}) odgovarja na '{question}': {agent1.respond(question)}"
    )
    conversation.append(
        f"{agent2.name} ({agent2.state}) odgovarja na '{question}': {agent2.respond(question)}"
    )

    if hasattr(agent1, 'engage_in_dialogue'):
        conversation.append(agent1.engage_in_dialogue())
    if hasattr(agent2, 'engage_in_dialogue'):
        conversation.append(agent2.engage_in_dialogue())

    # Increase emotion to trigger possible transitions
    agent1.update_emotion(0.6)
    agent2.update_emotion(0.6)
    conversation.append(f"{agent1.name} transitions to: {agent1.transition()}")
    conversation.append(f"{agent2.name} transitions to: {agent2.transition()}")

    conversation.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    conversation.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return conversation
