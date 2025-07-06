"""Basic modules representing awareness, opposition and transition logic."""

class AwarenessModule:
    """Manage awareness state."""

    def __init__(self, name: str, state: str = "inactive") -> None:
        self.name = name
        self.state = state

    def activate(self) -> None:
        if self.state == "inactive":
            self.state = "active"

    def deactivate(self) -> None:
        if self.state == "active":
            self.state = "inactive"


class OppositionModule:
    """Handle opposition forces within the system."""

    def __init__(self, name: str, state: str = "inactive") -> None:
        self.name = name
        self.state = state

    def toggle_opposition(self) -> None:
        if self.state == "inactive":
            self.state = "active"
        else:
            self.state = "inactive"


class TransitionModule:
    """Process transitions between modules."""

    def __init__(self, awareness: AwarenessModule, opposition: OppositionModule) -> None:
        self.awareness = awareness
        self.opposition = opposition

    def process(self) -> None:
        self.awareness.activate()
        self.opposition.toggle_opposition()
