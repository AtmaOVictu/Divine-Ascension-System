import json
from pathlib import Path
from typing import Any, Dict, List

from .codex_agent import CodexAgent


class CodexConfig:
    """Load agent configuration from a JSON file."""

    def __init__(self, config_file: str = "settings.json") -> None:
        self.config_file = Path(config_file)
        self.config_data = self.load_config()

    def load_config(self) -> Dict[str, Any]:
        with self.config_file.open("r", encoding="utf-8") as file:
            return json.load(file)

    def get_agents(self) -> List[Dict[str, Any]]:
        """Return list of agent definitions."""
        return self.config_data.get("agents", [])

    def instantiate_agents(self) -> List[CodexAgent]:
        """Instantiate CodexAgent objects from configuration."""
        agents: List[CodexAgent] = []
        for info in self.get_agents():
            agent = CodexAgent(
                ime=info["ime"],
                filozofija=info["filozofija"],
                motivacija=info["motivacija"],
                dimenzija=info["dimenzija"],
            )
            agents.append(agent)
        return agents
