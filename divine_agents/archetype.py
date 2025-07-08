from dataclasses import dataclass
from .agent import Agent


@dataclass(init=False)
class ArchetypeAgent(Agent):
    """Divine agent representing a symbolic archetype."""

    archetype_type: str = "Ego"
    power: int = 100

    def __init__(self, name: str, archetype_type: str = "Ego", **kwargs):
        super().__init__(name, **kwargs)
        self.archetype_type = archetype_type
        self.power = 100

    def redefine_name(self, new_name: str) -> None:
        self.name = new_name

    def influence_environment(self) -> str:
        if self.archetype_type == "Absolute Truth":
            return f"{self.name} razkriva temelj resnice."
        if self.archetype_type == "Ego":
            return f"{self.name} poudarja svojo individualnost."
        if self.archetype_type == "Creation":
            return f"{self.name} ustvarja nove ideje."
        return f"{self.name} oblikuje svet."

    def evolve(self, new_archetype: str) -> None:
        self.archetype_type = new_archetype
        self.state = new_archetype if new_archetype in self.STATES else self.state
        self.power += 50
