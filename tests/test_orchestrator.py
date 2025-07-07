import unittest
from divine_agents import (
    OrchestratorAgent,
    GitHubIntegrationAgent,
    FileSearchAgent,
)


class TestOrchestrator(unittest.TestCase):
    def test_delegation(self):
        orchestrator = OrchestratorAgent()
        orchestrator.add_sub_agent(GitHubIntegrationAgent(repo_path="."))
        orchestrator.add_sub_agent(FileSearchAgent(root=".", pattern="README.md"))

        output_branch = orchestrator.run("List github branches")
        self.assertIn("Branches", output_branch)

        output_files = orchestrator.run("search file")
        self.assertIn("Found", output_files)


if __name__ == "__main__":
    unittest.main()
