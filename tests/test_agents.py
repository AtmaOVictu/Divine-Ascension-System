import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, philosophical_debate


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

    def test_debate_progression(self):
        a1 = Agent("A1")
        a2 = Agent("A2")
        transcript = philosophical_debate(a1, a2, rounds=3)
        # at least one agent should progress beyond Ego due to emotion increase
        self.assertTrue(any(state != "Ego" for state in (a1.state, a2.state)))
        # emotional responses should contain marker
        self.assertTrue(any("čustvo" in line for line in transcript))


if __name__ == '__main__':
    unittest.main()
