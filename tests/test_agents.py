import unittest

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_by_tension(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_transition_by_emotion(self):
        agent = Agent("B")
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("C", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # After the dialogue, agent2 should transition to Enotnost
        self.assertIn("Enotnost", a2.state)
        # Check that dialogue lines contain references to different truths
        concatenated = " ".join(lines)
        self.assertIn("absolutna", concatenated)
        self.assertIn("relativna", concatenated)
        self.assertIn("eno", concatenated)


if __name__ == '__main__':
    unittest.main()
