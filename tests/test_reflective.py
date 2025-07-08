import unittest
from divine_agents.reflective_agent import ReflectiveAgent
from divine_agents.dialogue import reflective_dialogue


class TestReflectiveAgent(unittest.TestCase):
    def test_reflection_triggers_transition(self):
        agent = ReflectiveAgent("R1")
        agent.reflect_and_write("test", "anger", "Argument")
        self.assertIn(agent.state, ["Jaz", "Enotnost"])

    def test_dialogue_history(self):
        a1 = ReflectiveAgent("A1")
        a2 = ReflectiveAgent("A2", state="Jaz")
        lines = reflective_dialogue(a1, a2)
        self.assertTrue(len(a1.writer.review_history()) > 0)
        self.assertTrue(len(a2.writer.review_history()) > 0)
        self.assertEqual(len(lines), 6)


if __name__ == "__main__":
    unittest.main()
