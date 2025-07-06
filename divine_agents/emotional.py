from dataclasses import dataclass
from typing import List
from .agent import Agent

@dataclass
class EmotionState:
    """Represents an emotion and its intensity."""
    kind: str
    intensity: float

class EmotionalAgent(Agent):
    """Agent that tracks a specific emotion affecting transitions and dialogue."""

    def __init__(self, name: str, state: str = "Ego",
                 tension: float = 0.0, emotion: EmotionState | None = None):
        intensity = emotion.intensity if emotion else 0.0
        super().__init__(name, state, tension, intensity)
        self.emotion_state = emotion or EmotionState("neutral", 0.0)

    def set_emotion(self, kind: str, intensity: float) -> None:
        """Set current emotion and update tension accordingly."""
        self.emotion_state = EmotionState(kind, intensity)
        self.update_emotion(intensity)

    def emotional_response(self, question: str) -> str:
        """Return philosophical response that reflects the current emotion."""
        base = self.respond(question)
        return f"{base} (Čustvo: {self.emotion_state.kind}, intenziteta: {self.emotion_state.intensity})"

def emotional_dialogue(a1: EmotionalAgent, a2: EmotionalAgent) -> List[str]:
    """Generate a short emotional philosophical dialogue between two agents."""
    convo: List[str] = []
    convo.append(f"{a1.name} ({a1.state}): {a1.emotional_response('Kaj je resnica?')}")
    convo.append(f"{a2.name} ({a2.state}): {a2.emotional_response('Kaj je resnica?')}")

    # agents experience emotions which may trigger state transitions
    a1.set_emotion('anger', 0.6)
    convo.append(f"{a1.name} prehaja v stanje: {a1.transition()}")

    a2.set_emotion('joy', 0.4)
    convo.append(f"{a2.name} ostaja v stanju: {a2.transition()}")

    convo.append(f"{a1.name}: {a1.emotional_response('Kaj je resnica?')}")
    convo.append(f"{a2.name}: {a2.emotional_response('Kaj je resnica?')}")

    return convo
