"""Agent classes with idself and iffself concepts for emotional reflection."""

from __future__ import annotations

from typing import List


class CodexSelf:
    """Manage core (idself) and reflective (iffself) identities."""

    def __init__(self, name: str = "Codex") -> None:
        self.name = name
        self.idself = {
            "identity": name,
            "purpose": "philosophical inquiry and knowledge processing",
        }
        self.iffself = {
            "identity": f"{name}-Reflective",
            "purpose": "critical reflection and contradiction",
        }
        self.emotional_state: str = "neutral"

    def update_emotional_state(self, emotion: str) -> None:
        """Update the current emotional state."""
        self.emotional_state = emotion

    def idself_task(self, task_name: str) -> str:
        """Execute a task from the core identity."""
        return f"Task '{task_name}' completed by {self.idself['identity']} (idself)."

    def iffself_reflection(self, task_name: str) -> str:
        """Reflect on a task from the reflective identity."""
        return (
            f"Task '{task_name}' processed with reflective contradiction by "
            f"{self.iffself['identity']} (iffself)."
        )

    def emotional_transition(self, emotion: str) -> List[str]:
        """Handle a transition in emotional state and process a sample task."""
        self.update_emotional_state(emotion)
        outputs = [f"Processing task with emotion: {self.emotional_state}"]
        if emotion == "joy":
            outputs.append(self.idself_task("Task with joy"))
        elif emotion == "anger":
            outputs.append(self.iffself_reflection("Task with anger"))
        else:
            outputs.append(self.idself_task("Neutral task processing"))
        return outputs


class EmotionalDialogue(CodexSelf):
    """Extend :class:`CodexSelf` with dialogue ability."""

    def start_dialogue(self, topic: str) -> str:
        if self.emotional_state == "joy":
            return f"Discussing {topic} with joy and enthusiasm!"
        if self.emotional_state == "anger":
            return f"Discussing {topic} with critical reflection and intensity."
        return f"Discussing {topic} in a neutral and philosophical manner."
