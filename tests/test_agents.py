import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.symbolic_box import SymbolicBox


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


class TestSymbolicBox(unittest.TestCase):
    def test_audit_trail(self):
        box = SymbolicBox(stage="∴", emotion=0.2, tension=0.3)
        box.transition("∆", emotion=0.6, tension=0.8)
        trail = box.get_audit_trail()
        self.assertEqual(len(trail), 1)
        record = trail[0]
        self.assertEqual(record.old_state, "∴")
        self.assertEqual(record.new_state, "∆")
        self.assertAlmostEqual(record.emotion, 0.6)
        self.assertAlmostEqual(record.tension, 0.8)
        self.assertIsNotNone(record.timestamp)


if __name__ == '__main__':
    unittest.main()
