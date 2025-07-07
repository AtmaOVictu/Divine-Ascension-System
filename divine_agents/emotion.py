"""Emotional processing utilities for agents."""

from .agent import Agent


class EmotionalAgent(Agent):
    """Agent dedicated to confirming emotional states."""

    def __init__(self):
        super().__init__(name="Emotional Agent")

    def process_emotion(self, emotion: str) -> str:
        """Return a textual confirmation for the given emotion."""
        if emotion in {"anger", "frustration"}:
            return "Emotion confirmed: Negative"
        if emotion in {"happiness", "joy"}:
            return "Emotion confirmed: Positive"
        return "Emotion confirmed: Neutral"


class EmotionalBox:
    """Container for emotional data to be processed separately."""

    def __init__(self, emotion: str):
        self.emotion = emotion
        self.status = "unprocessed"

    def process(self, emotional_agent: EmotionalAgent) -> str:
        """Process the stored emotion using the provided agent."""
        self.status = emotional_agent.process_emotion(self.emotion)
        return self.status


class MainTaskAgent(Agent):
    """Agent that performs tasks while confirming emotional state."""

    def handle_task(self, task: str, emotional_box: EmotionalBox) -> str:
        """Process a task only if emotion allows it."""
        emotion_status = emotional_box.process(EmotionalAgent())

        if emotion_status == "Emotion confirmed: Negative":
            # negative emotions halt progress
            self.update_emotion(0.8)
            self.transition()
            return "Task halted due to negative emotional state."

        if emotion_status == "Emotion confirmed: Positive":
            self.update_emotion(0.6)
        else:
            self.update_emotion(0.3)

        self.transition()
        return f"Task '{task}' completed."
