from typing import Dict
from .agent import Agent

class EmotionDimensionAgent(Agent):
    """Agent that links emotion intensity with dimensional perception and senses."""

    def __init__(self, name: str, emotion_name: str, intensity: float, dimension: int, state: str = "Ego"):
        super().__init__(name, state=state, tension=0.0, emotion=0.0)
        self.emotion_name = emotion_name
        self.intensity = intensity  # 0-100
        self.dimension = dimension
        self.senses: Dict[str, float] = {}

    def activate(self) -> str:
        """Activate emotion, process it and return transition info."""
        result = [
            f"\u010custvo '{self.emotion_name}' z intenzivnostjo {self.intensity}% je aktivirano v dimenziji {self.dimension}."
        ]
        result.append(self.process_emotion())
        # update parent's emotion and tension for possible state change
        self.update_emotion(self.intensity / 100)
        result.append(f"{self.name} prehaja v stanje: {self.transition()}")
        return "\n".join(result)

    def process_emotion(self) -> str:
        """Compute sense perception based on emotion intensity."""
        if self.intensity > 50:
            intensity_desc = f"Intenzivnost {self.emotion_name} je visoka, zaznana bo mo\u010dna reakcija!"
        else:
            intensity_desc = f"Intenzivnost {self.emotion_name} je zmerna, zaznana bo zmerna reakcija."
        self.senses["touch"] = self.intensity * 0.5
        self.senses["sight"] = self.intensity * 0.4
        percentage_influence = (self.intensity / 100) * self.dimension
        sense_desc = (
            f"\u010custvo vpliva na zaznavo \u010dutila: Dotik: {self.senses['touch']} | Vid: {self.senses['sight']}\n"
            f"Dele\u017e \u010custva v tej dimenziji je: {percentage_influence * 100}%"
        )
        return intensity_desc + "\n" + sense_desc
