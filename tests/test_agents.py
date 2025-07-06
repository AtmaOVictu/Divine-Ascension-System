import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, emotional_philosophical_dialogue


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

    def test_emotional_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        emotions1 = [(0.3, "jeza"), (0.6, "veselje")]
        emotions2 = [(0.2, "strah"), (0.8, "jeza")]
        lines = emotional_philosophical_dialogue(a1, a2, emotions1, emotions2)
        # After second round A1 should transition to Jaz and A2 to Enotnost
        self.assertIn("Jaz", a1.history[-1])
        self.assertIn("Enotnost", a2.history[-1])


if __name__ == '__main__':
    unittest.main()
