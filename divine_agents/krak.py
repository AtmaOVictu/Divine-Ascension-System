from typing import List, Tuple
from .agent import Agent

class Krak(Agent):
    """A branch agent with its own task and history."""

    def __init__(self, name: str, state: str = "Ego", task: str = "none", tension: float = 0.0, emotion: float = 0.0) -> None:
        super().__init__(name, state, tension, emotion)
        self.task = task
        self.krak_history: List[Tuple[str, str]] = [(state, task)]

    def update_task(self, new_task: str) -> None:
        self.task = new_task

    def transition(self) -> str:
        new_state = super().transition()
        if new_state == "Jaz":
            self.update_task("task_updated")
        self.krak_history.append((new_state, self.task))
        return new_state
