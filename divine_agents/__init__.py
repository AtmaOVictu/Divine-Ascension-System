"""Initialization for the divine_agents package."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .ego import Ego
from .ontoznano import Ontoznano
from .modul import Modul
from .knowledge_base import KnowledgeBase
from .codex import Codex

print("Agentni sistem inicializiran.")


def inicializiraj_paket() -> None:
    """Helper for explicit initialization."""
    print("Paket za agente in naloge je bil inicializiran.")
