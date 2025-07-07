"""Agent with emotional state mapped to colors and thought lines."""

from typing import Optional

from .agent import Agent


class EmotionalAgent(Agent):
    """Extends ``Agent`` with symbolic emotional states."""

    COLOR_MAP = {
        "anger": "red",
        "calm": "blue",
        "growth": "green",
        "intensity": "UV",
        "sadness": "blue",
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_label: Optional[str] = None):
        super().__init__(name, state, tension, emotion)
        self.emotion_label = emotion_label or "calm"
        self.thought_line = "clear"

    def update_emotion(self, value: float, label: str) -> None:
        """Update emotion intensity and label, adjusting tension."""
        super().update_emotion(value)
        self.emotion_label = label
        self._update_thought_line()

    def _update_thought_line(self) -> None:
        if self.emotion_label == "anger":
            self.thought_line = "intense, focused"
        elif self.emotion_label == "calm":
            self.thought_line = "clear, rational"
        elif self.emotion_label == "growth":
            self.thought_line = "empathetic, expansive"
        elif self.emotion_label == "intensity":
            self.thought_line = "highly alert, sharp focus"
        else:
            self.thought_line = "neutral, balanced"

    def describe_emotion(self) -> str:
        """Return a human readable description of the current emotion."""
        color = self.COLOR_MAP.get(self.emotion_label, "unknown")
        return (
            f"{self.name} feels {self.emotion_label} "
            f"({color}); thought line: {self.thought_line}"
        )

    def make_decision(self, task: str) -> str:
        """Return a decision statement influenced by the emotional state."""
        decision = f"Decision for task '{task}': "
        if self.emotion_label == "anger":
            decision += "Act swiftly and intensely."
        elif self.emotion_label == "calm":
            decision += "Analyze the situation rationally."
        elif self.emotion_label == "growth":
            decision += "Consider the broader perspective."
        elif self.emotion_label == "intensity":
            decision += "Focus on immediate action with precision."
        else:
            decision += "Take balanced, thoughtful action."
        return decision

