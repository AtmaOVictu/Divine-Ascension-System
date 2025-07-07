from typing import Dict, List, Optional

class Box:
    """A container that stores data and tracks its history."""
    def __init__(self, name: str, data: Optional[Dict] = None):
        self.name = name
        self.data: Dict = data or {}
        self.history: List[Dict] = []

    def update(self, new_data: Dict) -> None:
        """Update the box, preserving previous state in history."""
        self.history.append(self.data.copy())
        self.data.update(new_data)

    def unpack(self) -> Dict:
        """Return the current data without modification."""
        return self.data
