from __future__ import annotations
from typing import Callable, List

from .agent import Agent


class EmotionStateCluster:
    """Evaluate and apply state transitions based on the agent's tension and emotion."""

    def __init__(self, agent: Agent):
        self.agent = agent

    def evaluate(self) -> str:
        """Trigger agent transition if thresholds are met."""
        previous = self.agent.state
        new_state = self.agent.transition()
        if previous != new_state:
            return f"{self.agent.name} transitioned to {new_state}"
        return f"{self.agent.name} remains in {new_state}"


class TaskAssignmentCluster:
    """Assign tasks to an agent based on its current state and internal levels."""

    def __init__(self, agent: Agent):
        self.agent = agent

    def assign_task(self, task: str) -> str:
        if self.agent.state in ("Jaz", "Enotnost") and (
            self.agent.emotion > 0.5 or self.agent.tension > 0.7
        ):
            return f"Task '{task}' assigned to {self.agent.name}."
        return f"{self.agent.name} is not ready for task '{task}'."


class LockUnlockCluster:
    """Manage locked tasks or states that require specific conditions."""

    def __init__(self, lock_condition: Callable[[Agent], bool], agent: Agent):
        self.lock_condition = lock_condition
        self.agent = agent
        self.locked = True

    def unlock(self) -> str:
        if self.lock_condition(self.agent):
            self.locked = False
            return f"Lock is unlocked for {self.agent.name}."
        return f"{self.agent.name} cannot unlock due to unsatisfied conditions."

    def check_status(self) -> str:
        return (
            f"Lock is active for {self.agent.name}."
            if self.locked
            else f"Lock is inactive for {self.agent.name}."
        )


class ReflectionSelfAwarenessCluster:
    """Provide reflective messages based on the agent's current state."""

    def __init__(self, agent: Agent):
        self.agent = agent

    def reflect(self) -> str:
        if self.agent.state == "Enotnost":
            return f"{self.agent.name} reflects: 'I am at unity, all is connected.'"
        return f"{self.agent.name} reflects: 'Currently in {self.agent.state}.'"


class DynamicSystem:
    """Integrate clusters to update the agent in a single step."""

    def __init__(self, agent: Agent):
        self.agent = agent
        self.emotion_cluster = EmotionStateCluster(agent)
        self.task_cluster = TaskAssignmentCluster(agent)
        self.lock_cluster = LockUnlockCluster(self.lock_condition, agent)
        self.reflect_cluster = ReflectionSelfAwarenessCluster(agent)

    def lock_condition(self, agent: Agent) -> bool:
        return agent.state == "Ego" and agent.emotion > 0.5

    def update(self) -> List[str]:
        messages = [self.emotion_cluster.evaluate()]
        messages.append(self.task_cluster.assign_task("Transition Task"))
        messages.append(self.reflect_cluster.reflect())
        messages.append(self.lock_cluster.check_status())
        messages.append(self.lock_cluster.unlock())
        return messages
