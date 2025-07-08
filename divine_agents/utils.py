from __future__ import annotations

import time
from typing import Dict

from .memory import Memory


def analyze_concept(concept: str) -> Dict[str, int]:
    """Analyze a philosophical concept by counting word occurrences."""
    words = concept.lower().split()
    return {word: words.count(word) for word in set(words)}


def parse_philosophical_statement(statement: str, memory: Memory) -> str:
    """Parse and store the philosophical statement for future reflection."""
    parsed = analyze_concept(statement)
    memory.store_long_term({"concept": parsed, "timestamp": time.time()})
    return f"Statement '{statement}' parsed and stored for reflection."


def calculate_tension_change(initial: float, duration: int) -> float:
    """Simple decay model for emotional tension."""
    decay_rate = 0.05
    final = initial * (1 - decay_rate * duration)
    return max(final, 0.0)


def simulate_emotional_tension(emotion: Dict[str, float], duration: int, memory: Memory) -> str:
    """Simulate emotional tension change over time."""
    initial = emotion.get("tension_level", 0.0)
    final_tension = calculate_tension_change(initial, duration)
    memory.store_short_term({"emotion": emotion, "final_tension": final_tension, "duration": duration})
    return f"Emotional tension simulated. Final tension: {final_tension}"


def handle_complex_query(query: str, memory: Memory) -> str:
    """Handle a complex user query using simple heuristics."""
    if "paradox" in query:
        return parse_philosophical_statement(query, memory)
    if "emotion change" in query:
        return simulate_emotional_tension({"tension_level": 0.5}, 5, memory)
    return "Query not understood."


def analyze_improvements(interactions):
    """Analyze past interactions for potential improvements."""
    return len([i for i in interactions if i.get("emotion") == "resolved"])


def self_reflection(memory: Memory) -> str:
    """Reflect on past interactions stored in memory."""
    past = memory.recall("long")
    improvements = analyze_improvements(past)
    return f"Self-reflection complete. Improvements identified: {improvements}"

