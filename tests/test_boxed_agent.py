import unittest
from divine_agents.boxed_agent import BoxedAgent
from divine_agents.dialogue import philosophical_dialogue


class TestBoxedAgent(unittest.TestCase):
    def test_transition_with_emotion(self):
        agent = BoxedAgent("A")
        agent.update_emotion(0.6, "fear")
        state = agent.transition()
        self.assertEqual(state, "Jaz")
        self.assertEqual(agent.self_box.get_data()["state"], "Jaz")

    def test_dialogue_responses(self):
        a1 = BoxedAgent("A1", state="Ego")
        a2 = BoxedAgent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        joined = "\n".join(lines)
        self.assertIn("relativna", joined)
        self.assertIn("čustvo", joined)


if __name__ == '__main__':
    unittest.main()
