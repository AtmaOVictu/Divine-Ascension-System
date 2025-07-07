"""Emotional processing utilities for agents."""

from .agent import Agent


class EmotionalAgent(Agent):
    """Agent dedicated to processing and confirming emotional states."""

    def __init__(self):
        super().__init__(name="Emotional Agent")

    def process_emotion(self, emotion: str) -> str:
        """Process emotion and return a textual confirmation."""
        negative = {"anger", "frustration"}
        positive = {"happiness", "joy"}
        if emotion in negative:
            return "Emotion confirmed: Negative"
        if emotion in positive:
            return "Emotion confirmed: Positive"
        return "Emotion confirmed: Neutral"


class EmotionalBox:
    """Symbolic container for emotional data."""

    def __init__(self, emotion: str):
        self.emotion = emotion
        self.status = "unprocessed"

    def process(self, emotional_agent: EmotionalAgent) -> str:
        """Process the contained emotion through the given agent."""
        self.status = emotional_agent.process_emotion(self.emotion)
        return self.status


class MainTaskAgent(Agent):
    """Main agent that handles tasks while confirming emotions."""

    def __init__(self, name: str = "Main Task Agent"):
        super().__init__(name=name)

    def handle_task(self, task: str, emotional_box: EmotionalBox) -> str:
        """Process task after confirming the emotional state."""
        status = emotional_box.process(EmotionalAgent())
        if status == "Emotion confirmed: Negative":
            return "Task halted due to negative emotional state."
        return f"Task '{task}' completed."
