from typing import Dict, Tuple, Optional

class SpaceModule:
    """Manage agent positions in a 2D plane."""

    def __init__(self) -> None:
        self.space: Dict[str, Tuple[int, int]] = {}

    def add_agent(self, name: str, position: Tuple[int, int]) -> None:
        self.space[name] = position

    def move_agent(self, name: str, position: Tuple[int, int]) -> None:
        if name in self.space:
            self.space[name] = position

    def distance(self, name1: str, name2: str) -> Optional[float]:
        p1, p2 = self.space.get(name1), self.space.get(name2)
        if p1 and p2:
            return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5
        return None
