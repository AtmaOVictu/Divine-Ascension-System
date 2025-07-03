class Ontoznano:
    """Track ontological transitions for an agent."""

    def __init__(self) -> None:
        self.podrocje = "neznano"
        self.napredek = 0
        self.historia = []

    def prehod_v_ontoznano(self, prehod: str) -> str:
        """Update internal state based on the given transition."""
        mapping = {
            "samospoznanje": ("poznavanje lastne resnice", 100),
            "logični prehod": ("logična analiza", 50),
            "emotivni prehod": ("emocionalna refleksija", 75),
        }
        self.podrocje, self.napredek = mapping.get(prehod, ("neznano", 0))
        self.historia.append((prehod, self.napredek))
        return self.podrocje
