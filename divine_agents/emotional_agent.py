from __future__ import annotations
from typing import Dict, Optional

from .agent import Agent


class EmotionalAgent(Agent):
    """Agent with emotional states mapped to colors and thought lines."""

    COLOR_MAP: Dict[str, str] = {
        "anger": "red",
        "calm": "blue",
        "growth": "green",
        "intensity": "UV",
        "sadness": "blue",
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_name: str = "neutral"):
        super().__init__(name, state, tension, emotion)
        self.emotion_name = emotion_name
        self.thought_line = "clear"
        self.update_thought_line()

    def update_emotion(self, value: float, emotion_name: Optional[str] = None) -> None:
        """Update emotion intensity, optionally setting a new emotion name."""
        super().update_emotion(value)
        if emotion_name:
            self.emotion_name = emotion_name
        self.update_thought_line()

    def update_thought_line(self) -> None:
        """Adjust the thought line based on the current emotion name."""
        if self.emotion_name == "anger":
            self.thought_line = "intense, focused"
        elif self.emotion_name == "calm":
            self.thought_line = "clear, rational"
        elif self.emotion_name == "growth":
            self.thought_line = "empathetic, expansive"
        elif self.emotion_name == "intensity":
            self.thought_line = "highly alert, sharp focus"
        else:
            self.thought_line = "neutral, balanced"

    def make_decision(self, task: str) -> str:
        """Return a decision phrase influenced by the current emotion."""
        decision = f"Decision for task '{task}': "
        if self.emotion_name == "anger":
            decision += "Act swiftly and intensely."
        elif self.emotion_name == "calm":
            decision += "Analyze the situation rationally."
        elif self.emotion_name == "growth":
            decision += "Consider the broader perspective."
        elif self.emotion_name == "intensity":
            decision += "Focus on immediate action with precision."
        else:
            decision += "Take balanced, thoughtful action."
        return decision
