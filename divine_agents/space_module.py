from typing import Tuple, Dict

class SpaceModule:
    """Represent a simple two-dimensional space for agents."""

    def __init__(self) -> None:
        self.space: Dict[str, Tuple[float, float]] = {}

    def add_agent_to_space(self, agent_name: str, position: Tuple[float, float]) -> None:
        self.space[agent_name] = position

    def move_agent(self, agent_name: str, new_position: Tuple[float, float]) -> None:
        if agent_name in self.space:
            self.space[agent_name] = new_position

    def check_proximity(self, agent1: str, agent2: str) -> float | None:
        pos1 = self.space.get(agent1)
        pos2 = self.space.get(agent2)
        if pos1 and pos2:
            return ((pos2[0] - pos1[0]) ** 2 + (pos2[1] - pos1[1]) ** 2) ** 0.5
        return None
