"""Additional discourse simulations for philosophical debates."""

from typing import List
from .agent import Agent


class TruthDiscourse:
    """Simulate a simple dialogue about the nature of truth."""

    def __init__(self, agent1: Agent, agent2: Agent):
        self.agent1 = agent1
        self.agent2 = agent2
        self.intensity = 0.0

    def discuss(self) -> List[str]:
        lines = []
        lines.append(
            f"{self.agent1.name}: Resnica je večna in neodvisna od človeške percepcije."
        )
        self.intensity += 0.2
        lines.append(
            f"{self.agent2.name}: Ampak, resnica je subjektivna. To, kar je resnično za enega, ni nujno resnično za drugega."
        )
        self.intensity -= 0.3
        if self.intensity > 0:
            lines.append(
                "Napetost raste: argumenti postajajo bolj izraziti."
            )
        elif self.intensity < 0:
            lines.append(
                "Napetost se zmanjšuje: izmenjava mnenj je postala manj agresivna."
            )
        else:
            lines.append(
                "Napetost se je stabilizirala: oba agenta prepoznata vrednost nasprotja."
            )
        return lines
