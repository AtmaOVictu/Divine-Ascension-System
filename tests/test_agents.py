import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
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

    def test_multiple_contradictions(self):
        agent = Agent("B")
        agent.update_emotion(0.3)
        result = agent.interact(None, "The world is flat and I am not alive.")
        self.assertEqual(len(result), 2)
        self.assertIn("coexist", result[0])

    def test_self_reflection(self):
        agent = Agent("C")
        agent.update_emotion(0.6)
        agent.interact(None, "I am not alive")
        reflection = agent.reflect_on_beliefs()
        self.assertIn("reflects", reflection)


if __name__ == '__main__':
    unittest.main()
