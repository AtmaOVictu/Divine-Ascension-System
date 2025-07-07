from .agent import Agent


class Krak(Agent):
    """Specialized Agent representing an independent functional unit."""

    def __init__(self, name: str, state: str = "Ego", task: str = "none"):
        super().__init__(name, state)
        self.task = task
        self.task_history = [task]

    def update_task(self, new_task: str) -> None:
        """Update the current task and store it in history."""
        self.task = new_task
        self.task_history.append(new_task)

    def adapt_task_based_on_emotion(self) -> None:
        """Adjust task based on current emotion level."""
        if self.emotion > 0.7:
            self.update_task("high_emotion_task")
        else:
            self.update_task("low_emotion_task")

    def update_emotion(self, value: float) -> None:
        super().update_emotion(value)
        self.adapt_task_based_on_emotion()

    def transition(self) -> str:
        new_state = super().transition()
        if new_state == "Jaz":
            self.update_task("task_updated")
        return new_state
