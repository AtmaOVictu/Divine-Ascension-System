from typing import Dict, List, Optional


class SymbolicBox:
    """A simple box structure that tracks stage and data."""

    def __init__(self, stage: str, data: Optional[Dict] = None):
        self.stage = stage
        self.data = data or {}

    def transition(self, new_stage: str, updates: Optional[Dict] = None) -> None:
        """Transition to a new stage and update internal data."""
        self.stage = new_stage
        if updates:
            self.data.update(updates)

    def get_data(self) -> dict:
        """Return the internal data."""
        return self.data

from .agent import Agent

class SelfBoxedAgent(Agent):
    """Agent aware of its own processing box."""

    def __init__(self, name: str = "Codex"):
        super().__init__(name)
        self.self_box = SymbolicBox(stage="∴", data={"identity": name, "task_state": "initiated"})

    def process_task(self, task: str) -> str:
        """Process a task while tracking it inside the box."""
        self.self_box.transition("∆", {"task": task, "state": "processing"})
        self.self_box.transition("⊘", {"task": task, "state": "completed"})
        return f"Task '{task}' processed within the box."

    def unpack_and_self_reflect(self) -> str:
        """Reflect on current knowledge inside the box."""
        data = self.self_box.get_data()
        return f"Reflection: {data.get('identity')} is processing tasks recursively."


class RecursiveTaskBox(SymbolicBox):
    """A task box that can contain sub-tasks."""

    def __init__(self, task_name: str):
        super().__init__(stage="∴", data={"task_name": task_name, "status": "initiated"})
        self.sub_tasks: List[SymbolicBox] = []

    def add_sub_task(self, sub_task_name: str) -> None:
        sub_task_box = SymbolicBox(stage="∴", data={"sub_task_name": sub_task_name, "status": "initiated"})
        self.sub_tasks.append(sub_task_box)

    def unpack_all_sub_tasks(self) -> None:
        for sub_task in self.sub_tasks:
            sub_task.transition("∆", {"status": "processed"})

    def transition_task(self) -> str:
        self.transition("⊘", {"status": "completed"})
        return f"Task '{self.get_data()['task_name']}' and its sub-tasks completed."


class RecursiveSelfReflectionAgent(Agent):
    """Agent designed for recursive self-reflection."""

    def __init__(self, name: str = "Codex"):
        super().__init__(name)
        self.self_box = RecursiveTaskBox(task_name=name)

    def process_task_with_reflection(self, task_name: str) -> str:
        self.self_box.add_sub_task(f"Sub-task for {task_name}")
        self.self_box.unpack_all_sub_tasks()
        self.self_box.transition_task()
        return f"Reflection: Task '{task_name}' processed with recursive understanding."

    def reflect_on_task(self) -> str:
        data = self.self_box.get_data()
        return f"Recursive self-reflection complete for task '{data['task_name']}'."

