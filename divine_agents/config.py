import json
from pathlib import Path
from typing import List, Dict


class CodexConfig:
    """Load agent configuration from a JSON file."""

    def __init__(self, config_file: str = "settings.json"):
        self.config_file = Path(config_file)
        self.config_data = self._load_config()

    def _load_config(self) -> Dict:
        with self.config_file.open("r", encoding="utf-8") as file:
            return json.load(file)

    def get_agents(self) -> List[Dict]:
        """Return list of agent descriptions."""
        return self.config_data.get("agents", [])
