import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.memory import memory
from divine_agents.utils import (
    parse_philosophical_statement,
    simulate_emotional_tension,
    handle_complex_query,
    self_reflection,
    augment_knowledge_base,
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

    def test_philosophical_storage(self):
        message = parse_philosophical_statement("Truth is relative to context")
        self.assertIn("parsed", message)
        self.assertGreater(len(memory.long_term), 0)

    def test_emotional_simulation(self):
        result = simulate_emotional_tension({"tension_level": 1.0}, 3)
        self.assertIn("Final tension", result)

    def test_complex_query(self):
        response = handle_complex_query("This is a paradox of time")
        self.assertIn("Analyzing", response)

    def test_self_reflection(self):
        augment_knowledge_base({"emotion": "resolved"})
        report = self_reflection()
        self.assertIn("Improvements", report)


if __name__ == '__main__':
    unittest.main()
