from .agent import Agent


class ArchetypeAgent(Agent):
    """Ontological agent representing a symbolic archetype."""

    def __init__(self, name: str, archetype_type: str,
                 state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        super().__init__(name, state, tension, emotion)
        self.archetype_type = archetype_type
        self.power = 100

    def redefine_name(self, new_name: str) -> None:
        """Change the archetype's name."""
        self.name = new_name

    def influence_environment(self) -> str:
        """Return a string describing the archetype's influence."""
        if self.archetype_type == "Absolute Truth":
            return f"{self.name} razkriva temelj resničnosti."
        if self.archetype_type == "Ego":
            return f"{self.name} poudarja svoj obstoj in individualnost."
        if self.archetype_type == "Creation":
            return f"{self.name} prinaša nove ideje v obstoj."
        return f"{self.name} oblikuje svet na skrivnostne načine."

    def evolve(self, new_archetype: str) -> str:
        """Transform into a new archetype and increase power."""
        self.archetype_type = new_archetype
        self.power += 50
        return self.archetype_type
