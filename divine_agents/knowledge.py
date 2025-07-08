import random
from typing import Optional

class KnowledgeBase:
    """Track processed knowledge to avoid repetition."""

    def __init__(self) -> None:
        self.processed = set()

    def add(self, item: str) -> bool:
        """Add knowledge if not already processed.

        Returns True if the item was new.
        """
        if item not in self.processed:
            self.processed.add(item)
            return True
        return False

    def random_item(self) -> Optional[str]:
        """Return a random item from processed knowledge or None."""
        if not self.processed:
            return None
        return random.choice(list(self.processed))

    def random_explore(self) -> Optional[str]:
        """Alias for random_item for semantic clarity."""
        return self.random_item()
