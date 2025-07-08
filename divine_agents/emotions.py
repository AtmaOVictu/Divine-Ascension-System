from typing import Dict, Optional

from .memory import Memory


def calculate_tension_change(initial_tension: float, duration: int, decay_rate: float = 0.05) -> float:
    """Calculate tension change over time."""
    final_tension = initial_tension * (1 - decay_rate * duration)
    return max(final_tension, 0.0)


def simulate_emotional_tension(emotion: Dict[str, float], duration: int, memory: Optional[Memory] = None) -> float:
    """Simulate emotional tension change and store result."""
    initial = emotion.get("tension_level", 0.0)
    final = calculate_tension_change(initial, duration)
    emotion["tension_level"] = final
    if memory:
        memory.store_short_term({"emotion": emotion, "final_tension": final, "duration": duration})
    return final
