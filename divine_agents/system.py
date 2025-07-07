from typing import List
from .wide_agent import WideAgent
from .narrow_agent import NarrowAgent


class ComplexSystem:
    """System combining a wide and a narrow agent for interaction."""

    def __init__(self):
        self.wide_agent = WideAgent("WideAgent")
        self.narrow_agent = NarrowAgent("NarrowAgent")

    def process(self) -> List[str]:
        lines: List[str] = []
        lines.append(
            f"{self.wide_agent.name} ({self.wide_agent.state}): "
            f"{self.wide_agent.respond('Kaj je resnica?')}"
        )
        lines.append(
            f"{self.narrow_agent.name} ({self.narrow_agent.state}): "
            f"{self.narrow_agent.respond('Kaj je resnica?')}"
        )

        self.wide_agent.update_emotion(0.8)
        lines.append(f"{self.wide_agent.name} prehaja v stanje: {self.wide_agent.transition()}")

        # escalate again to reach Enotnost
        self.wide_agent.update_emotion(0.9)
        lines.append(f"{self.wide_agent.name} prehaja v stanje: {self.wide_agent.transition()}")

        self.narrow_agent.update_value(0.9)
        lines.append(
            f"{self.narrow_agent.name} prehaja v stanje: {self.narrow_agent.state}"
        )

        lines.append(f"{self.wide_agent.name}: {self.wide_agent.respond('Kaj je resnica?')}")
        lines.append(f"{self.narrow_agent.name}: {self.narrow_agent.respond('Kaj je resnica?')}")
        return lines
