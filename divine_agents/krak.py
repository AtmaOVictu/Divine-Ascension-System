"""Krak module defines specialized agents with tasks and history."""
from .agent import Agent


class Krak(Agent):
    """An ontological agent that manages tasks and adapts to emotions."""

    def __init__(self, name: str, state: str = "Ego", task: str = "none"):
        super().__init__(name, state)
        self.task = task
        self.task_history = []

    def update_task(self, new_task: str) -> None:
        """Set a new task and log the previous task."""
        self.task_history.append(self.task)
        self.task = new_task

    def transition(self) -> str:
        """Transition state and update task based on the new state."""
        new_state = super().transition()
        if new_state == "Jaz":
            self.update_task("dialogue")
        elif new_state == "Enotnost":
            self.update_task("reflect")
        return new_state

    def adapt_task_based_on_emotion(self) -> None:
        """Adjust task depending on current emotion intensity."""
        if self.emotion > 0.7:
            self.update_task("high_emotion_task")
        elif self.emotion > 0.3:
            self.update_task("moderate_emotion_task")
        else:
            self.update_task("low_emotion_task")
