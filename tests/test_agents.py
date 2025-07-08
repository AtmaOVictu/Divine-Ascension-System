import unittest

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.memory import Memory
from divine_agents.philosophy import (
    parse_philosophical_statement,
    simulate_emotional_tension,
    calculate_tension_change,
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


class TestPhilosophyUtilities(unittest.TestCase):
    def test_parse_statement(self):
        mem = Memory()
        parse_philosophical_statement("Resnica je ena", mem)
        self.assertEqual(len(mem.long_term), 1)

    def test_simulate_emotion(self):
        mem = Memory()
        emotion = {"name": "fear", "tension_level": 1.0}
        simulate_emotional_tension(emotion, duration=2, memory=mem)
        self.assertEqual(len(mem.short_term), 1)
        self.assertLess(calculate_tension_change(1.0, 2), 1.0)


if __name__ == '__main__':
    unittest.main()
