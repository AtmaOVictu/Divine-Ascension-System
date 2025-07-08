from .agent import Agent


class KnowledgeBase:
    """Track processed knowledge to avoid repetition."""

    def __init__(self):
        self.processed_knowledge = set()

    def add_knowledge(self, knowledge: str) -> bool:
        """Add knowledge if not already processed, return True if new."""
        if knowledge not in self.processed_knowledge:
            self.processed_knowledge.add(knowledge)
            return True
        return False


class AutoLearningSystem:
    """Continuously processes new knowledge using agents."""

    def __init__(self, agent: Agent, knowledge_base: KnowledgeBase):
        self.agent = agent
        self.knowledge_base = knowledge_base
        self.learned = 0

    def process(self, knowledge: str) -> str:
        """Process a piece of knowledge and return agent response."""
        if self.knowledge_base.add_knowledge(knowledge):
            self.agent.update_emotion("joy", 0.6)
        else:
            self.agent.update_emotion("fear", 0.3)
        self.agent.transition()
        self.learned += 1
        return self.agent.respond(knowledge)
