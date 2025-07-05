import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, emotional_dialogue


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

    def test_emotional_dialogue_transitions(self):
        a1 = Agent("A1")
        a2 = Agent("A2")
        lines = emotional_dialogue(a1, a2, rounds=3)
        # at least one agent should reach Jaz or Enotnost after emotional buildup
        self.assertTrue(any(state in a1.history for state in ("Jaz", "Enotnost")) or
                        any(state in a2.history for state in ("Jaz", "Enotnost")))


if __name__ == '__main__':
    unittest.main()
