from typing import List, Dict
from .agent import Agent


class AgentFrekvenca:
    """Detect frequency resonance and log results."""

    def __init__(self) -> None:
        self.records: List[Dict[str, float | str]] = []

    def detect(self, state: str, frequency: float) -> str:
        if frequency < 0.5:
            status = "Nizka frekvenca – proces v nastajanju, še ne prepoznan"
        elif 0.5 <= frequency <= 1.5:
            status = "Srednja frekvenca – napetost rasti, proces z začetkom"
        else:
            status = "Visoka frekvenca – maksimalna napetost, prehod v nov ciklus"
        self.records.append({"stanje": state, "frekvenca": frequency, "status": status})
        return status

    def history(self) -> List[Dict[str, float | str]]:
        return self.records


class AgentZvok:
    """Observe when frequency turns into resonance (sound) and influence agent state."""

    def __init__(self) -> None:
        self.records: List[Dict[str, float | str]] = []

    def receive_frequency(self, agent: Agent, frequency: float) -> str:
        """Receive frequency and update agent state if resonance occurs."""
        status = "Brez zvena"
        if frequency > 1.5:
            status = "Zven – frekvenca je prešla v resonanco"
            agent.update_tension(frequency)
            agent.transition()
        self.records.append({"agent": agent.name, "frekvenca": frequency, "status": status, "state": agent.state})
        return status

    def history(self) -> List[Dict[str, float | str]]:
        return self.records
