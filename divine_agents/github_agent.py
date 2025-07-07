from pathlib import Path
import subprocess
from .orchestrator import SubAgent


class GitHubIntegrationAgent(SubAgent):
    """Agent that retrieves branch names from a local Git repository."""

    def __init__(self, repo_path: str):
        self.repo_path = Path(repo_path)

    def is_relevant(self, input_data: str) -> bool:
        return "github" in input_data.lower() or "branch" in input_data.lower()

    def process(self, input_data: str) -> str:
        cmd = [
            "git",
            "-C",
            str(self.repo_path),
            "branch",
            "--format=%(refname:short)",
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        branches = [b.strip() for b in result.stdout.splitlines() if b.strip()]
        return f"Branches: {branches}"
