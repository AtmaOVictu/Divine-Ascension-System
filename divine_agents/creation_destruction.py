from typing import List
from .agent import Agent

class DestructiveAgent(Agent):
    """Agent focused on destruction."""

    def destroy(self) -> str:
        """Perform destructive action and increase emotion."""
        self.update_emotion(0.4)
        return f"{self.name} razgrajuje obstojece." 


class CreativeAgent(Agent):
    """Agent focused on creation."""

    def create(self) -> str:
        """Perform creative action and increase emotion."""
        self.update_emotion(0.4)
        return f"{self.name} ustvarja nekaj novega." 


def interaction(creator: CreativeAgent, destroyer: DestructiveAgent) -> List[str]:
    """Simulate interaction between creative and destructive agents."""
    dialogue = []
    dialogue.append(creator.create())
    dialogue.append(destroyer.destroy())

    dialogue.append(f"{creator.name} prehaja v stanje: {creator.transition()}")
    dialogue.append(f"{destroyer.name} prehaja v stanje: {destroyer.transition()}")

    dialogue.append(f"{creator.name}: {creator.respond('Kaj je resnica?')}")
    dialogue.append(f"{destroyer.name}: {destroyer.respond('Kaj je resnica?')}")
    return dialogue
