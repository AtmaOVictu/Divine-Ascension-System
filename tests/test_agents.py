import unittest

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_emotion_trigger(self):
        agent = Agent("B", state="Jaz")
        agent.update_emotion(0.6, "veselje")
        state = agent.transition()
        self.assertEqual(state, "Enotnost")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond()
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # ensure state transitions occurred
        self.assertIn("Jaz", a1.history)
        self.assertIn("Enotnost", a2.history)
        # check philosophical statements present
        joined = "\n".join(lines)
        self.assertIn("absolutna", joined)
        self.assertIn("relativna", joined)
        self.assertIn("eno", joined)


if __name__ == '__main__':
    unittest.main()
