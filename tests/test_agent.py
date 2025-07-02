import unittest

from src.agent import Agent


class TestAgent(unittest.TestCase):
    def test_transition_with_high_tension(self):
        agent = Agent(name="A", tension=0.8)
        agent.check_transition()
        self.assertEqual(agent.state, "Jaz")

    def test_transition_with_high_emotion(self):
        agent = Agent(name="B", state="Jaz", emotion=0.6)
        agent.check_transition()
        self.assertEqual(agent.state, "Enotnost")

    def test_no_transition_when_below_thresholds(self):
        agent = Agent(name="C", tension=0.5, emotion=0.4)
        agent.check_transition()
        self.assertEqual(agent.state, "Ego")

    def test_philosophical_responses(self):
        agent = Agent(name="A")
        self.assertIn("absolutna", agent.philosophical_response())
        agent.state = "Jaz"
        self.assertIn("relativna", agent.philosophical_response())
        agent.state = "Enotnost"
        self.assertIn("eno", agent.philosophical_response())


if __name__ == "__main__":
    unittest.main()
