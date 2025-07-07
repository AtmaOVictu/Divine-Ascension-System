"""Collection of agents for philosophical dialogues."""

from .agent import Agent
from .orchestrator import OrchestratorAgent, SubAgent
from .github_agent import GitHubIntegrationAgent
from .file_search_agent import FileSearchAgent
from .dialogue import philosophical_dialogue

__all__ = [
    "Agent",
    "OrchestratorAgent",
    "SubAgent",
    "GitHubIntegrationAgent",
    "FileSearchAgent",
    "philosophical_dialogue",
]
