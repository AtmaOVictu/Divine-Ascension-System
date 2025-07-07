"""Core package for ontological agents."""
from .agent import Agent
from .dialogue import philosophical_dialogue
from .repl import run_demo_loop

__all__ = ["Agent", "philosophical_dialogue", "run_demo_loop"]
