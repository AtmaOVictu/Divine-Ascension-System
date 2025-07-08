import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.memory import Memory
from divine_agents.philosophy_utils import (
    parse_philosophical_statement,
    simulate_emotional_tension,
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

    def test_philosophical_parsing(self):
        memory = Memory()
        msg = parse_philosophical_statement("Biti je vse", memory)
        self.assertIn("stored", msg)
        self.assertEqual(len(memory.long_term), 1)

    def test_emotional_tension_simulation(self):
        tension = simulate_emotional_tension({"tension_level": 1.0}, duration=2)
        self.assertAlmostEqual(tension, 1.0 * (1 - 0.05 * 2))


if __name__ == '__main__':
    unittest.main()
