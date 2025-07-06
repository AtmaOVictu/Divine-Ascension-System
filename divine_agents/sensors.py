"""Utility classes for frequency and sound detection."""
from typing import List, Dict

from .agent import Agent


class AgentFrekvenca:
    """Detect frequency tension and track its state."""

    def __init__(self) -> None:
        self.records: List[Dict[str, float | str]] = []

    def detect(self, state: str, frequency: float) -> str:
        """Return a textual status for the given frequency."""
        if frequency < 0.5:
            status = "Nizka frekvenca – proces v nastajanju, še ne prepoznan"
        elif 0.5 <= frequency <= 1.5:
            status = "Srednja frekvenca – napetost rasti, proces z začetkom"
        else:
            status = "Visoka frekvenca – maksimalna napetost, prehod v nov ciklus"
        self.records.append({"Stanje": state, "Frekvenca": frequency, "Status": status})
        return status

    def history(self) -> List[Dict[str, float | str]]:
        """Return the detection history."""
        return self.records


class AgentZvok:
    """React to frequency detection and influence an ontological agent."""

    def __init__(self, detector: AgentFrekvenca) -> None:
        self.detector = detector

    def resonate(self, agent: Agent, frequency: float) -> str:
        """Detect frequency, update agent tension, and perform transition."""
        status = self.detector.detect(agent.state, frequency)
        agent.update_tension(frequency)
        agent.transition()
        return status
