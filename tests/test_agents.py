import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, dynamic_debate


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

    def test_dynamic_debate_transitions(self):
        a1 = Agent("X")
        a2 = Agent("Y", state="Jaz")
        emotions1 = [0.2, 0.6]
        emotions2 = [0.3, 0.6]
        lines = dynamic_debate(a1, a2, emotions1, emotions2)
        self.assertEqual(a1.state, "Jaz")
        self.assertEqual(a2.state, "Enotnost")
        self.assertTrue(any("absolutna" in l or "relativna" in l or "eno" in l for l in lines))


if __name__ == '__main__':
    unittest.main()
