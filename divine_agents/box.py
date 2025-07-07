class SymbolicBox:
    """Container representing a symbolic box for storing data and stages."""

    def __init__(self, stage: str, data: dict):
        self.stage = stage
        self.data = data

    def transition(self, stage: str, data_update: dict) -> None:
        """Transition the box to a new stage and update its data."""
        self.stage = stage
        self.data.update(data_update)

    def get_data(self) -> dict:
        """Return stored data."""
        return self.data


class TaskBox(SymbolicBox):
    """Box that can contain sub tasks in a recursive structure."""

    def __init__(self, task_name: str):
        super().__init__(stage="∴", data={"task_name": task_name, "status": "initiated"})
        self.sub_tasks = []

    def add_sub_task(self, sub_task_name: str) -> None:
        box = SymbolicBox(stage="∴", data={"sub_task_name": sub_task_name, "status": "initiated"})
        self.sub_tasks.append(box)

    def unpack_all_sub_tasks(self) -> None:
        for sub_task in self.sub_tasks:
            sub_task.transition("∆", {"status": "processed"})

    def complete(self) -> None:
        self.transition("⊘", {"status": "completed"})
