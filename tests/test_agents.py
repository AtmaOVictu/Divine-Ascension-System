import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

        # no transition if thresholds not reached
        agent2 = Agent("B")
        agent2.update_tension(0.5)
        state2 = agent2.transition()
        self.assertEqual(state2, "Ego")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

        agent.update_emotion(0.6)
        emotional_reply = agent.respond("Kaj je resnica?")
        self.assertIn("custva", emotional_reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # At least one line should mention a transition to Enotnost
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
