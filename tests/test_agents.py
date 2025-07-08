import unittest

from divine_agents import (
    Agent,
    philosophical_dialogue,
    parse_philosophical_statement,
    simulate_emotional_tension,
    self_reflection,
    memory,
)


class TestAgentTransitions(unittest.TestCase):
    def setUp(self):
        # Clear memory before each test
        memory.long_term.clear()
        memory.short_term.clear()

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

    def test_parse_statement(self):
        parse_philosophical_statement("Truth is relative.")
        self.assertTrue(len(memory.long_term) == 1)

    def test_simulate_emotion(self):
        simulate_emotional_tension({"tension_level": 1.0}, duration=2)
        self.assertTrue(len(memory.short_term) == 1)

    def test_self_reflection(self):
        memory.store_long_term({"emotion": "resolved"})
        result = self_reflection()
        self.assertIn("1", result)


if __name__ == "__main__":
    unittest.main()
