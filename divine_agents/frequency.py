class AgentFrekvenca:
    """Detects resonance frequency states and logs their status."""

    def __init__(self) -> None:
        self.records = []

    def detect(self, state: str, frequency: float) -> str:
        """Classify frequency resonance and store the result."""
        if frequency < 0.5:
            status = "Nizka frekvenca – proces v nastajanju, še ne prepoznan"
        elif 0.5 <= frequency <= 1.5:
            status = "Srednja frekvenca – napetost rasti, proces z začetkom"
        else:
            status = "Visoka frekvenca – maksimalna napetost, prehod v nov ciklus"
        self.records.append({"state": state, "frequency": frequency, "status": status})
        return status

    def history(self):
        return self.records
