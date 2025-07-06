import unittest
from divine_agents import Agent, philosophical_dialogue, simulate_debate


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_emotion_transition(self):
        agent = Agent("B", state="Jaz")
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Enotnost")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_debate_simulation(self):
        a1 = Agent("P1")
        a2 = Agent("P2", state="Jaz")
        lines = simulate_debate(a1, a2, rounds=2)
        # at least one transition should occur in 2 rounds
        self.assertTrue(any("prehaja" in l for l in lines))


if __name__ == '__main__':
    unittest.main()
