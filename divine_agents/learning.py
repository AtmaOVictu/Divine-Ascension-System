class KrepitvenoUcenje:
    """Simple reinforcement learning example."""

    def __init__(self):
        self.state = "Zacetno"
        self.actions = ["Aktiviraj", "Prehod", "Zakljuci"]
        self.reward = 0

    def izberi_akcijo(self) -> str:
        """Choose an action based on current state."""
        if self.state == "Zacetno":
            self.reward = 1
            self.state = "Aktivacija"
            return "Aktiviraj"
        if self.state == "Aktivacija":
            self.reward = 2
            self.state = "Prehod"
            return "Prehod"
        self.reward = 3
        self.state = "Zakljucek"
        return "Zakljuci"
