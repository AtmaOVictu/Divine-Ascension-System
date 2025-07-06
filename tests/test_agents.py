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

    def test_dynamic_debate(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        transcript = dynamic_debate(a1, a2, turns=2)
        # After debate both agents should have transitioned at least once
        self.assertNotEqual(a1.history[0], a1.state)
        self.assertNotEqual(a2.history[0], a2.state)
        # Ensure debate contains responses
        self.assertTrue(any("Resnica" in line for line in transcript))


if __name__ == '__main__':
    unittest.main()
