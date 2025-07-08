import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


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

    def test_child_creation_and_inheritance(self):
        parent = Agent("Parent")
        parent.beliefs.append("Absolutna resnica")
        parent.update_emotion(0.4)
        child = parent.create_child("Child")
        self.assertEqual(child.parent, parent)
        self.assertIn("Absolutna resnica", child.beliefs)
        self.assertEqual(child.emotion, parent.emotion)
        self.assertIn(child, parent.children)


if __name__ == '__main__':
    unittest.main()
