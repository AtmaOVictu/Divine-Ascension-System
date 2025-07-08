"""Creative and Destructive agents interacting with ontological states."""

from typing import List

from .agent import Agent


class CreativeAgent(Agent):
    """Agent focused on creation and positive karma."""

    def __init__(self, name: str, state: str = "Ego"):
        super().__init__(name, state)
        self.karma: int = 0
        self.actions: List[str] = []

    def create(self) -> None:
        """Perform a creative act, increasing karma and calm."""
        self.karma += 10
        # Creating calms the agent and may trigger a transition
        self.update_emotion(0.6)
        self.actions.append("create")

    def perform_action(self) -> str:
        self.create()
        return self.transition()


class DestructiveAgent(Agent):
    """Agent focused on destruction and negative karma."""

    def __init__(self, name: str, state: str = "Ego"):
        super().__init__(name, state)
        self.karma: int = 0
        self.actions: List[str] = []

    def destroy(self) -> None:
        """Perform a destructive act, decreasing karma and increasing anger."""
        self.karma -= 10
        # Destruction fuels tension and may trigger a transition
        self.update_emotion(0.8)
        self.actions.append("destroy")

    def perform_action(self) -> str:
        self.destroy()
        return self.transition()


def interact(creator: CreativeAgent, destroyer: DestructiveAgent) -> List[str]:
    """Simulate one interaction step between a creative and a destructive agent."""
    lines: List[str] = []
    lines.append(f"{creator.name} ({creator.state}): {creator.respond('Kaj je resnica?')}")
    lines.append(f"{destroyer.name} ({destroyer.state}): {destroyer.respond('Kaj je resnica?')}")

    creator.perform_action()
    destroyer.perform_action()

    lines.append(f"{creator.name} karma: {creator.karma} state: {creator.state}")
    lines.append(f"{destroyer.name} karma: {destroyer.karma} state: {destroyer.state}")

    lines.append(f"{creator.name}: {creator.respond('Kaj je resnica?')}")
    lines.append(f"{destroyer.name}: {destroyer.respond('Kaj je resnica?')}")
    return lines
