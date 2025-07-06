class NanoAgent:
    """Agent performing tiny specialised tasks."""

    def __init__(self, name: str, task: str):
        self.name = name
        self.task = task

    def execute(self, params: dict):
        """Execute nano-task based on assigned role."""
        if self.task == "analyze_temperature":
            return params.get("temperature", 0) * 1.2
        if self.task == "check_pressure":
            return params.get("pressure", 0) * 0.95
        return None
