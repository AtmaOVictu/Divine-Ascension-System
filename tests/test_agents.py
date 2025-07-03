import unittest
from divine_agents import Agent, philosophical_dialogue, debate


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


class TestDebate(unittest.TestCase):
    def test_debate_transitions(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        transcript = debate(a1, a2, rounds=2, seed=42)
        # After two rounds with seed, second agent should reach Enotnost
        self.assertIn("A2 prehaja v stanje: Enotnost", transcript)
        self.assertTrue(len(a2.history) > 1)


if __name__ == '__main__':
    unittest.main()
