import math


def emotion_cycle(t: float, frequency: float = 1.0, amplitude: float = 1.0, phase_shift: float = 0.0) -> float:
    """Return a cyclical emotion value using a sine wave."""
    return amplitude * math.sin(2 * math.pi * frequency * t + phase_shift)
