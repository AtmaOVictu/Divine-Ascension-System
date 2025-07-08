from __future__ import annotations

from .agent import Agent


class ArchetypeAgent(Agent):
    """An agent representing a higher, symbolic archetype."""

    def __init__(self, name: str, archetype_type: str, **kwargs):
        super().__init__(name, **kwargs)
        self.archetype_type = archetype_type
        self.power = 100

    def redefine_name(self, new_name: str) -> None:
        """Change the archetype's display name."""
        self.name = new_name

    def influence_environment(self) -> str:
        """Return a message describing its influence."""
        if self.archetype_type == "Absolute Truth":
            return f"{self.name} razkriva temelj vse realnosti."
        if self.archetype_type == "Ego":
            return f"{self.name} uveljavlja svojo individualnost."
        if self.archetype_type == "Creation":
            return f"{self.name} prina\u0161a nove ideje v obstoj."
        return f"{self.name} oblikuje svet na skrivnosten na\u010din."

    def evolve(self, new_archetype: str) -> None:
        """Evolve into a new archetype and increase power."""
        self.archetype_type = new_archetype
        self.state = self.transition()
        self.power += 50
