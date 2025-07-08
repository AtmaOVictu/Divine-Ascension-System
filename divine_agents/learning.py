import random
from typing import Optional, Set

class KnowledgeBase:
    """Track processed knowledge to avoid unnecessary repetition."""

    def __init__(self) -> None:
        self.processed_knowledge: Set[str] = set()

    def add_knowledge(self, knowledge: str) -> bool:
        """Add knowledge if new. Return True if it was added."""
        if knowledge not in self.processed_knowledge:
            self.processed_knowledge.add(knowledge)
            return True
        return False

    def is_new(self, knowledge: str) -> bool:
        """Check whether the knowledge is new."""
        return knowledge not in self.processed_knowledge

    def get_random(self) -> Optional[str]:
        """Get a random piece of knowledge for exploration."""
        if not self.processed_knowledge:
            return None
        return random.choice(list(self.processed_knowledge))


class AutoLearningSystem:
    """System that processes inputs and explores unresolved knowledge."""

    def __init__(self, knowledge_base: KnowledgeBase) -> None:
        self.knowledge_base = knowledge_base
        self.learned_concepts = 0

    def process_input(self, concept: str) -> bool:
        """Process incoming concept. Returns True if it was new."""
        if self.knowledge_base.add_knowledge(concept):
            self.learned_concepts += 1
            return True
        return False

    def random_exploration(self) -> Optional[str]:
        """Return a randomly selected concept for further exploration."""
        return self.knowledge_base.get_random()
