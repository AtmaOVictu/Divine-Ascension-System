class AutomatskiPrehodi:
    """Automated state transitions based on agent's internal state."""
    def __init__(self, agent):
        self.agent = agent

    def preveri_pogoje_za_prehod(self):
        if self.agent.tension > 0.7 or self.agent.emotion > 0.5:
            if self.agent.state == "Ego":
                self.agent.state = "Jaz"
            elif self.agent.state == "Jaz":
                self.agent.state = "Enotnost"
        return self.agent.state


class SamodejnaOptimizacija:
    """Automatically adjust agent state after errors."""
    def __init__(self, agent):
        self.agent = agent

    def optimiziraj_kodo(self):
        if any("error" in h for h in self.agent.history):
            self.agent.tension = max(self.agent.tension - 0.1, 0)
        return self.agent
