import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.memory import Memory
from divine_agents.utils import (
    parse_philosophical_statement,
    simulate_emotional_tension,
    calculate_tension_change,
    handle_complex_query,
    self_reflection,
)


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


class TestUtilities(unittest.TestCase):
    def test_parse_statement(self):
        memory = Memory()
        parse_philosophical_statement("Truth is absolute", memory)
        self.assertEqual(len(memory.long_term), 1)
        self.assertTrue(memory.long_term[0]["concept"]["absolute"])

    def test_emotional_simulation(self):
        memory = Memory()
        result = simulate_emotional_tension({"tension_level": 1.0}, 3, memory)
        expected = calculate_tension_change(1.0, 3)
        self.assertIn("Final tension", result)
        self.assertAlmostEqual(memory.short_term[0]["final_tension"], expected)

    def test_complex_query(self):
        memory = Memory()
        reply = handle_complex_query("This is a paradox", memory)
        self.assertEqual(reply, "Paradox analyzed.")

    def test_self_reflection(self):
        memory = Memory()
        memory.history.append({"emotion": "resolved"})
        message = self_reflection(memory)
        self.assertIn("1", message)


if __name__ == '__main__':
    unittest.main()
