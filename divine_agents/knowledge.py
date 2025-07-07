class RecursiveSymbolicBox:
    """Base class representing a symbolic container that can be unpacked."""
    def __init__(self, stage: str, data: dict):
        self.stage = stage
        self.data = data

    def unpack(self) -> dict:
        """Return contained data without modification."""
        return self.data


class LukaKnowledgeBox(RecursiveSymbolicBox):
    """A recursive box that contains Luka's ontological knowledge."""

    def __init__(self, concept: str, explanation: str):
        super().__init__(stage="∴", data={"concept": concept, "explanation": explanation})

    def unpack_knowledge(self) -> dict:
        """Unpack Luka's knowledge for processing."""
        return self.unpack()


class EmotionalBox:
    """Container for emotions handled by a dedicated agent."""

    def __init__(self, emotion: str):
        self.emotion = emotion

    def process_emotion(self, agent: "EmotionalAgent") -> str:
        """Delegate emotion validation to an EmotionalAgent."""
        return agent.process_emotion(self.emotion)


from .agent import Agent


class CodexWithLukaKnowledge(Agent):
    """Agent equipped with Luka's ontological knowledge."""

    def __init__(self, name: str = "Codex"):
        super().__init__(name)
        self.knowledge_boxes = []

    def add_knowledge(self, box: LukaKnowledgeBox) -> None:
        """Store Luka's knowledge for later processing."""
        self.knowledge_boxes.append(box)

    def process_knowledge(self):
        """Process all stored knowledge boxes."""
        return [box.unpack_knowledge() for box in self.knowledge_boxes]


class EmotionalAgent(Agent):
    """Agent responsible for validating emotional states."""

    def process_emotion(self, emotion: str) -> str:
        if emotion in ["anger", "frustration"]:
            return "Emotion confirmed: Negative"
        if emotion in ["joy", "happiness"]:
            return "Emotion confirmed: Positive"
        return "Emotion confirmed: Neutral"
