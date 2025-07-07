import unittest
from divine_agents import Agent, ManagerAgent, SubAgent


class TestManagerAndSubAgent(unittest.TestCase):
    def test_manager_triggers_transition(self):
        agent = Agent("M")
        manager = ManagerAgent("Mgr")
        manager.add_agent(agent)
        agent.update_emotion(0.6)
        manager.manage_transitions()
        self.assertEqual(agent.state, "Jaz")

    def test_subagent_logging(self):
        agent = Agent("S")
        sub = SubAgent("helper", agent)
        sub.log_action("act")
        self.assertTrue(sub.logs)
        self.assertIn("helper", sub.logs[0])


if __name__ == "__main__":
    unittest.main()
