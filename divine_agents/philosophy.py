import time
from typing import Dict, List

from .memory import Memory


def extract_relationships(concept: str) -> List[str]:
    """Extract simple relationships from a concept."""
    return concept.split()


def analyze_concept(concept: str) -> Dict[str, List[str]]:
    """Analyze concept for its relationships."""
    relationships = extract_relationships(concept)
    return {"relationships": relationships}


def parse_philosophical_statement(statement: str, memory: Memory) -> str:
    """Parse and store a philosophical statement for reflection."""
    parsed_statement = analyze_concept(statement)
    memory.store_long_term({"concept": parsed_statement, "timestamp": time.time()})
    return f"Statement '{statement}' parsed and stored for reflection."
