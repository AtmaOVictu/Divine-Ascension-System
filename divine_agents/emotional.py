class EmotionalAgent:
    """Agent dedicated to processing and confirming emotional states."""

    def __init__(self, name: str = "Emotional Agent"):
        self.name = name

    def process_emotion(self, emotion: str) -> str:
        """Return a confirmation string based on the emotion."""
        if emotion in ["anger", "frustration"]:
            return "Emotion confirmed: Negative"
        if emotion in ["happiness", "joy"]:
            return "Emotion confirmed: Positive"
        return "Emotion confirmed: Neutral"


class EmotionalBox:
    """Symbolic container to isolate emotional data."""

    def __init__(self, emotion: str):
        self.emotion = emotion
        self.status = "unprocessed"

    def process(self, emotional_agent: EmotionalAgent) -> str:
        """Process emotion with the given agent and update status."""
        self.status = emotional_agent.process_emotion(self.emotion)
        return self.status


class MainTaskAgent:
    """Agent that handles tasks while checking emotional context."""

    def __init__(self, name: str = "Main Task Agent"):
        self.name = name

    def handle_task(self, task: str, emotional_box: EmotionalBox) -> str:
        """Process task after emotion confirmation."""
        emotion_status = emotional_box.process(EmotionalAgent())
        if emotion_status != "Emotion confirmed: Negative":
            return f"Task '{task}' completed."
        return "Task halted due to negative emotional state."
