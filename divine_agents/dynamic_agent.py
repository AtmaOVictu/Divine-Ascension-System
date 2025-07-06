class DynamicAgent:
    """Agent capable of dynamic state transitions and reorganization."""

    def __init__(self, ime, stanje="neutral", tension=0.0, emotion=0.0, aktivnosti=0):
        self.ime = ime
        self.stanje = stanje
        self.tension = tension
        self.emotion = emotion
        self.aktivnosti = aktivnosti
        self.povezave = []

    def prehod(self):
        """Transition between states based on tension and emotion."""
        if self.tension > 0.7:
            self.stanje = "Jaz"
        elif self.emotion > 0.5:
            self.stanje = "Enotnost"
        else:
            self.stanje = "Ego"
        return self.stanje

    def komunikacija(self, drugi_agent):
        """Communicate and propagate activation state."""
        if self.stanje == "aktiviran":
            drugi_agent.stanje = "aktiviran"
            return f"{self.ime} je komuniciral z {drugi_agent.ime}. Stanje: {drugi_agent.stanje}"
        return f"{self.ime} ni komuniciral, ker ni v aktiviranem stanju."

    def reorganiziraj(self, drugi_agent):
        """Reorganize when activity is high."""
        if self.aktivnosti > 5:
            self.stanje = "prehod"
            drugi_agent.povezave.append(self)
            return f"{self.ime} se je reorganiziral z {drugi_agent.ime}"
        return f"{self.ime} se ni reorganiziral."
