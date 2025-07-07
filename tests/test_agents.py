import os
import unittest
from divine_agents import (
    Agent,
    philosophical_dialogue,
    OrchestratorAgent,
    GitHubIntegrationAgent,
    FileSearchAgent,
)


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_emotion_threshold(self):
        agent = Agent("B")
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))


class TestOrchestrator(unittest.TestCase):
    def test_orchestrator_delegation(self):
        orch = OrchestratorAgent()
        orch.add_sub_agent(GitHubIntegrationAgent(repo_path="."))
        result = orch.run("github info")
        self.assertIn("Branches", result)

    def test_file_search_agent(self):
        orch = OrchestratorAgent()
        orch.add_sub_agent(FileSearchAgent(base_dir="."))
        # search for this test file itself
        result = orch.run("find file test_agents.py")
        self.assertIn("test_agents.py", result)


if __name__ == "__main__":
    unittest.main()
