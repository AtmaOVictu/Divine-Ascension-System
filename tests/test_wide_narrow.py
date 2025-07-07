import unittest
from divine_agents.wide_narrow import WideAgent, NarrowAgent, debate


class TestWideNarrowAgents(unittest.TestCase):
    def test_wide_agent_transition_by_emotion(self):
        agent = WideAgent("W")
        agent.update_emotion(0.6)
        self.assertEqual(agent.transition(), "Jaz")

    def test_narrow_agent_action_triggered(self):
        agent = NarrowAgent("N", threshold=0.4)
        agent.update_tension(0.5)
        agent.check_threshold()
        self.assertTrue(agent.action_triggered)

    def test_debate_dialogue(self):
        a1 = WideAgent("A1")
        a2 = WideAgent("A2", state="Jaz")
        lines = debate(a1, a2)
        self.assertGreaterEqual(len(lines), 4)
        self.assertTrue(any("Resnica" in line for line in lines))


if __name__ == "__main__":
    unittest.main()
