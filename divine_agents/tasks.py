class Task:
    """Simple task with an urgency level."""

    def __init__(self, name: str, urgency: float):
        self.name = name
        self.urgency = urgency


class TaskAgent:
    """Agent that can handle tasks and perform transitions after executing them."""

    def __init__(self, base_agent):
        self.agent = base_agent
        self.tasks = []

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def execute_tasks(self) -> str:
        for task in self.tasks:
            if task.urgency > 0.8:
                self.agent.update_emotion(1.0, "stress")
                self.agent.tension += 0.5
            else:
                self.agent.update_emotion(0.5, "focus")
                self.agent.tension += 0.2
        self.tasks.clear()
        return self.agent.transition()


class SystemErrorAgent(TaskAgent):
    """Agent that reacts to system errors."""

    def __init__(self, base_agent, system_error: bool = False):
        super().__init__(base_agent)
        self.system_error = system_error

    def check_system(self) -> str:
        if self.system_error:
            self.agent.state = "Jaz"
            self.agent.update_emotion(1.0, "panic")
            self.agent.tension += 0.7
        else:
            self.agent.state = "Ego"
            self.agent.update_emotion(0.5, "calm")
            self.agent.tension += 0.3
        self.agent.history.append(self.agent.state)
        return self.agent.state


class UrgentDecisionAgent(SystemErrorAgent):
    """Agent that can make urgent decisions influencing its state."""

    def __init__(self, base_agent, system_error: bool = False, decision_made: bool = False):
        super().__init__(base_agent, system_error)
        self.decision_made = decision_made

    def make_urgent_decision(self) -> str:
        if not self.decision_made:
            self.decision_made = True
            self.agent.state = "Enotnost"
            self.agent.update_emotion(1.0, "resolution")
            self.agent.tension += 0.8
            self.agent.history.append(self.agent.state)
        return self.agent.state
