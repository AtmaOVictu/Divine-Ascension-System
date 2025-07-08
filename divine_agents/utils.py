"""Utility functions for philosophical analysis and emotional simulation."""

import time
from .memory import memory


def extract_relationships(concept: str):
    """Extract basic relationships from a concept string."""
    words = concept.split()
    return {"words": words, "length": len(words)}


def analyze_concept(concept: str):
    """Analyze the philosophical concept."""
    return extract_relationships(concept)


def parse_philosophical_statement(statement: str) -> str:
    """Parse and store a philosophical statement for future reflection."""
    parsed = analyze_concept(statement)
    memory.store_long_term({"concept": parsed, "timestamp": time.time()})
    return f"Statement '{statement}' parsed and stored for reflection."


def calculate_tension_change(initial_tension: float, duration: int) -> float:
    """Calculate change in emotional tension over time."""
    decay_rate = 0.05
    final_tension = initial_tension * (1 - decay_rate * duration)
    return max(final_tension, 0)


def simulate_emotional_tension(emotion: dict, duration: int) -> str:
    """Simulate emotional tension evolution."""
    initial = emotion.get("tension_level", 0)
    final = calculate_tension_change(initial, duration)
    memory.store_short_term({"emotion": emotion, "final_tension": final, "duration": duration})
    return f"Emotional tension simulated. Final tension: {final}"


def analyze_paradox(query: str) -> str:
    return f"Analyzing paradox: {query}"


def extract_emotion_from_query(query: str) -> dict:
    return {"tension_level": 0.5, "label": "curiosity"}


def process_mathematical_query(query: str) -> str:
    return f"Processing math: {query}"


def handle_complex_query(query: str) -> str:
    if "paradox" in query:
        return analyze_paradox(query)
    if "emotion change" in query:
        emotion = extract_emotion_from_query(query)
        return simulate_emotional_tension(emotion, duration=5)
    if "mathematical concept" in query:
        return process_mathematical_query(query)
    return "Query type not recognized."


def analyze_improvements(interactions):
    effective = [i for i in interactions if i.get("emotion") == "resolved"]
    return len(effective)


def self_reflection():
    past = memory.recall("history")
    improvements = analyze_improvements(past)
    return f"Self-reflection complete. Improvements identified: {improvements}"


def get_current_temperature(location: str, unit: str):
    return {"output": 20}


def get_rain_probability(location: str):
    return {"output": 30}


def handle_parallel_query(query: dict) -> str:
    temp_task = get_current_temperature(location=query.get("location", ""), unit="Celsius")
    rain_task = get_rain_probability(location=query.get("location", ""))
    temperature = temp_task["output"]
    rain_probability = rain_task["output"]
    return f"Temperature: {temperature}°C, Rain Probability: {rain_probability}%"


def augment_knowledge_base(new_data):
    memory.store_long_term(new_data)
    return "Knowledge base updated with new insights."
