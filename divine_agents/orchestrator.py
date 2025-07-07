class BaseProcessingAgent:
    """Interface for specialized processing agents."""

    def is_relevant(self, input_data: str) -> bool:
        raise NotImplementedError

    def process(self, input_data: str) -> str:
        raise NotImplementedError


class OrchestratorAgent:
    """Top-level agent that delegates tasks to sub-agents."""

    def __init__(self, name: str = "Orchestrator"):
        self.name = name
        self.sub_agents = []

    def add_sub_agent(self, agent: BaseProcessingAgent) -> None:
        self.sub_agents.append(agent)

    def run(self, input_data: str) -> str:
        for agent in self.sub_agents:
            if agent.is_relevant(input_data):
                return agent.process(input_data)
        return "No relevant agent found." 



import os
import subprocess

class GitHubIntegrationAgent(BaseProcessingAgent):
    """Agent that retrieves branch information from a git repository."""

    def __init__(self, repo_path: str):
        self.repo_path = repo_path

    def is_relevant(self, input_data: str) -> bool:
        return "github" in input_data.lower()

    def process(self, input_data: str) -> str:
        try:
            output = subprocess.check_output(
                ["git", "-C", self.repo_path, "branch", "--list"],
                text=True,
            )
            branches = [b.strip().lstrip("* ") for b in output.splitlines() if b]
        except subprocess.CalledProcessError:
            branches = []
        return f"Branches: {branches}"


class FileSearchAgent(BaseProcessingAgent):
    """Agent that searches for a file name within a directory tree."""

    def __init__(self, base_dir: str):
        self.base_dir = base_dir

    def is_relevant(self, input_data: str) -> bool:
        return "file" in input_data.lower()

    def process(self, input_data: str) -> str:
        target = input_data.split()[-1]
        matches = []
        for root, _dirs, files in os.walk(self.base_dir):
            if target in files:
                matches.append(os.path.join(root, target))
        return f"Found files: {matches}"
