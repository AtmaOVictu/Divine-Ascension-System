import re
import time
from typing import Dict, List


class Memory:
    """Simple memory store for agents."""

    def __init__(self) -> None:
        self.short_term: List[Dict] = []
        self.long_term: List[Dict] = []

    def store_short_term(self, data: Dict) -> None:
        self.short_term.append(data)

    def store_long_term(self, data: Dict) -> None:
        self.long_term.append(data)

    def recall(self, mem_type: str = "short") -> List[Dict]:
        if mem_type == "long":
            return list(self.long_term)
        return list(self.short_term)


def extract_relationships(concept: str) -> List[str]:
    """Extract simple relationships from a concept string."""
    return re.findall(r"\b\w+\b", concept)


def analyze_concept(concept: str) -> List[str]:
    """Analyze a philosophical concept for its core terms."""
    return extract_relationships(concept)


def parse_philosophical_statement(statement: str, memory: Memory) -> List[str]:
    """Parse and store the philosophical statement for future reflection."""
    parsed_statement = analyze_concept(statement)
    memory.store_long_term({"concept": parsed_statement, "timestamp": time.time()})
    return parsed_statement


def calculate_tension_change(initial_tension: float, duration: int, decay_rate: float = 0.05) -> float:
    """Calculate how emotional tension changes over time."""
    final_tension = initial_tension * (1 - decay_rate * duration)
    return max(final_tension, 0)


def simulate_emotional_tension(emotion: Dict[str, float], duration: int, memory: Memory) -> float:
    """Simulate emotional tension change over time."""
    initial_tension = emotion.get("tension_level", 0)
    final_tension = calculate_tension_change(initial_tension, duration)
    memory.store_short_term({"emotion": emotion, "final_tension": final_tension, "duration": duration})
    return final_tension


def handle_complex_query(query: str, agent_state: Dict[str, float], memory: Memory) -> str:
    """Handle complex or nuanced queries."""
    if "paradox" in query:
        parsed = parse_philosophical_statement(query, memory)
        return f"Paradox analyzed: {parsed}"
    if "emotion change" in query:
        result = simulate_emotional_tension(agent_state, duration=5, memory=memory)
        return f"Emotion adjusted to tension {result:.2f}"
    return "Query not understood"


def self_reflection(memory: Memory) -> str:
    """Reflect on stored interactions for improvements."""
    past_interactions = memory.recall("long") + memory.recall("short")
    improvements = len(past_interactions)
    return f"Self-reflection complete. Entries reviewed: {improvements}"
