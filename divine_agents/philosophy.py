"""Utilities for philosophical analysis and emotional dynamics."""

from typing import Dict, Any, List
import time

from .memory import Memory
from .agent import Agent

memory = Memory()


def extract_relationships(concept: str) -> List[str]:
    """Simplistic relationship extraction by splitting concept into keywords."""
    return [word.strip('.,') for word in concept.lower().split()]


def analyze_concept(concept: str) -> List[str]:
    """Analyze the philosophical concept for relationships."""
    return extract_relationships(concept)


def parse_philosophical_statement(statement: str) -> str:
    """Parse and store philosophical statement for future reflection."""
    parsed = analyze_concept(statement)
    memory.store_long_term({"concept": parsed, "timestamp": time.time()})
    return f"Statement '{statement}' parsed and stored."


def calculate_tension_change(initial_tension: float, duration: float) -> float:
    """Calculate tension decay over time."""
    decay_rate = 0.05
    final = initial_tension * (1 - decay_rate * duration)
    return max(final, 0.0)


def simulate_emotional_tension(emotion: Dict[str, Any], duration: float) -> str:
    """Simulate emotional tension change and store the result."""
    level = emotion.get("tension_level", 0.0)
    final = calculate_tension_change(level, duration)
    memory.store_short_term({"emotion": emotion, "final_tension": final, "duration": duration})
    return f"Emotional tension simulated. Final tension: {final}"


def handle_complex_query(query: str) -> str:
    """Handle nuanced queries by delegating to specialized functions."""
    if "paradox" in query.lower():
        return parse_philosophical_statement(query)
    if "emotion change" in query.lower():
        emotion = {"tension_level": 1.0}
        return simulate_emotional_tension(emotion, duration=5)
    return parse_philosophical_statement(query)


def analyze_improvements(interactions: List[Dict[str, Any]]) -> int:
    """Count resolved emotional interactions for improvement metric."""
    return sum(1 for i in interactions if i.get("emotion") == "resolved")


def self_reflection() -> str:
    """Analyze history from memory and provide improvement feedback."""
    past = memory.recall("long_term")
    improvements = analyze_improvements(past)
    return f"Self-reflection complete. Improvements identified: {improvements}"
