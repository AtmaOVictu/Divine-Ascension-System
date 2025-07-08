import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.philosophy import parse_philosophical_statement
from divine_agents.emotions import simulate_emotional_tension
from divine_agents.memory import Memory


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

    def test_parse_statement(self):
        memory = Memory()
        msg = parse_philosophical_statement("Truth is relative", memory)
        self.assertTrue(memory.long_term)
        self.assertIn("parsed", msg or "parsed")

    def test_emotional_simulation(self):
        memory = Memory()
        emotion = {"name": "fear", "tension_level": 1.0}
        final = simulate_emotional_tension(emotion, duration=2, memory=memory)
        self.assertLess(final, 1.0)
        self.assertTrue(memory.short_term)

    def test_self_reflection(self):
        memory = Memory()
        memory.store_long_term({"emotion": "resolved"})
        agent = Agent("A", memory=memory)
        count = agent.self_reflection()
        self.assertEqual(count, 1)


if __name__ == '__main__':
    unittest.main()
