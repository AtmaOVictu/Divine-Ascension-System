class Ego:
    """Simple ego representation handling urgent events."""

    def __init__(self):
        self.state = "stable"

    def react(self, urgency: str) -> str:
        """React to a given urgency and adjust internal state."""
        if urgency == "kriticna napaka":
            self.state = "reakcija na napako"
        elif urgency == "nova naloga":
            self.state = "sprejemanje naloge"
        elif urgency == "sprememba stanja":
            self.state = "adaptacija na spremembo"
        else:
            self.state = "stable"
        return self.state
