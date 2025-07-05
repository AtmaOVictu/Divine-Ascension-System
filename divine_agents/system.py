class ModularUnit:
    """Building block that can connect to other units."""

    def __init__(self, name: str, connected_units: list | None = None):
        self.name = name
        self.connected_units = connected_units or []

    def connect_unit(self, unit: "ModularUnit") -> None:
        if unit not in self.connected_units:
            self.connected_units.append(unit)

    def activate(self) -> list[str]:
        activations = [self.name]
        for unit in self.connected_units:
            activations.extend(unit.activate())
        return activations


class AgentSystem:
    """System managing agents and modular units."""

    def __init__(self):
        self.agents: list = []
        self.units: list = []

    def add_agent(self, agent) -> None:
        self.agents.append(agent)

    def add_unit(self, unit: ModularUnit) -> None:
        self.units.append(unit)

    def simulate(self) -> dict:
        transitions = [agent.transition() for agent in self.agents]
        unit_activations: list[str] = []
        for unit in self.units:
            unit_activations.extend(unit.activate())
        return {"transitions": transitions, "activations": unit_activations}
