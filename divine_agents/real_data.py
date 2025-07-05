class RealDataConnector:
    """Placeholder for reading real sensor data."""

    def __init__(self, stress: float = 0.0, mood: float = 0.0):
        self.stress = stress
        self.mood = mood

    def read(self):
        return {"stress": self.stress, "mood": self.mood}
