from __future__ import annotations

"""Specialized agents representing creative and destructive behaviors."""

from .agent import Agent


class CreativeAgent(Agent):
    """Agent focused on creation and constructive actions."""

    def __init__(self, name: str, state: str = "Ego") -> None:
        super().__init__(name, state)
        self.karma = 0

    def create(self) -> None:
        """Perform a creative act influencing emotion and karma."""
        self.karma += 10
        # Strong creative impulse raises emotion enough to trigger transitions
        self.update_emotion(0.8)


class DestructiveAgent(Agent):
    """Agent focused on destruction and chaotic actions."""

    def __init__(self, name: str, state: str = "Ego") -> None:
        super().__init__(name, state)
        self.karma = 0

    def destroy(self) -> None:
        """Perform a destructive act influencing emotion and karma."""
        self.karma -= 10
        # Destructive rage increases emotion beyond the threshold
        self.update_emotion(0.8)


def creative_destructive_interaction(creator: CreativeAgent, destroyer: DestructiveAgent):
    """Simulate interaction between creative and destructive agents."""
    lines = []
    lines.append(f"{creator.name} ({creator.state}): {creator.respond('Kaj je resnica?')}")
    lines.append(f"{destroyer.name} ({destroyer.state}): {destroyer.respond('Kaj je resnica?')}")

    creator.create()
    lines.append(f"{creator.name} prehaja v stanje: {creator.transition()}")

    destroyer.destroy()
    lines.append(f"{destroyer.name} prehaja v stanje: {destroyer.transition()}")

    lines.append(f"{creator.name}: {creator.respond('Kaj je resnica?')}")
    lines.append(f"{destroyer.name}: {destroyer.respond('Kaj je resnica?')}")
    return lines
