import unittest
from divine_agents import Agent, philosophical_dialogue, debug_cycle


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

    def test_emotion_threshold_transition(self):
        agent = Agent("B")
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_debug_cycle_iterations(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = debug_cycle(a1, a2, iterations=3, seed=42)
        iterations_count = sum(1 for line in lines if line.startswith("-- Iteracija"))
        self.assertEqual(iterations_count, 3)


if __name__ == '__main__':
    unittest.main()
