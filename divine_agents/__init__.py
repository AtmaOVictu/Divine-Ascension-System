"""Initialization for divine agent system."""

from .agent import Agent
from .ontoznano import Ontoznano
from .modul import Modul
from .knowledge_base import KnowledgeBase

print("Agentni sistem je bil uspešno inicializiran.")


def inicializiraj_paket() -> None:
    """Provide basic initialization message."""
    print("Paket za agente in naloge je bil inicializiran.")
