from .agent import Agent
from .dialogue import philosophical_dialogue
from .orchestrator import (
    OrchestratorAgent,
    GitHubIntegrationAgent,
    FileSearchAgent,
    BaseProcessingAgent,
)

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "OrchestratorAgent",
    "GitHubIntegrationAgent",
    "FileSearchAgent",
    "BaseProcessingAgent",
]
