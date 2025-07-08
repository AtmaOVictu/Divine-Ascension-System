from __future__ import annotations

import asyncio
from typing import Any, Dict, List

from .memory import Memory


def extract_relationships(concept: str) -> List[str]:
    """Trivial relationship extractor used for demonstration."""
    return [word.strip(".,") for word in concept.split() if len(word) > 3]


def analyze_concept(concept: str) -> List[str]:
    """Analyze a concept and return related terms."""
    return extract_relationships(concept)


def parse_philosophical_statement(statement: str, memory: Memory) -> str:
    """Parse and store a philosophical statement for later reflection."""
    parsed = analyze_concept(statement)
    memory.store_long_term({"concept": parsed})
    return f"Statement '{statement}' parsed and stored for reflection."


def calculate_tension_change(initial_tension: float, duration: int) -> float:
    """Calculate tension change over time using a simple decay model."""
    decay_rate = 0.05
    final_tension = initial_tension * (1 - decay_rate * duration)
    return max(final_tension, 0.0)


def simulate_emotional_tension(emotion: Dict[str, Any], duration: int, memory: Memory) -> str:
    """Simulate emotional tension change and store the result."""
    initial_tension = emotion.get("tension_level", 0.0)
    final_tension = calculate_tension_change(initial_tension, duration)
    memory.store_short_term({"emotion": emotion, "final_tension": final_tension, "duration": duration})
    return f"Emotional tension simulated. Final tension: {final_tension}"


def handle_complex_query(query: str, agent, memory: Memory) -> str:
    """Break down a complex query and act sequentially."""
    if "history" in query:
        history = agent.history
        memory.store_short_term({"query": query, "history": history})
        return f"History length: {len(history)}"
    if "emotion change" in query:
        emotion = {"tension_level": agent.tension}
        return simulate_emotional_tension(emotion, duration=5, memory=memory)
    return "Query not understood."


async def get_current_temperature(location: str, unit: str = "Celsius") -> int:
    await asyncio.sleep(0.01)
    return 20


async def get_rain_probability(location: str) -> int:
    await asyncio.sleep(0.01)
    return 10


async def handle_parallel_query(query: Dict[str, Any]) -> str:
    """Handle queries requiring parallel tasks."""
    temp_task = asyncio.create_task(get_current_temperature(query["location"]))
    rain_task = asyncio.create_task(get_rain_probability(query["location"]))
    temperature = await temp_task
    rain_probability = await rain_task
    return f"Temperature: {temperature}\u00b0C, Rain Probability: {rain_probability}%"


def augment_knowledge_base(memory: Memory, new_data: Dict[str, Any]) -> str:
    """Add new insights to long-term memory."""
    memory.store_long_term(new_data)
    return "Knowledge base updated with new insights."


def analyze_improvements(interactions: List[Dict[str, Any]]) -> int:
    """Simple analysis for improvements."""
    return len([i for i in interactions if i.get("emotion") == "resolved"])


def self_reflection(memory: Memory) -> str:
    """Reflect on past interactions to adapt responses."""
    past = memory.recall("long")
    improvements = analyze_improvements(past)
    return f"Self-reflection complete. Improvements identified: {improvements}"
