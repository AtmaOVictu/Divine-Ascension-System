from .agent import Agent

class Krak(Agent):
    """Specialized agent representing a working branch in the system."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, task: str = "none"):
        super().__init__(name, state, tension, emotion)
        self.task = task

    def update_task(self, new_task: str) -> None:
        """Update the current task of the krak."""
        self.task = new_task

    def adapt_task_based_on_emotion(self) -> None:
        """Automatically adjust task depending on emotion intensity."""
        if self.emotion > 0.7:
            self.update_task("high_emotion_task")
        else:
            self.update_task("low_emotion_task")

    def update_emotion(self, value: float) -> None:
        """Update emotion and adapt task accordingly."""
        super().update_emotion(value)
        self.adapt_task_based_on_emotion()
