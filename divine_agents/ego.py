class Ego:
    """Simple ego component reacting to urgent tasks."""

    def reakcionira_na_nujnost(self, naloga: str) -> str:
        """Return a short reaction string."""
        return f"Ego reagira na nujnost: {naloga}"
