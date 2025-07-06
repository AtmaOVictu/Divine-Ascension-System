import unittest
from divine_agents.dynamic import DynamicAgent, MultiAgentSystem


class TestDynamicAgent(unittest.TestCase):
    def test_threshold_transition(self):
        agent = DynamicAgent("tester")
        agent.update_tension(0.8)
        self.assertEqual(agent.state, "Jaz")

    def test_emotion_transition(self):
        agent = DynamicAgent("tester", state="Jaz")
        agent.update_emotion(0.6)
        self.assertEqual(agent.state, "Enotnost")

    def test_dialogue_responses(self):
        a1 = DynamicAgent("A1")
        a2 = DynamicAgent("A2", state="Jaz")
        system = MultiAgentSystem()
        system.add_agent(a1)
        system.add_agent(a2)
        lines = system.interact()
        self.assertGreater(len(lines), 0)
        self.assertTrue(any("Resnica" in l for l in lines))


if __name__ == "__main__":
    unittest.main()
